from typing import List

from django import template

from govuk_frontend_django.components.header import GovUKHeader, HeaderNavigation
from govuk_frontend_django.components.tabs import TabsItems
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class HeaderNode(GovUKComponentNode):
    dataclass_cls = GovUKHeader

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["navigation"]: List[TabsItems] = [
            node
            for node in self.get_nodes_by_type_and_resolve(
                node_type=HeaderNavItemNode,
                context=context,
                many=True,
            )
        ]

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_header",
    node_cls=HeaderNode,
)


class HeaderNavItemNode(GovUKComponentNode):
    dataclass_cls = HeaderNavigation

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        href = component_kwargs["href"]
        component_kwargs["active"] = bool(href == context["request"].path)

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_header_nav_item",
    node_cls=HeaderNavItemNode,
    end_if_not_contains=["text", "html"],
)
