# Accordion

See: [https://design-system.service.gov.uk/components/accordion/](https://design-system.service.gov.uk/components/accordion/)

## Usage

To use the accordion, you need to load the `govuk_frontend_django` template tag library and then use the following tags:

* `gds_summary_list`
    * `gds_summary_list_card`
        * `gds_summary_list_card_title`
        * `gds_summary_list_card_actions`
            * `gds_summary_list_card_actions_item`
    * `gds_summary_list_row`
        * `gds_summary_list_row_key`
        * `gds_summary_list_row_value`
        * `gds_summary_list_row_actions`
            * `gds_summary_list_row_actions_item`


### Example:

```django
{% load govuk_frontend_django %}
...
{% gds_summary_list %}
    {% gds_summary_list_card %}
        {% gds_summary_list_card_title text="This is a summary list card title" %}
        {% gds_summary_list_card_actions %}
            {% gds_summary_list_card_actions_item text="Action 1" href="/" %}
            {% gds_summary_list_card_actions_item href="/" %}
                Action 2
            {% end_gds_summary_list_card_actions_item %}
        {% end_gds_summary_list_card_actions %}
    {% end_gds_summary_list_card %}
    {% gds_summary_list_row %}
        {% gds_summary_list_row_key text="Key 1" %}
        {% gds_summary_list_row_value text="Value 1" %}
        {% gds_summary_list_row_actions %}
            {% gds_summary_list_row_actions_item text="Action 1" href="/" %}
            {% gds_summary_list_row_actions_item href="/" %}
                Action 2
            {% end_gds_summary_list_row_actions_item %}
        {% end_gds_summary_list_row_actions %}
    {% end_gds_summary_list_row %}
    {% gds_summary_list_row %}
        {% gds_summary_list_row_key %}
            Key 2
        {% end_gds_summary_list_row_key %}
        {% gds_summary_list_row_value %}
            Value 2
        {% end_gds_summary_list_row_value %}
        {% gds_summary_list_row_actions %}
            {% gds_summary_list_row_actions_item text="Action 1" href="/" %}
            {% gds_summary_list_row_actions_item href="/" %}
                Action 2
            {% end_gds_summary_list_row_actions_item %}
        {% end_gds_summary_list_row_actions %}
    {% end_gds_summary_list_row %}
{% end_gds_summary_list %}
```