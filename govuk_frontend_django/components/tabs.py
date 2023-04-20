from dataclasses import dataclass
from typing import List, Optional

from govuk_frontend_django.components import base as govuk_frontend_base
from govuk_frontend_django.components import (
    error_message as govuk_frontend_error_message,
)
from govuk_frontend_django.components import fieldset as govuk_frontend_fieldset
from govuk_frontend_django.components import hint as govuk_frontend_hint
from govuk_frontend_django.components import label as govuk_frontend_label
from govuk_frontend_django.components import tag as govuk_frontend_tag


@dataclass(kw_only=True)
class TabsItems:
    id: str
    label: govuk_frontend_label.GovUKLabel
    attributes: Optional[govuk_frontend_base.Attributes] = None
    panel: govuk_frontend_base.TextAndHtml


@dataclass(kw_only=True)
class GovUKTabs(govuk_frontend_base.GovUKComponent):
    """GOV.UK Tabs

    See: https://design-system.service.gov.uk/components/tabs/
    """

    id: Optional[str] = None
    idPrefix: Optional[str] = None
    title: Optional[str] = None
    items: List[TabsItems]

    _jinja2_template = "govuk_frontend_jinja/components/tabs/macro.html"
    _macro_name = "govukTabs"


COMPONENT = GovUKTabs
