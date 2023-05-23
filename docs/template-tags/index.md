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
- [Cookie banner](./cookie-banner.md)
- [Error summary](./error-summary.md)
- [Footer](./footer.md)
- [Header](./header.md)
- [Pagination](./pagination.md)
- [Phase banner](./phase-banner.md)
- [Summary list](./summary-list.md)
- [Table](./table.md)
- [Tabs](./tabs.md)

### Formatting with djLint

If you use [djLint](https://github.com/Riverside-Healthcare/djLint) to format your templates, you will need to add the following `custom_blocks` to your settings as per the [Custom Blocks documentation](https://www.djlint.com/docs/configuration/#custom-blocks).

```
gds_accordion,gds_accordion_item,gds_breadcrumbs,gds_checkboxes,gds_checkbox_conditional,gds_cookie_banner,gds_cookie_banner_message,gds_error_summary,gds_error_summary_error_list_item,gds_footer,gds_footer_nav,gds_footer_meta,gds_header,gds_header_nav_item,gds_phase_banner,gds_summary_list,gds_summary_list_row,gds_summary_list_row_key,gds_summary_list_row_value,gds_summary_list_row_actions,gds_summary_list_row_actions_item,gds_summary_list_card,gds_summary_list_card_actions,gds_summary_list_card_actions_item,gds_tabs,gds_tabs_tab
```

Currently, djLint doesn't support the use of tags acting like either a tag or a block.

For example, in the code below the `gds_error_summary_error_list_item` tag is both used with and without an end tag:

```django
{% gds_error_summary titleText="Error summary" descriptionText="Some descriptions about the error summary." %}
    {% gds_error_summary_error_list_item href="/" text="Error item 1" %}
    {% gds_error_summary_error_list_item href="/" %}
        Error 2
    {% endgds_error_summary_error_list_item %}
{% endgds_error_summary %}
```

Running djLint over this example will result in poorly formatted templates.

The current workaround for this is to suffix the tag with `_inline` like so:

```django
{% gds_error_summary titleText="Error summary" descriptionText="Some descriptions about the error summary." %}
    {% gds_error_summary_error_list_item_inline href="/" text="Error item 1" %}
    {% gds_error_summary_error_list_item href="/" %}
        Error 2
    {% endgds_error_summary_error_list_item %}
{% endgds_error_summary %}
```

As you can see, the `gds_error_summary_error_list_item` without an end tag became `gds_error_summary_error_list_item_inline`. This workaround isn't ideal.

## Currently unsupported components

Currently we don't support the following components:

- [Character count](https://design-system.service.gov.uk/components/character-count/)
- [Checkboxes](https://design-system.service.gov.uk/components/checkboxes/)
- [Date input](https://design-system.service.gov.uk/components/date-input/)
- [Fieldset](https://design-system.service.gov.uk/components/fieldset/)
- [File upload](https://design-system.service.gov.uk/components/file-upload/)
- [Input](https://design-system.service.gov.uk/components/input/)
- [Radios](https://design-system.service.gov.uk/components/radios/)
- [Select](https://design-system.service.gov.uk/components/select/)
- [Textarea](https://design-system.service.gov.uk/components/textarea/)

These are all fields that are best implemented using [Crispy Forms GDS](https://github.com/wildfish/crispy-forms-gds).
