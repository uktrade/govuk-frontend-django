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
class CookieBannerMessagesActions:
    text: str
    type: Optional[str] = None
    href: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class CookieBannerMessages:
    headingText: Optional[str] = None
    headingHtml: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    actions: Optional[List[CookieBannerMessagesActions]] = None
    hidden: Optional[bool] = None
    role: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKCookieBanner(govuk_frontend_base.GovUKComponent):
    """GOV.UK Cookie Banner

    See: https://design-system.service.gov.uk/components/cookie-banner/
    """

    ariaLabel: Optional[str] = None
    hidden: Optional[bool] = None
    messages: List[CookieBannerMessages]

    _jinja2_template = "govuk_frontend_jinja/components/cookie-banner/macro.html"
    _macro_name = "govukCookieBanner"


COMPONENT = GovUKCookieBanner
