import importlib
import pathlib
from dataclasses import is_dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Type, Union, cast

from django import template
from django.forms import BoundField
from django.template.base import (
    FilterExpression,
    Node,
    NodeList,
    Parser,
    Token,
    token_kwargs,
)
from django.template.context import Context
from django.template.defaulttags import ForNode, IfNode

from govuk_frontend_django.components.base import GovUKComponent

if TYPE_CHECKING:
    from _typeshed import DataclassInstance

register = template.Library()

SubDataclassWithNode = Tuple["DataclassInstance", Node]
DataclassDict = Dict[str, Any]
SubDataclassDictWithNode = Tuple[DataclassDict, Node]
SubDataclassDictWithOrWithoutNode = Union[DataclassDict, SubDataclassDictWithNode]


class ResolvingNode(Node):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sub_dataclasses: List[SubDataclassWithNode] = []

    def clear(self) -> None:
        self.sub_dataclasses = []

    def resolve_nodelist(self, nodelist: NodeList, context: Context) -> None:
        for node in nodelist:
            if isinstance(node, GovUKComponentNode):
                dcls = node.resolve_dataclass(context, as_dict=False)
                assert is_dataclass(dcls)

                dcls_with_node = cast(SubDataclassWithNode, (dcls, node))
                self.sub_dataclasses.append(dcls_with_node)
                self.sub_dataclasses.extend(node.sub_dataclasses)
                continue

            if isinstance(node, IfNode):
                node = ComponentIfNode(conditions_nodelists=node.conditions_nodelists)

            if isinstance(node, ForNode):
                node = ComponentForNode(
                    loopvars=node.loopvars,
                    sequence=node.sequence,
                    is_reversed=node.is_reversed,
                    nodelist_loop=node.nodelist_loop,
                    nodelist_empty=node.nodelist_empty,
                )

            if hasattr(node, "resolve"):
                node.resolve(context)
            if hasattr(node, "sub_dataclasses"):
                self.sub_dataclasses.extend(node.sub_dataclasses)

    def resolve(
        self,
        context: Context,
    ) -> None:
        nodelist = getattr(self, "nodelist", NodeList())
        self.resolve_nodelist(nodelist, context)

    def get_sub_dataclasses_by_type(
        self,
        dataclass_cls: Type,
        many: bool = True,
        include_node: bool = False,
    ) -> Union[
        SubDataclassDictWithOrWithoutNode, List[SubDataclassDictWithOrWithoutNode]
    ]:
        if not hasattr(self, "sub_dataclasses"):
            return []

        sub_dataclasses: List[SubDataclassDictWithOrWithoutNode] = []
        for dc in self.sub_dataclasses:
            if isinstance(dc[0], dataclass_cls):
                if include_node:
                    sub_dataclasses.append(
                        (
                            dc[0].__dict__,
                            dc[1],
                        )
                    )
                else:
                    sub_dataclasses.append(dc[0].__dict__)

        if not many and sub_dataclasses:
            return sub_dataclasses[0]
        return sub_dataclasses


class ComponentIfNode(ResolvingNode, IfNode):
    """
    Custom IfNode that will only resolve the nodelist if the condition is True.
    """

    def resolve(self, context: Context, **kwargs):
        """
        See: IfNode.render
        """
        super().resolve(context)

        self.sub_dataclasses = []

        for condition, nodelist in self.conditions_nodelists:
            if condition is not None:  # if / elif clause
                try:
                    match = condition.eval(context.flatten())
                except template.VariableDoesNotExist:
                    match = None
            else:  # else clause
                match = True

            if match:
                self.resolve_nodelist(nodelist, context)


class ComponentForNode(ResolvingNode, ForNode):
    """
    Custom ForNode that will resolve the nodelist as per the loop.
    """

    def resolve(self, context: Context, **kwargs):
        """
        See: ForNode.render
        """
        assert isinstance(self.sequence, FilterExpression)

        self.nodelist = NodeList()

        if "forloop" in context:
            parentloop = context["forloop"]
        else:
            parentloop = {}
        with context.push():
            values = self.sequence.resolve(context, ignore_failures=True)
            if values is None:
                values = []
            if not hasattr(values, "__len__"):
                values = list(values)
            len_values = len(values)
            if len_values < 1:
                assert isinstance(self.nodelist_empty, NodeList)
                return self.nodelist_empty.render(context)
            if self.is_reversed:
                values = reversed(values)
            num_loopvars = len(self.loopvars)
            unpack = num_loopvars > 1
            # Create a forloop value in the context.  We'll update counters on each
            # iteration just below.
            loop_dict = context["forloop"] = {"parentloop": parentloop}
            for i, item in enumerate(values):
                # Shortcuts for current loop iteration number.
                loop_dict["counter0"] = i
                loop_dict["counter"] = i + 1
                # Reverse counter iteration numbers.
                loop_dict["revcounter"] = len_values - i
                loop_dict["revcounter0"] = len_values - i - 1
                # Boolean values designating first and last times through loop.
                loop_dict["first"] = i == 0
                loop_dict["last"] = i == len_values - 1

                pop_context = False
                if unpack:
                    # If there are multiple loop variables, unpack the item into
                    # them.
                    try:
                        len_item = len(item)
                    except TypeError:  # not an iterable
                        len_item = 1
                    # Check loop variable count before unpacking
                    if num_loopvars != len_item:
                        raise ValueError(
                            "Need {} values to unpack in for loop; got {}. ".format(
                                num_loopvars, len_item
                            ),
                        )
                    unpacked_vars = dict(zip(self.loopvars, item))
                    pop_context = True
                    context.update(unpacked_vars)
                else:
                    context[self.loopvars[0]] = item

                assert isinstance(self.nodelist_loop, NodeList)

                self.resolve_nodelist(self.nodelist_loop, context)

                if pop_context:
                    # Pop the loop variables pushed on to the context to avoid
                    # the context ending up in an inconsistent state when other
                    # tags (e.g., include and with) push data to context.
                    context.pop()

        return super().resolve(context)


class GovUKComponentNode(ResolvingNode):
    dataclass_cls: Type["DataclassInstance"]

    def __init__(
        self,
        extra_context: Dict[str, FilterExpression],
        nodelist: Optional[NodeList] = None,
        dataclass_cls: Optional[Type["DataclassInstance"]] = None,
    ):
        self.nodelist = nodelist or NodeList()
        self.extra_context = extra_context
        if dataclass_cls:
            self.dataclass_cls = dataclass_cls
        self.resolved_kwargs: Dict[str, Any] = {}
        self.resolved_dataclass = None
        super().__init__()

    def resolve(self, context: Context):
        super().resolve(context)

        self.resolved_kwargs = {
            key: val.resolve(context)  # type: ignore
            for key, val in self.extra_context.items()
        }

    def build_component_kwargs(self, context: Context):
        self.resolve(context)
        component_kwargs = self.resolved_kwargs.copy()
        return component_kwargs

    def resolve_dataclass(
        self, context: Context, as_dict=True
    ) -> Union["DataclassInstance", DataclassDict]:
        self.resolved_dataclass = self.dataclass_cls(  # type: ignore
            **self.build_component_kwargs(context)
        )
        if as_dict:
            return self.resolved_dataclass.__dict__
        return self.resolved_dataclass  # type: ignore

    def render(self, context: Context) -> str:
        super().render(context)
        resolved_dataclass = self.resolve_dataclass(context, as_dict=False)

        if hasattr(resolved_dataclass, "render"):
            assert isinstance(resolved_dataclass, GovUKComponent)
            return resolved_dataclass.render()
        return ""


FIELD_COMPONENTS = [
    "character-count",
    "checkboxes",
    "date-input",
    "fieldset",
    "file-upload",
    "input",
    "radios",
    "select",
    "textarea",
]
COMPLEX_COMPONENTS = [
    "breadcrumbs",
    "cookie-banner",
    "error-summary",
    "footer",
    "header",
    "pagination",
    "phase-banner",
    "summary-list",
    "table",
    "tabs",
]


@register.tag
def gds_component(parser: Parser, token: Token):
    bits = token.split_contents()
    component_name = bits[1].replace("'", "").replace('"', "")

    if component_name in FIELD_COMPONENTS:
        raise Exception(
            f"Use the gds_field_component tag for {component_name} components."
        )
    if component_name in COMPLEX_COMPONENTS:
        raise Exception(
            f"{component_name} is a complex component with it's own templatetag."
        )

    remaining_bits = bits[2:]
    extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

    # Component dataclass
    underscored_component_name = component_name.replace("-", "_")
    module_name = f"govuk_frontend_django.components.{underscored_component_name}"
    module = importlib.import_module(module_name)
    dataclass_cls = getattr(module, "COMPONENT")

    return GovUKComponentNode(
        nodelist=NodeList(),
        extra_context=extra_context,
        dataclass_cls=dataclass_cls,
    )


@register.simple_tag
def gds_field_component(field: BoundField, **kwargs):
    return "Not yet implemented"


class SetNode(Node):
    def __init__(self, nodelist: NodeList, asvar: str):
        self.nodelist = nodelist
        self.asvar = asvar

    def resolve(self, context: Context):
        context[self.asvar] = self.nodelist.render(context)

    def render(self, context: Context):
        self.resolve(context)
        return ""


@register.tag
def set(parser: Parser, token: Token):
    nodelist = parser.parse(("endset",))
    parser.delete_first_token()

    bits = token.split_contents()
    node = SetNode(nodelist=nodelist, asvar=bits[1])

    return node


@register.simple_tag
def gds_component_template(jinja2_template: str, macro_name: str, **kwargs):
    """Fallback template tag for rendering a GovUK component.

    Args:
        jinja2_template (str): The path to the Jinja2 template.
        macro_name (str): The name of the macro to render.
        **kwargs: The keyword arguments to pass to the macro.

    Usage:
        {% gds_component_template jinja2_template="govuk_frontend_jinja/components/warning-text/macro.html" macro_name="govukWarningText" text="WARNING: something is wrong!" %}
    """

    component = GovUKComponent()
    component.set_jinja2_template(jinja2_template)
    component.set_macro_name(macro_name)
    return component.render(component_data={**kwargs})


def gds_register_tag(
    library: template.Library,
    name: str,
    node_cls: Type[GovUKComponentNode],
    has_end_tag: bool = True,
    end_if_not_contains: Optional[List[str]] = None,
):
    end_if_not_contains = end_if_not_contains or []

    def template_tag(parser: Parser, token: Token):
        assert end_if_not_contains is not None

        bits = token.split_contents()
        remaining_bits = bits[1:]
        nodelist = template.NodeList()
        extra_context = token_kwargs(remaining_bits, parser, support_legacy=True)

        if has_end_tag:
            if not any(
                [
                    end_if_not_contain in extra_context
                    for end_if_not_contain in end_if_not_contains
                ]
            ):
                nodelist = parser.parse((f"end{name}",))
                parser.delete_first_token()

        return node_cls(
            extra_context=extra_context,
            nodelist=nodelist,
        )

    library.tag(name=name, compile_function=template_tag)
    library.tag(name=name + "_inline", compile_function=template_tag)


# Loop over python files in this directory and update the register object
# with the tags and filters defined in each file.
for path in pathlib.Path(__file__).parent.iterdir():
    if path.suffix == ".py" and path.name != "__init__.py":
        module_name = path.stem
        module = importlib.import_module(f".{module_name}", __package__)
        register.tags.update(module.register.tags)
        register.filters.update(module.register.filters)
