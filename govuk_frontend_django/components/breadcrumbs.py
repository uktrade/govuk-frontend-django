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
class BreadcrumbsItems:
    text: Optional[str] = None
    html: Optional[str] = None
    href: Optional[str] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKBreadcrumbs(govuk_frontend_base.GovUKComponent):
    """GOV.UK Breadcrumbs

    See: https://design-system.service.gov.uk/components/breadcrumbs/
    """

    items: List[BreadcrumbsItems]
    collapseOnMobile: Optional[bool] = None
    labelText: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/breadcrumbs/macro.html"
    _macro_name = "govukBreadcrumbs"


COMPONENT = GovUKBreadcrumbs
