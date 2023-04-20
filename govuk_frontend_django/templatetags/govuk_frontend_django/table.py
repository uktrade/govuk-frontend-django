from typing import Dict, Iterable, List, Optional, Tuple, Union

from django import template
from django.db.models import Model
from django.db.models.query import QuerySet

from govuk_frontend_django.components.table import GovUKTable, TableHead, TableRows

register = template.Library()


@register.simple_tag
def gds_table(columns: List[Tuple[str, str]], rows: QuerySet | List[Dict], **kwargs):
    """GDS table template tag.

    Args:
        columns (List[Tuple[str, str]]):
            A list of tuples, each tuple should contain the key and the human
            readable name.
        rows (Iterable):
            An iterable object, could be a list of Dicts or a Model Queryset

    Usage:
        ```django
        {% load govuk_frontend_django %}
        {% gds_table ... %}
        ```
    """

    if isinstance(rows, QuerySet):
        fields = [column[0] for column in columns]
        rows = rows.values(*fields)

    table_head: List[TableHead] = []
    for column in columns:
        table_head.append(TableHead(text=column[1]))

    table_rows: List[List[TableRows]] = []
    for row in rows:
        table_row: List[TableRows] = []
        for column in columns:
            table_row.append(TableRows(text=row[column[0]]).__dict__)
        table_rows.append(table_row)

    return GovUKTable(head=table_head, rows=table_rows, **kwargs)
