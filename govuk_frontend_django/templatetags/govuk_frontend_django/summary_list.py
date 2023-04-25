from django import template

from govuk_frontend_django.components.base import (
    SummaryListRow,
    SummaryListRowsActions,
    SummaryListRowsActionsItem,
    SummaryListRowsKey,
    SummaryListRowsValue,
)
from govuk_frontend_django.components.summary_list import (
    GovUKSummaryList,
    SummaryListCard,
    SummaryListCardActions,
    SummaryListCardActionsItems,
    SummaryListCardTitle,
)
from govuk_frontend_django.templatetags.govuk_frontend_django import (
    GovUKComponentNode,
    gds_register_tag,
)

register = template.Library()


class SummaryListCardActionsItemsNode(GovUKComponentNode):
    dataclass_cls = SummaryListCardActionsItems

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_card_actions_item",
    node_cls=SummaryListCardActionsItemsNode,
    end_if_not_contains=["text", "html"],
)


class SummaryListCardActionsNode(GovUKComponentNode):
    dataclass_cls = SummaryListCardActions

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["items"] = [
            node
            for node in self.get_sub_dataclasses_by_type(
                dataclass_cls=SummaryListCardActionsItems,
                many=True,
            )
        ]
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_card_actions",
    node_cls=SummaryListCardActionsNode,
)


class SummaryListCardTitleNode(GovUKComponentNode):
    dataclass_cls = SummaryListCardTitle

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_card_title",
    node_cls=SummaryListCardTitleNode,
    end_if_not_contains=["text", "html"],
)


class SummaryListCardNode(GovUKComponentNode):
    dataclass_cls = SummaryListCard

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["title"] = self.get_sub_dataclasses_by_type(
            dataclass_cls=SummaryListCardTitle,
            many=False,
        )
        component_kwargs["actions"] = self.get_sub_dataclasses_by_type(
            dataclass_cls=SummaryListCardActions,
            many=False,
        )
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_card",
    node_cls=SummaryListCardNode,
)


class SummaryListRowsValueNode(GovUKComponentNode):
    dataclass_cls = SummaryListRowsValue

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_row_value",
    node_cls=SummaryListRowsValueNode,
    end_if_not_contains=["text", "html"],
)


class SummaryListRowsActionsItemNode(GovUKComponentNode):
    dataclass_cls = SummaryListRowsActionsItem

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_row_actions_item",
    node_cls=SummaryListRowsActionsItemNode,
    end_if_not_contains=["text", "html"],
)


class SummaryListRowsActionsNode(GovUKComponentNode):
    dataclass_cls = SummaryListRowsActions

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["items"] = [
            node
            for node in self.get_sub_dataclasses_by_type(
                dataclass_cls=SummaryListRowsActionsItem,
                many=True,
            )
        ]
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_row_actions",
    node_cls=SummaryListRowsActionsNode,
)


class SummaryListRowsKeyNode(GovUKComponentNode):
    dataclass_cls = SummaryListRowsKey

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        rendered_contents = self.nodelist.render(context).strip()
        if rendered_contents and "html" not in component_kwargs:
            component_kwargs["html"] = rendered_contents
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_row_key",
    node_cls=SummaryListRowsKeyNode,
    end_if_not_contains=["text", "html"],
)


class SummaryListRowNode(GovUKComponentNode):
    dataclass_cls = SummaryListRow

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["key"] = self.get_sub_dataclasses_by_type(
            dataclass_cls=SummaryListRowsKey,
            many=False,
        )

        component_kwargs["value"] = self.get_sub_dataclasses_by_type(
            dataclass_cls=SummaryListRowsValue,
            many=False,
        )

        component_kwargs["actions"] = self.get_sub_dataclasses_by_type(
            dataclass_cls=SummaryListRowsActions,
            many=False,
        )
        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list_row",
    node_cls=SummaryListRowNode,
)


class SummaryListNode(GovUKComponentNode):
    dataclass_cls = GovUKSummaryList

    def build_component_kwargs(self, context):
        component_kwargs = super().build_component_kwargs(context)

        component_kwargs["card"] = self.get_sub_dataclasses_by_type(
            dataclass_cls=SummaryListCard,
            many=False,
        )

        component_kwargs["rows"] = [
            node
            for node in self.get_sub_dataclasses_by_type(
                dataclass_cls=SummaryListRow,
                many=True,
            )
        ]

        self.clear()
        return component_kwargs


gds_register_tag(
    library=register,
    name="gds_summary_list",
    node_cls=SummaryListNode,
)
