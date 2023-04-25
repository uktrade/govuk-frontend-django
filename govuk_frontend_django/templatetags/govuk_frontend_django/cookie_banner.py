from typing import List

from django import template

from govuk_frontend_django.components.cookie_banner import (
    CookieBannerMessages,
    CookieBannerMessagesActions,
    GovUKCookieBanner,
)
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class CookieBannerNode(GovUKComponentNode):
    dataclass_cls = GovUKCookieBanner

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["messages"]: List[CookieBannerMessages] = [
            node
            for node in self.get_nodes_by_type_and_resolve(
                node_type=CookieBannerMessageNode,
                context=context,
                many=True,
            )
        ]

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_cookie_banner",
    node_cls=CookieBannerNode,
)


class CookieBannerMessageNode(GovUKComponentNode):
    dataclass_cls = CookieBannerMessages

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["actions"]: List[CookieBannerMessagesActions] = [
            node
            for node in self.get_nodes_by_type_and_resolve(
                node_type=CookieBannerMessageActionNode,
                context=context,
                many=True,
            )
        ]

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in self.extra_context:
            component_kwargs["html"] = rendered_contents

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_cookie_banner_message",
    node_cls=CookieBannerMessageNode,
    end_if_not_contains=["text", "html"],
)


class CookieBannerMessageActionNode(GovUKComponentNode):
    dataclass_cls = CookieBannerMessagesActions

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_cookie_banner_message_action",
    node_cls=CookieBannerMessageActionNode,
    has_end_tag=False,
)
