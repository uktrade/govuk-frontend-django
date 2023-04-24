import importlib
import pathlib
from dataclasses import dataclass
from typing import Dict, List, Optional, Type, Union

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

from govuk_frontend_django.components.base import GovUKComponent

register = template.Library()


class GovUKComponentNode(Node):
    dataclass_cls: Type[dataclass]

    def __init__(
        self,
        extra_context: Dict[str, FilterExpression],
        nodelist: Optional[NodeList] = None,
        dataclass_cls: Type[dataclass] = None,
    ):
        self.nodelist = nodelist or NodeList()
        self.extra_context = extra_context
        if dataclass_cls:
            self.dataclass_cls = dataclass_cls
        self.resolved_kwargs = {}

    def resolve(self, context):
        # Add any SetNodes to the context
        for node in self.nodelist.get_nodes_by_type(SetNode):
            node.resolve(context)

        if not self.resolved_kwargs:
            self.resolved_kwargs = {
                key: val.resolve(context) for key, val in self.extra_context.items()
            }

    def build_component_kwargs(self, context):
        self.resolve(context)
        return self.resolved_kwargs.copy()

    def resolve_dataclass(self, context, as_dict=True) -> Union[GovUKComponent, Dict]:
        resolved_dataclass = self.dataclass_cls(**self.build_component_kwargs(context))
        if as_dict:
            return resolved_dataclass.__dict__
        return resolved_dataclass

    def render(self, context):
        super().render(context)
        resolved_dataclass = self.resolve_dataclass(context, as_dict=False)
        if hasattr(resolved_dataclass, "render"):
            return resolved_dataclass.render()
        return ""

    def get_node_by_type_and_resolve(
        self,
        node_type: Type["GovUKComponentNode"],
        context,
        **kwargs,
    ) -> Optional[GovUKComponent]:
        for node in self.nodelist.get_nodes_by_type(node_type):
            resolved_dataclass = node.resolve_dataclass(context, **kwargs)
            return resolved_dataclass
        return None


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
        nodelist=[],
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

    def resolve(self, context):
        context[self.asvar] = self.nodelist.render(context)

    def render(self, context):
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
    component._jinja2_template = jinja2_template
    component._macro_name = macro_name
    return component.render(component_data={**kwargs})


def gds_register_tag(
    library: template.Library,
    name: str,
    node_cls: GovUKComponentNode,
    has_end_tag: bool = True,
    end_if_not_contains: Optional[List[str]] = None,
):
    end_if_not_contains = end_if_not_contains or []

    def template_tag(parser: Parser, token: Token):
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


# Loop over python files in this directory and update the register object
# with the tags and filters defined in each file.
for path in pathlib.Path(__file__).parent.iterdir():
    if path.suffix == ".py" and path.name != "__init__.py":
        module_name = path.stem
        module = importlib.import_module(f".{module_name}", __package__)
        register.tags.update(module.register.tags)
        register.filters.update(module.register.filters)
