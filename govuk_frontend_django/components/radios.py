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
class RadiosItemsConditional:
    html: str


@dataclass(kw_only=True)
class RadiosItems:
    text: Optional[str] = None
    html: Optional[str] = None
    id: Optional[str] = None
    value: str
    label: Optional[govuk_frontend_label.GovUKLabel] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    divider: Optional[str] = None
    checked: Optional[bool] = None
    conditional: Optional[RadiosItemsConditional] = None
    disabled: Optional[bool] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKRadios(govuk_frontend_base.GovUKComponent):
    """GOV.UK Radios

    See: https://design-system.service.gov.uk/components/radios/
    """

    fieldset: Optional[govuk_frontend_fieldset.GovUKFieldset] = None
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    idPrefix: Optional[str] = None
    name: str
    items: List[RadiosItems]
    value: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/radios/macro.html"
    _macro_name = "govukRadios"


COMPONENT = GovUKRadios
