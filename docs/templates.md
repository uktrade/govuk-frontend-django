---
hide:
  - navigation
---

# Templates

Below are a list of templates that you can use in your Django project.

## Base template

See: [GDS base template](https://design-system.service.gov.uk/styles/page-template/)

`govuk_frontend_django/base.html`

You should create your own `base.html` template that extends this one, this will give you one location to add your own CSS and JS.

**Example:**
```django
{% extends "govuk_frontend_django/base.html" %}
{% load static govuk_frontend_django %}

{% block title %}GOV.UK Frontend Django example project{% endblock title %}

{% block head %}
    <link href="{% static 'css/styles.css' %}" rel="stylesheet" type="text/css" />
{% endblock head %}

{% block header %}
    {% gds_header homepageUrl="/" serviceName="GOV.UK Frontend Django example project" serviceUrl="/" containerClasses="govuk-width-container" %}
        {% gds_header_nav_item href="/" text="Components" %}
        {% gds_header_nav_item href="/" text="User list" %}
    {% endgds_header %}
{% endblock header %}
```

## 404 template

See: [GDS page not found pages](https://design-system.service.gov.uk/patterns/page-not-found-pages/)

```django
{% load govuk_frontend_django %}

{% block content %}
    <div class="govuk-grid-row">
        <div class="govuk-grid-column-two-thirds">
            <h1 class="govuk-heading-l">Page not found</h1>
            <p class="govuk-body">If you typed the web address, check it is correct.</p>
            <p class="govuk-body">If you pasted the web address, check you copied the entire address.</p>
            <p class="govuk-body">If the web address is correct or you selected a link or button, <a href="#" class="govuk-link">contact the Tax Credits Helpline</a> if you need to speak to someone about your tax credits.</p>
        </div>
    </div>
{% endblock content %}
```

## 500 template

See: [GDS service unavailable pages](https://design-system.service.gov.uk/patterns/service-unavailable-pages/)

```django
{% load govuk_frontend_django %}

{% block content %}
    <div class="govuk-grid-row">
        <div class="govuk-grid-column-two-thirds">
            <h1 class="govuk-heading-l">Sorry, there is a problem with the service</h1>
            <p class="govuk-body">Try again later.</p>
        </div>
    </div>
{% endblock content %}

```

## Confirmation page template

See: [GDS confirmation pages](https://design-system.service.gov.uk/patterns/confirmation-pages/)

```django
{% load govuk_frontend_django %}

{% block content %}
    <div class="govuk-grid-row">
        <div class="govuk-grid-column-two-thirds">
            {% set panel_html %}Your reference number<br><strong>ABC1234D</strong>{% endset %}
            {% gds_component "panel" titleText="Application complete" html=panel_html %}

            <p class="govuk-body">We have sent you a confirmation email.</p>

            <h2 class="govuk-heading-m">What happens next</h2>

            <p class="govuk-body">
                We've sent your application to Hackney Electoral Register Office.
            </p>
            <p class="govuk-body">
                They will contact you either to confirm your registration, or to ask for more information.
            </p>

            <p class="govuk-body">
                <a href="#" class="govuk-link">What did you think of this service?</a> (takes 30 seconds)
            </p>
        </div>
    </div>
{% endblock content %}
```
