from dataclasses import dataclass
from typing import Any, List, Optional

from govuk_frontend_django.components import base as govuk_frontend_base
from govuk_frontend_django.components import (
    error_message as govuk_frontend_error_message,
)
from govuk_frontend_django.components import fieldset as govuk_frontend_fieldset
from govuk_frontend_django.components import hint as govuk_frontend_hint
from govuk_frontend_django.components import label as govuk_frontend_label
from govuk_frontend_django.components import tag as govuk_frontend_tag


@dataclass(kw_only=True)
class TaskListItemsStatus:
    tag: Optional[Any] = None
    text: Optional[str] = None
    html: Optional[str] = None
    classes: Optional[str] = None


@dataclass(kw_only=True)
class TaskListItemsTitle:
    text: Optional[str] = None
    html: Optional[str] = None
    classes: Optional[str] = None


@dataclass(kw_only=True)
class TaskListItems:
    title: TaskListItemsTitle
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    status: TaskListItemsStatus
    href: Optional[str] = None
    classes: Optional[str] = None


@dataclass(kw_only=True)
class GovUKTaskList(govuk_frontend_base.GovUKComponent):
    """GOV.UK Task List

    See: https://design-system.service.gov.uk/components/task-list/
    """

    items: List[TaskListItems]
    idPrefix: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/task-list/macro.html"
    _macro_name = "govukTaskList"


COMPONENT = GovUKTaskList
