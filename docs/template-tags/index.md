# GDS Components template tags

See: [https://design-system.service.gov.uk/components/](https://design-system.service.gov.uk/components/) for more information on the GDS components.

## The gds_component tag
The `gds_component` templatetag allows you to render any component that has been implemented in the `govuk_frontend_django` package. The first arg taken is the hyphenated name for the component (e.g. "back-link" for the Back Link component). The remaining args are passed through as keyword arguments to the component.

Examples:

```django
{% load govuk_frontend_django %}

{% gds_component "back-link" href="/" %}
{% gds_component "button" text="Save" %}
{% gds_component "details" summaryText="Click me to see some hidden text" text="Some hidden text" %}
{% gds_component "error-message" text="An error message" %}
{% gds_component "hint" text="Some hint text" %}
{% gds_component "inset-text" text="Some inset text" %}
{% gds_component "label" text="A label" %}
{% gds_component "notification-banner" text="Notification banner" %}
{% gds_component "panel" titleText="Panel title" text="Panel content" %}
{% gds_component "skip-link" text="Skip to main content" %}
{% gds_component "tag" text="Tag content" %}
{% gds_component "warning-text" text="This is a warning" %}
```

## Complex template tags

Some of the components aren't a simple flat mapping, for these we implement custom template tags.

- [Accordion](./accordion.md)
- [Breadcrumbs](./breadcrumbs.md)
- [Header](./header.md)
- [Pagination](./pagination.md)
- [Tabs](./tabs.md)

## Currently unsupported components

The following components are not yet supported:

- Fields
    - [Character count](https://design-system.service.gov.uk/components/character-count/)
    - [Checkboxes](https://design-system.service.gov.uk/components/checkboxes/)
    - [Date input](https://design-system.service.gov.uk/components/date-input/)
    - [Fieldset](https://design-system.service.gov.uk/components/fieldset/)
    - [File upload](https://design-system.service.gov.uk/components/file-upload/)
    - [Input](https://design-system.service.gov.uk/components/input/)
    - [Radios](https://design-system.service.gov.uk/components/radios/)
    - [Select](https://design-system.service.gov.uk/components/select/)
    - [Textarea](https://design-system.service.gov.uk/components/textarea/)
- Complex components
    - [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/)
    - [Error summary](https://design-system.service.gov.uk/components/error-summary/)
    - [Footer](https://design-system.service.gov.uk/components/footer/)
    - [Phase banner](https://design-system.service.gov.uk/components/phase-banner/)
    - [Summary list](https://design-system.service.gov.uk/components/summary-list/)
    - [Table](https://design-system.service.gov.uk/components/table/)
