# Header

See: [https://design-system.service.gov.uk/components/header/](https://design-system.service.gov.uk/components/header/)

## Usage

To use the component, you need to load the `govuk_frontend_django` template tag library and then use the `gds_header` and `gds_header_nav_item` tags.

### Example:

```django
{% load govuk_frontend_django %}
...
{% gds_header homepageUrl="/" productName="Some product" serviceName="Service name" serviceUrl="/" %}
    {% gds_header_nav_item href="/" %}
        Nav item 1
    {% end_gds_header_nav_item %}
    {% gds_header_nav_item href="/" text="Nav item 2" %}
{% end_gds_header %}
```
