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

If there are new Jinja templates available, update `govuk_frontend_jinja` and run the `generate-components` command again.

```bash
poetry update govuk_frontend_jinja
make generate-components
```
