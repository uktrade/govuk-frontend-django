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
class ErrorSummaryErrorlist:
    href: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKErrorSummary(govuk_frontend_base.GovUKComponent):
    """GOV.UK Error Summary

    See: https://design-system.service.gov.uk/components/error-summary/
    """

    titleText: Optional[str] = None
    titleHtml: Optional[str] = None
    descriptionText: Optional[str] = None
    descriptionHtml: Optional[str] = None
    errorList: Optional[List[ErrorSummaryErrorlist]] = None
    disableAutoFocus: Optional[bool] = None

    _jinja2_template = "govuk_frontend_jinja/components/error-summary/macro.html"
    _macro_name = "govukErrorSummary"


COMPONENT = GovUKErrorSummary
