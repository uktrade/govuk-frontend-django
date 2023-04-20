# Footer

See: [https://design-system.service.gov.uk/components/footer/](https://design-system.service.gov.uk/components/footer/)

## Usage

To use the footer component, you need to load the `govuk_frontend_django` template tag library and then use the `gds_footer` and `gds_footer_nav_item` tags.


### Example:

```django
{% load govuk_frontend_django %}
...
{% gds_footer %}
    {% gds_footer_nav title="Services and information" width="two-thirds" columns=2 %}
        {% gds_footer_nav_item href="/" text="Footer nav item 1" %}
        {% gds_footer_nav_item href="/" text="Footer nav item 2" %}
        {% gds_footer_nav_item href="/" text="Footer nav item 3" %}
    {% end_gds_footer_nav %}

    {% gds_footer_nav title="Departments and policy" width="one-third" %}
        {% gds_footer_nav_item href="/" text="Footer nav item 4" %}
        {% gds_footer_nav_item href="/" text="Footer nav item 5" %}
        {% gds_footer_nav_item href="/" text="Footer nav item 6" %}
    {% end_gds_footer_nav %}

    {% gds_footer_meta text="meta" %}
        {% gds_footer_meta_item href="/" text="Meta item 1" %}
        {% gds_footer_meta_item href="/" text="Meta item 2" %}
        {% gds_footer_meta_item href="/" text="Meta item 3" %}
        {% gds_footer_meta_item href="/" text="Meta item 4" %}
    {% end_gds_footer_meta %}

    {% gds_footer_content_licence text="content licence text" %}
    {% gds_footer_copyright text="copyright text" %}
{% end_gds_footer %}
```
