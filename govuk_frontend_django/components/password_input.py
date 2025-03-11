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
class PasswordInputButton:
    classes: Optional[str] = None


@dataclass(kw_only=True)
class GovUKPasswordInput(govuk_frontend_base.GovUKComponent):
    """GOV.UK Password Input

    See: https://design-system.service.gov.uk/components/password-input/
    """

    id: Optional[str] = None
    name: str
    value: Optional[str] = None
    disabled: Optional[bool] = None
    describedBy: Optional[str] = None
    label: govuk_frontend_label.GovUKLabel
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    autocomplete: Optional[str] = None
    showPasswordText: Optional[str] = None
    hidePasswordText: Optional[str] = None
    showPasswordAriaLabelText: Optional[str] = None
    hidePasswordAriaLabelText: Optional[str] = None
    passwordShownAnnouncementText: Optional[str] = None
    passwordHiddenAnnouncementText: Optional[str] = None
    button: Optional[PasswordInputButton] = None

    _jinja2_template = "govuk_frontend_jinja/components/password-input/macro.html"
    _macro_name = "govukPasswordInput"


COMPONENT = GovUKPasswordInput
