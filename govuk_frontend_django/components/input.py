from dataclasses import dataclass
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
class InputInputwrapper:
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class InputSuffix:
    text: Optional[str] = None
    html: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class InputPrefix:
    text: Optional[str] = None
    html: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKInput(govuk_frontend_base.GovUKComponent):
    """GOV.UK Input

    See: https://design-system.service.gov.uk/components/input/
    """

    id: Optional[str] = None
    name: str
    type: Optional[str] = None
    inputmode: Optional[str] = None
    value: Optional[str] = None
    disabled: Optional[bool] = None
    describedBy: Optional[str] = None
    label: govuk_frontend_label.GovUKLabel
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    prefix: Optional[InputPrefix] = None
    suffix: Optional[InputSuffix] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    autocomplete: Optional[str] = None
    pattern: Optional[str] = None
    spellcheck: Optional[bool] = None
    autocapitalize: Optional[str] = None
    inputWrapper: Optional[InputInputwrapper] = None

    _jinja2_template = "govuk_frontend_jinja/components/input/macro.html"
    _macro_name = "govukInput"


COMPONENT = GovUKInput
