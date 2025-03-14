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
class ServiceNavigationSlots:
    start: Optional[str] = None
    end: Optional[str] = None
    navigationStart: Optional[str] = None
    navigationEnd: Optional[str] = None


@dataclass(kw_only=True)
class ServiceNavigationNavigation:
    current: Optional[bool] = None
    active: Optional[bool] = None
    html: Optional[str] = None
    text: Optional[str] = None
    href: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKServiceNavigation(govuk_frontend_base.GovUKComponent):
    """GOV.UK Service Navigation

    See: https://design-system.service.gov.uk/components/service-navigation/
    """

    ariaLabel: Optional[str] = None
    menuButtonText: Optional[str] = None
    menuButtonLabel: Optional[str] = None
    navigationLabel: Optional[str] = None
    navigationId: Optional[str] = None
    navigationClasses: Optional[str] = None
    serviceName: Optional[str] = None
    serviceUrl: Optional[str] = None
    navigation: List[ServiceNavigationNavigation]
    slots: Optional[ServiceNavigationSlots] = None

    _jinja2_template = "govuk_frontend_jinja/components/service-navigation/macro.html"
    _macro_name = "govukServiceNavigation"


COMPONENT = GovUKServiceNavigation
