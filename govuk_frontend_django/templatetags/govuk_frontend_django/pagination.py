from typing import List, Optional

from django import template
from django.core.paginator import Page, Paginator
from django.utils.translation import gettext_lazy as _

from govuk_frontend_django.components.pagination import (
    GovUKPagination,
    PaginationItems,
    PaginationNext,
    PaginationPrevious,
)

register = template.Library()

# From Paginator.ELLIPSIS
ELLIPSIS = _("…")


@register.simple_tag
def gds_pagination(page_obj: Page):
    """GDS pagination template tag.

    Args:
        page_obj (Page):
            The Django Paginator Page object.

    Usage:
        This template tag is designed to be used with the Django pagination,
        below is an example of it being used with a ListView.

        *views.py:*
        ```python
        from django.views.generic import ListView
        from django.contrib.auth import get_user_model

        User = get_user_model()


        class UserListingView(ListView):
            template_name = "template.html"
            model = User
            paginate_by = 25
        ```

        *template.html:*
        ```django
        {% load govuk_frontend_django %}
        {% gds_pagination page_obj %}
        ```
    """

    previous: Optional[PaginationPrevious] = None
    next: Optional[PaginationNext] = None
    pagination_items: List[PaginationItems] = []

    if page_obj.has_previous():
        previous = PaginationPrevious(
            href=f"?page={page_obj.previous_page_number()}",
            labelText="Previous",
        ).__dict__  # type: ignore

    if page_obj.has_next():
        next = PaginationNext(
            href=f"?page={page_obj.next_page_number()}",
            labelText="Next",
        ).__dict__  # type: ignore

    for page_number in page_obj.paginator.get_elided_page_range(  # type: ignore
        page_obj.number, on_each_side=2, on_ends=1
    ):
        if page_number == ELLIPSIS:
            pagination_items.append(PaginationItems(href=None, ellipsis=True))
        else:
            pagination_items.append(
                PaginationItems(
                    number=page_number,
                    current=page_number == page_obj.number,
                    href=f"?page={page_number}",
                )
            )

    return GovUKPagination(previous=previous, next=next, items=pagination_items)
