from typing import List

from django import template

from govuk_frontend_django.components.error_summary import (
    ErrorSummaryErrorlist,
    GovUKErrorSummary,
)
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class ErrorSummaryNode(GovUKComponentNode):
    dataclass_cls = GovUKErrorSummary

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["errorList"] = [
            node
            for node in self.get_sub_dataclasses_by_type(
                dataclass_cls=ErrorSummaryErrorlist,
                many=True,
            )
        ]
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_error_summary",
    node_cls=ErrorSummaryNode,
)


class ErrorSummaryErrorListItemNode(GovUKComponentNode):
    dataclass_cls = ErrorSummaryErrorlist

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in self.extra_context:
            component_kwargs["html"] = rendered_contents
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_error_summary_error_list_item",
    node_cls=ErrorSummaryErrorListItemNode,
    end_if_not_contains=["text", "html"],
)
