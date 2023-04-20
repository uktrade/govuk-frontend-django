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
class GovUKAccordion(govuk_frontend_base.GovUKComponent):
    """GOV.UK Accordion

    See: https://design-system.service.gov.uk/components/accordion/
    """

    id: str
    headingLevel: Optional[int] = None
    rememberExpanded: Optional[bool] = None
    hideAllSectionsText: Optional[str] = None
    hideSectionText: Optional[str] = None
    hideSectionAriaLabelText: Optional[str] = None
    showAllSectionsText: Optional[str] = None
    showSectionText: Optional[str] = None
    showSectionAriaLabelText: Optional[str] = None
    items: List[govuk_frontend_base.AccordionItem]

    _jinja2_template = "govuk_frontend_jinja/components/accordion/macro.html"
    _macro_name = "govukAccordion"


COMPONENT = GovUKAccordion
