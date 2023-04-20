# Table

See: [https://design-system.service.gov.uk/components/table/](https://design-system.service.gov.uk/components/table/)

## Usage

To use the tabs component, you need to load the `govuk_frontend_django` template tag library and then use the `gds_table` tag.
This tag takes the following arguments:

* `columns` - A list of tuples containing the column header, each tuple is made up of 2 parts:
    * The machine name of the column
    * The human readable name of the column
* `rows` - You can pass either:
    * A list of dictionaries containing the data for each row, each dictionary should be keyed by the machine name of the column
    * A Django QuerySet

### Example:

```django
{% load govuk_frontend_django %}
...
{% gds_table columns=table_columns rows=table_rows %}
```
