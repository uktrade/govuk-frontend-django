# Error summary

See: [https://design-system.service.gov.uk/components/error-summary/](https://design-system.service.gov.uk/components/error-summary/)

## Usage

To use the component, you need to load the `govuk_frontend_django` template tag library and then use the `gds_error_summary` and `gds_error_summary_error_list_item` tags.


### Example:

```django
{% load govuk_frontend_django %}
...
{% gds_error_summary titleText="Error summary" descriptionText="Some descriptions about the error summary." %}
    {% gds_error_summary_error_list_item href="/" text="Error item 1" %}
    {% gds_error_summary_error_list_item href="/" %}
        Error 2
    {% endgds_error_summary_error_list_item %}
{% endgds_error_summary %}
```
