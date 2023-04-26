from typing import List

from django import template

from govuk_frontend_django.components.breadcrumbs import (
    BreadcrumbsItems,
    GovUKBreadcrumbs,
)
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class BreadcrumbsNode(GovUKComponentNode):
    dataclass_cls = GovUKBreadcrumbs

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        if "items" not in self.resolved_kwargs:
            component_kwargs["items"] = [
                node
                for node in self.get_sub_dataclasses_by_type(
                    dataclass_cls=BreadcrumbsItems,
                    many=True,
                )
            ]

        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_breadcrumbs",
    node_cls=BreadcrumbsNode,
    end_if_not_contains=["items"],
)


class BreadcrumbsItemsNode(GovUKComponentNode):
    dataclass_cls = BreadcrumbsItems


gds_register_tag(
    library=register,
    name="gds_breadcrumb_item",
    node_cls=BreadcrumbsItemsNode,
    has_end_tag=False,
)
