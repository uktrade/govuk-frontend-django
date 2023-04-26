---
hide:
  - navigation
---

# Python components

!!! note
    The recommended way to use GOV.UK components is via the [template tags](./template-tags/index.md). The template tags use the python components under the hood.

    Building the Python components directly can be useful if you want to build out a complex component in python.

The components have been built in a way that allows you to simply pass through a dict as the `kwargs` for the component in the same format that we see in teh Nunjucks template examples on the GDS website.

For example, the **Back Link**, which can be found [here](https://design-system.service.gov.uk/components/back-link/), has the folowing Nunjucks example:

```nunjucks
{% from "govuk/components/back-link/macro.njk" import govukBackLink %}

{{ govukBackLink({
  text: "Back",
  href: "#"
}) }}
```

To use the Python version of this component you can do the following:

**views.py**
```python
from govuk_frontend_django.components.back_link import GovUKBackLink

def my_view(request):
    data = {
        "text": "Back",
        "href": "#"
    }
    context = {
        'back_link': GovUKBackLink(**data)
    }
    return render(request, 'my_template.html', context)
```

**my_template.html**
```django
{% load govuk_frontend_django %}

{{ back_link }}
```

This works because the `GovUKBackLink` class inherits from the `GovUKComponent` class which handles the rendering of the component.

## Keyword Arguments
Instead of defining a `data` dict and passing it through as `**data` you can also pass through the keyword arguments directly.

```python
GovUKBackLink(
    text="Back",
    href="#",
)
```
