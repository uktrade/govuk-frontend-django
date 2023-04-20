# Cookie banner

See: [https://design-system.service.gov.uk/components/cookie-banner/](https://design-system.service.gov.uk/components/cookie-banner/)

## Usage

To use the component, you need to load the `govuk_frontend_django` template tag library and then use the `gds_cookie_banner`, `gds_cookie_banner_message` and `gds_cookie_banner_message_action` tags.

You can define HTML using the `set` tag and then use the `html` parameter of the `gds_cookie_banner_message` tag to render it.

### Example:

```django
{% load govuk_frontend_django %}
...
{% set message_3_html %}
    <p class="govuk-body">Message 3 content</p>
{% endset %}
{% gds_cookie_banner %}
    {% gds_cookie_banner_message headingText="Message 1 heading" %}
        <p class="govuk-body">Message 1 content</p>
        {% gds_cookie_banner_message_action text="Action 1" %}
        {% gds_cookie_banner_message_action text="Action 2" %}
    {% end_gds_cookie_banner_message %}
    {% gds_cookie_banner_message headingText="Message 2 heading" text="Message 2 content" %}
    {% gds_cookie_banner_message headingText="Message 3 heading" html=message_3_html %}
{% end_gds_cookie_banner %}
```
