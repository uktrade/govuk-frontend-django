from dataclasses import is_dataclass
from typing import Any, Dict

from django import template
from django.forms import BoundField
from django.template.context import Context

from govuk_frontend_django.components.base import CheckboxesConditional
from govuk_frontend_django.components.checkboxes import CheckboxesItems, GovUKCheckboxes
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    DataclassDict,
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class FieldNode(GovUKComponentNode):
    def resolve(self, context: Context):
        super().resolve(context)
        self.bound_field: BoundField = self.resolved_kwargs["field"]
        self.resolved_kwargs["name"] = self.bound_field.name
        self.resolved_kwargs["fieldset"] = {
            "legend": {
                "text": "How would you like to be contacted?",
                "isPageHeading": True,
                "classes": "govuk-fieldset__legend--l",
            }
        }

    def build_component_kwargs(self, context: Context):
        component_kwargs = super().build_component_kwargs(context)
        component_kwargs.pop("field")
        return component_kwargs


class CheckboxesNode(FieldNode):
    dataclass_cls = GovUKCheckboxes

    def build_component_kwargs(self, context: Context):
        component_kwargs = super().build_component_kwargs(context)

        self.checkbox_conditional_items: Dict[Any, DataclassDict] = {}
        for checkbox_conditional_item, node in self.get_sub_dataclasses_by_type(  # type: ignore
            dataclass_cls=CheckboxesConditional,
            many=True,
            include_node=True,
        ):
            assert isinstance(node, GovUKComponentNode)
            assert isinstance(checkbox_conditional_item, Dict)

            conditional_value = node.resolved_kwargs["value"]
            self.checkbox_conditional_items[
                conditional_value
            ] = checkbox_conditional_item

        component_kwargs["items"] = []

        if self.bound_field.field.choices:
            for choice in self.bound_field.field.choices:
                item = CheckboxesItems(
                    value=choice[0],
                    text=choice[1],  # type: ignore
                )
                if item.value in self.checkbox_conditional_items:
                    item.conditional = self.checkbox_conditional_items[item.value]  # type: ignore
                component_kwargs["items"].append(item.__dict__)

        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_checkboxes",
    node_cls=CheckboxesNode,
)


class CheckboxConditionalNode(GovUKComponentNode):
    dataclass_cls = CheckboxesConditional

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents

        del component_kwargs["value"]
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_checkbox_conditional",
    node_cls=CheckboxConditionalNode,
    end_if_not_contains=["html"],
)
