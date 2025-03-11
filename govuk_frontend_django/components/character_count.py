from dataclasses import dataclass
from typing import Any, Optional

from govuk_frontend_django.components import base as govuk_frontend_base
from govuk_frontend_django.components import (
    error_message as govuk_frontend_error_message,
)
from govuk_frontend_django.components import fieldset as govuk_frontend_fieldset
from govuk_frontend_django.components import hint as govuk_frontend_hint
from govuk_frontend_django.components import label as govuk_frontend_label
from govuk_frontend_django.components import tag as govuk_frontend_tag


@dataclass(kw_only=True)
class CharacterCountCountmessage:
    classes: Optional[str] = None


@dataclass(kw_only=True)
class GovUKCharacterCount(govuk_frontend_base.GovUKComponent):
    """GOV.UK Character Count

    See: https://design-system.service.gov.uk/components/character-count/
    """

    id: Optional[str] = None
    name: str
    rows: Optional[str] = None
    value: Optional[str] = None
    maxlength: str
    maxwords: str
    threshold: Optional[str] = None
    label: govuk_frontend_label.GovUKLabel
    hint: Optional[govuk_frontend_hint.GovUKHint] = None
    errorMessage: Optional[govuk_frontend_error_message.GovUKErrorMessage] = None
    formGroup: Optional[govuk_frontend_base.FormGroup] = None
    spellcheck: Optional[bool] = None
    countMessage: Optional[CharacterCountCountmessage] = None
    textareaDescriptionText: Optional[str] = None
    charactersUnderLimitText: Optional[Any] = None
    charactersAtLimitText: Optional[str] = None
    charactersOverLimitText: Optional[Any] = None
    wordsUnderLimitText: Optional[Any] = None
    wordsAtLimitText: Optional[str] = None
    wordsOverLimitText: Optional[Any] = None

    _jinja2_template = "govuk_frontend_jinja/components/character-count/macro.html"
    _macro_name = "govukCharacterCount"


COMPONENT = GovUKCharacterCount
