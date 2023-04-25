from typing import List

from django import template

from govuk_frontend_django.components.base import TextAndHtml
from govuk_frontend_django.components.tabs import GovUKTabs, TabsItems
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class TabsNode(GovUKComponentNode):
    dataclass_cls = GovUKTabs

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["items"]: List[TabsItems] = [
            node
            for node in self.get_nodes_by_type_and_resolve(
                node_type=TabsTabNode,
                context=context,
                many=True,
            )
        ]

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_tabs",
    node_cls=TabsNode,
)


class TabsTabNode(GovUKComponentNode):
    dataclass_cls = TabsItems

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["panel"] = TextAndHtml(html=self.nodelist.render(context))

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_tabs_tab",
    node_cls=TabsTabNode,
)
