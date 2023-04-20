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
class DateInputItems:
    id: Optional[str] = None
    name: str
    label: Optional[govuk_frontend_label.GovUKLabel] = None
    value: Optional[str] = None
    autocomplete: Optional[str] = None
    pattern: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKDateInput(govuk_frontend_base.GovUKComponent):
    """GOV.UK Date Input

    See: https://design-system.service.gov.uk/components/date-input/
    """

    id: str
    namePrefix: Optional[str] = None
    items: Optional[List[DateInputItems]] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    fieldset: Optional[govuk_frontend_fieldset.GovUKFieldset] = None

    _jinja2_template = "govuk_frontend_jinja/components/date-input/macro.html"
    _macro_name = "govukDateInput"


COMPONENT = GovUKDateInput
