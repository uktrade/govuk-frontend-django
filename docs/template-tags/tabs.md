# Tabs

See: [https://design-system.service.gov.uk/components/tabs/](https://design-system.service.gov.uk/components/tabs/)

## Usage

To use the component, you need to load the `govuk_frontend_django` template tag library and then use the `gds_tabs` and `gds_tabs_tab` tags.

### Example:

```django
{% load govuk_frontend_django %}
...
{% gds_tabs id="tabs-1" title="Tab title" %}
    {% gds_tabs_tab id="tab-1" label="Tab 1" %}
        <strong>Test 1</strong>
    {% endgds_tabs_tab %}
    {% gds_tabs_tab id="tab-2" label="Tab 2" %}
        <strong>Test 2</strong>
    {% endgds_tabs_tab %}
    {% gds_tabs_tab id="tab-3" label="Tab 3" %}
        <strong>Test 3</strong>
    {% endgds_tabs_tab %}
{% endgds_tabs %}
```
