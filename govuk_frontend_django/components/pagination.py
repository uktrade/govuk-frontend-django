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
class PaginationNext:
    text: Optional[str] = None
    html: Optional[str] = None
    labelText: Optional[str] = None
    href: str
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class PaginationPrevious:
    text: Optional[str] = None
    html: Optional[str] = None
    labelText: Optional[str] = None
    href: str
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class PaginationItems:
    number: Optional[str] = None
    visuallyHiddenText: Optional[str] = None
    href: str
    current: Optional[bool] = None
    ellipsis: Optional[bool] = None
    attributes: Optional[govuk_frontend_base.Attributes] = None


@dataclass(kw_only=True)
class GovUKPagination(govuk_frontend_base.GovUKComponent):
    """GOV.UK Pagination

    See: https://design-system.service.gov.uk/components/pagination/
    """

    items: Optional[List[PaginationItems]] = None
    previous: Optional[PaginationPrevious] = None
    next: Optional[PaginationNext] = None
    landmarkLabel: Optional[str] = None

    _jinja2_template = "govuk_frontend_jinja/components/pagination/macro.html"
    _macro_name = "govukPagination"


COMPONENT = GovUKPagination
