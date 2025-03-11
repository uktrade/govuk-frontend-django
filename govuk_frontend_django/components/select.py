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
class SelectItems:
    value: Optional[str] = None
    text: str
    selected: Optional[bool] = None
    disabled: Optional[bool] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKSelect(govuk_frontend_base.GovUKComponent):
    """GOV.UK Select

    See: https://design-system.service.gov.uk/components/select/
    """

    id: Optional[str] = None
    name: str
    items: List[SelectItems]
    value: Optional[str] = None
    disabled: Optional[bool] = None
    describedBy: Optional[str] = None
    label: govuk_frontend_label.GovUKLabel
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None

    _jinja2_template = "govuk_frontend_jinja/components/select/macro.html"
    _macro_name = "govukSelect"


COMPONENT = GovUKSelect
