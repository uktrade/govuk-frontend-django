# GOV.UK Frontend Django

[Documentation Site](https://uktrade.github.io/govuk-frontend-django/) | [GitHub](https://github.com/uktrade/govuk-frontend-django/) | [PyPI](https://pypi.org/project/govuk-frontend-django/)


The `govuk_frontend_django` package contains Django functionality to help when building a GOV.UK website.

The main part of this package is the [template tags](./template-tags/index.md) that it offers for use in your templates. These template tags will reduce the amount of markup that you need to maintain in your project.

This package also contains some helpful [templates](./templates.md) for your project, such as the `govuk_frontend_django/base.html` template which contains the basic structure of a GOV.UK website.

## Getting started

First install the package:
```bash
pip install govuk-frontend-django
```

In your settings file, add the app to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    "govuk_frontend_django",
]
```

Start using the template tags in your templates!
```django
{% load govuk_frontend_django %}

{% gds_component "back-link" href="/" %}
```

[More template tags](./template-tags/index.md)

## Compatibility table

Below is a list of the versions of this package and the versions of the GOV.UK Frontend that they are compatible with.

| Package Version | GOV.UK Frontend Version |
| --------------- | ----------------------- |
| [0.15.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.15.0) - [0.15.1](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.15.1) | [v5.9.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.9.0) |
| [0.14.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.14.0) - [0.14.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.14.0) | [v5.8.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.8.0) |
| [0.13.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.13.0) - [0.13.1](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.13.1) | [v5.7.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.7.0) - [v5.7.1](https://github.com/alphagov/govuk-frontend/releases/tag/v5.7.1) |
| [0.12.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.12.0) - [0.12.1](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.12.1) | [v5.6.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.6.0) |
| [0.11.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.11.0) - [0.11.1](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.11.1) | [v5.5.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.5.0) |
| [0.10.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.10.0) - [0.10.1](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.10.1) | [v5.4.1](https://github.com/alphagov/govuk-frontend/releases/tag/v5.4.1) |
| [0.9.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.9.0) - [0.9.1](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.9.1) | [v5.4.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.4.0) |
| [0.8.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.8.0) - [0.8.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.8.0) | [v5.3.1](https://github.com/alphagov/govuk-frontend/releases/tag/v5.3.1) |
| [0.7.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.7.0) - [0.7.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.7.0) | [v5.3.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.3.0) |
| [0.6.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.6.0) - [0.6.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.6.0) | [v5.2.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.2.0) |
| [0.5.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.5.0) - [0.5.1](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.5.1) | [v5.1.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.1.0) |
| [0.4.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.4.0) - [0.4.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.4.0) | [v4.7.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.7.0) |
| [0.3.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.3.0) - [0.3.9](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.3.9) | [v4.6.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.6.0) |
| [0.2.0](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.2.0) - [0.2.3](https://github.com/uktrade/govuk-frontend-django/releases/tag/0.2.3) | [v4.5.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.5.0) |
