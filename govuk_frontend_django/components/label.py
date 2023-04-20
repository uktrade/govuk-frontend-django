from dataclasses import dataclass, field
from typing import Optional

from govuk_frontend_django.components import base as govuk_frontend_base
from govuk_frontend_django.components import (
    error_message as govuk_frontend_error_message,
)
from govuk_frontend_django.components import fieldset as govuk_frontend_fieldset
from govuk_frontend_django.components import hint as govuk_frontend_hint
from govuk_frontend_django.components import label as govuk_frontend_label
from govuk_frontend_django.components import tag as govuk_frontend_tag


@dataclass(kw_only=True)
class GovUKLabel(govuk_frontend_base.GovUKComponent):
    """GOV.UK Label

    See: https://design-system.service.gov.uk/components/label/
    """

    text: Optional[str] = None
    html: Optional[str] = None
    _for: Optional[str] = field(default=None, metadata={"name": "for"})
    isPageHeading: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/label/macro.html"
    _macro_name = "govukLabel"


COMPONENT = GovUKLabel
