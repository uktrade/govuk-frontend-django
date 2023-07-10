from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from django.utils.safestring import mark_safe
from jinja2 import (
    ChoiceLoader,
    Environment,
    PackageLoader,
    PrefixLoader,
    select_autoescape,
)

Attributes = Dict[str, Any]


class RenderableMixin:
    def get_context(self):
        raise NotImplementedError(
            "Subclasses of RenderableMixin must provide a get_context() method."
        )

    def render(self, template_name=None, context=None, renderer=None):
        raise NotImplementedError(
            "Subclasses of RenderableMixin must provide a render() method."
        )

    __str__ = render
    __html__ = render


@dataclass(kw_only=True)
class GovUKComponent(RenderableMixin):
    classes: Optional[str] = None
    attributes: Optional[Attributes] = None

    def set_jinja2_template(self, jinja2_template):
        self._jinja2_template = jinja2_template

    def set_macro_name(self, macro_name):
        self._macro_name = macro_name

    def build_jinja_template(self):
        return "".join(
            [
                "{%- from '",
                self._jinja2_template,
                "' import ",
                self._macro_name,
                " -%}",
                "{{ ",
                self._macro_name,
                "(data) }}",
            ]
        )

    def render(
        self,
        template_name=None,
        context=None,
        renderer=None,
        component_data=None,
    ):
        jinja_loader = ChoiceLoader(
            [
                PrefixLoader(
                    {"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}
                )
            ]
        )
        env = Environment(
            loader=jinja_loader,
            autoescape=select_autoescape(),
        )
        template = env.from_string(self.build_jinja_template())

        data = self.__dict__.copy()
        if component_data:
            data.update(component_data)

        def clean_data(data_to_clean: Union[Dict, List]):
            # Clean data
            # Iterate through the multi-level dict and remove any keys with a value of None
            if isinstance(data_to_clean, list):
                for item in data_to_clean:
                    clean_data(item)

            elif isinstance(data_to_clean, dict):
                for key, value in list(data_to_clean.items()):
                    if value is None:
                        del data_to_clean[key]
                    elif isinstance(value, dict) or isinstance(value, list):
                        clean_data(value)

        clean_data(data)

        return mark_safe(template.render(data=data))

    __str__ = render
    __html__ = render


@dataclass(kw_only=True)
class FieldsetLegend:
    text: str
    isPageHeading: bool
    classes: str


@dataclass(kw_only=True)
class TextAndHtml:
    text: Optional[str] = None
    html: Optional[str] = None


@dataclass(kw_only=True)
class FormGroup:
    classes: Optional[str] = None


"""
Accordion
"""


@dataclass(kw_only=True)
class AccordionItem:
    heading: Optional[TextAndHtml] = None
    summary: Optional[TextAndHtml] = None
    content: Optional[TextAndHtml] = None
    expanded: Optional[bool] = None


"""
Checkboxes
"""


@dataclass(kw_only=True)
class CheckboxesConditional:
    html: str


"""
Summary List
"""


@dataclass(kw_only=True)
class SummaryListRowsKey(TextAndHtml):
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListRowsValue(TextAndHtml):
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListRowsActionsItem:
    href: str
    text: Optional[str] = None
    html: Optional[str] = None
    visuallyHiddenText: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[Attributes] = None


@dataclass(kw_only=True)
class SummaryListRowsActions:
    items: List[SummaryListRowsActionsItem]
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListRow:
    classes: Optional[str] = None
    key: Optional[SummaryListRowsKey] = None
    value: Optional[SummaryListRowsValue] = None
    actions: Optional[SummaryListRowsActions] = None


SummaryListRows = List[SummaryListRow]
