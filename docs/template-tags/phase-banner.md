# Phase banner

See: [https://design-system.service.gov.uk/components/phase-banner/](https://design-system.service.gov.uk/components/phase-banner/)

## Usage

To use the component, you need to load the `govuk_frontend_django` template tag library and then use the `gds_phase_banner` tag.


### Example:

```django
{% load govuk_frontend_django %}
...
{% gds_phase_banner text="Phase banner text" tag=phase_tag %}
    {% gds_component "tag" text="Tag content" %}
{% endgds_phase_banner %}
```
