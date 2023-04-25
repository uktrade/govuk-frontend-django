from typing import List

from django import template

from govuk_frontend_django.components.accordion import GovUKAccordion
from govuk_frontend_django.components.base import AccordionItem, TextAndHtml
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class AccordionNode(GovUKComponentNode):
    dataclass_cls = GovUKAccordion

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["items"]: List[AccordionItem] = [
            node
            for node in self.get_nodes_by_type_and_resolve(
                node_type=AccordionItemNode,
                context=context,
                many=True,
            )
        ]

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_accordion",
    node_cls=AccordionNode,
)


class AccordionItemNode(GovUKComponentNode):
    dataclass_cls = AccordionItem

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["heading"] = TextAndHtml(text=component_kwargs["heading"])
        component_kwargs["summary"] = TextAndHtml(text=component_kwargs["summary"])
        component_kwargs["content"] = TextAndHtml(html=self.nodelist.render(context))

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_accordion_item",
    node_cls=AccordionItemNode,
)
