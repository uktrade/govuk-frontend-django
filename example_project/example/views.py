import os
import pathlib
from typing import Any, Dict

from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

from govuk_frontend_django.components.accordion import GovUKAccordion
from govuk_frontend_django.components.back_link import GovUKBackLink
from govuk_frontend_django.components.breadcrumbs import (
    BreadcrumbsItems,
    GovUKBreadcrumbs,
)
from govuk_frontend_django.components.button import GovUKButton
from govuk_frontend_django.components.character_count import GovUKCharacterCount
from govuk_frontend_django.components.checkboxes import GovUKCheckboxes
from govuk_frontend_django.components.cookie_banner import GovUKCookieBanner
from govuk_frontend_django.components.date_input import GovUKDateInput
from govuk_frontend_django.components.error_message import GovUKErrorMessage
from govuk_frontend_django.components.pagination import GovUKPagination

User = get_user_model()


class UserListingView(ListView):
    template_name = "example/user_listing.html"
    model = User
    paginate_by = 1

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            user_columns=[
                ("first_name", "First name"),
                ("last_name", "Last name"),
            ]
        )
        return context


class CustomForm(forms.Form):
    # Checkboxes
    contact = forms.ChoiceField(
        label="How would you like to be contacted?",
        choices=(
            ("email", "Email"),
            ("phone", "Phone"),
            ("text", "Text"),
        ),
        widget=forms.CheckboxSelectMultiple,
    )


def components_view(request):
    context = {}
    context.update(
        form=CustomForm(),
        page_obj=UserListingView.as_view()(request).context_data["page_obj"],
        breadcrumb_items=[
            BreadcrumbsItems(
                text="Item 1",
                href="#",
            ),
            BreadcrumbsItems(
                text="Item 2",
                href="#",
            ),
            BreadcrumbsItems(
                text="Item 3",
                href="#",
            ),
        ],
        table_columns=[
            ("column_1", "Column 1"),
            ("column_2", "Column 2"),
            ("column_3", "Column 3"),
        ],
        table_rows=[
            {
                "column_1": "Row 1 Column 1",
                "column_2": "Row 1 Column 2",
                "column_3": "Row 1 Column 3",
            },
            {
                "column_1": "Row 2 Column 1",
                "column_2": "Row 2 Column 2",
                "column_3": "Row 2 Column 3",
            },
            {
                "column_1": "Row 3 Column 1",
                "column_2": "Row 3 Column 2",
                "column_3": "Row 3 Column 3",
            },
        ],
        model_table_columns=[
            ("first_name", "First Name"),
            ("last_name", "Last Name"),
            ("email", "Email"),
        ],
        model_table_rows=User.objects.all(),
    )

    return render(request, "example/templatetags.html", context)
