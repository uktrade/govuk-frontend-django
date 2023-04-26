---
title: GOV.UK Frontend
---

# GOV.UK Frontend

This project uses the [GOV.UK Frontend Jinja Macros](https://github.com/LandRegistry/govuk-frontend-jinja) package for the component templates. This means that we can generate Django objects that are renderable with up to date GDS markup.

## Adding/updating components

To clear the generated components run the following command:

```bash
make clear-generated-components
```

To generate components run the following command:

```bash
make generate-components
```

Note that the generate-componets command will skip over any components that already exist.

If there are new Jinja templates available, run the following command to update the dependencies and generate the components:

```bash
make upgrade-components GOVUK_FRONTEND_VERSION=v4.6.0 GOVUK_FRONTEND_JINJA_VERSION=2.6.0
```

This command will upgrade the GOV.UK Frontend Jinja Macros package to the specified version and then generate the components using the component yaml files from the GOV.UK Frontend using the specified version.
