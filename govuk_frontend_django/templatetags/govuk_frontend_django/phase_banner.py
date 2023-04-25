from django import template

from govuk_frontend_django.components.base import GovUKComponent
from govuk_frontend_django.components.phase_banner import GovUKPhaseBanner
from govuk_frontend_django.components.tag import GovUKTag
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class PhaseBannerNode(GovUKComponentNode):
    dataclass_cls = GovUKPhaseBanner

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        nodes_to_hide = []

        component_kwargs["tag"] = None
        component_kwargs["tag"], tag_node = self.get_sub_dataclasses_by_type(
            dataclass_cls=GovUKTag,
            many=False,
            include_node=True,
        )
        nodes_to_hide.append(tag_node)

        for node_to_hide in nodes_to_hide:
            self.nodelist.remove(node_to_hide)

        rendered_contents = self.nodelist.render(context).strip()

        for node_to_hide in nodes_to_hide:
            self.nodelist.append(node_to_hide)

        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_phase_banner",
    node_cls=PhaseBannerNode,
)
