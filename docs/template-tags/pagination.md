# Pagination

See: [https://design-system.service.gov.uk/components/pagination/](https://design-system.service.gov.uk/components/pagination/)

## Usage

To use the GDS Pagination, you can use the `gds_pagination` template tag. This tag accepts a `page_obj` argument which should be a Django Paginated Page.

If you are using a Django `ListView`, the `page_obj` argument will be available in the template context.

### Example:

#### views.py
```python
from django.views.generic import ListView
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListingView(ListView):
    template_name = "template.html"
    model = User
    paginate_by = 25
```

#### template.html
```django
{% load govuk_frontend_django %}
{% gds_pagination page_obj %}
```