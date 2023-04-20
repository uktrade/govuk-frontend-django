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
            breadcrum_items: List[BreadcrumbsItems] = []
            for node in self.get_nodes_by_type(BreadcrumbsItemsNode):
                breadcrum_items.append(node.resolve_dataclass(context))

            component_kwargs["items"] = breadcrum_items

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
