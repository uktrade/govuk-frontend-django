serve-docs:
	poetry run mkdocs serve -a localhost:8001

# GDS components

GOVUK_FRONTEND_VERSION = "v4.5.0"
GOVUK_FRONTEND_JINJA_VERSION = "2.5.0"

generate-components:
	poetry run python scripts/generate_components.py $(GOVUK_FRONTEND_VERSION)
	poetry run isort --remove-redundant-aliase govuk_frontend_django/components
	poetry run autoflake --in-place --remove-unused-variables -r govuk_frontend_django/components
	poetry run black govuk_frontend_django/components

clear-generated-components:
	find govuk_frontend_django/components ! -name '__init__.py' ! -name 'base.py' -type f -exec rm -rf {} +

upgrade-components:
	echo "Upgrading components with"
	echo "GOV.UK Frontend: $(GOVUK_FRONTEND_VERSION)"
	echo "GOV.UK Frontend Jinja: $(GOVUK_FRONTEND_JINJA_VERSION)"
	poetry remove govuk_frontend_jinja
	poetry add govuk_frontend_jinja==$(GOVUK_FRONTEND_JINJA_VERSION)
	make clear-generated-components
	make generate-components GOVUK_FRONTEND_VERSION=$(GOVUK_FRONTEND_VERSION)

# Example project

init-example-project:
	poetry run python example_project/manage.py migrate
	poetry run python example_project/manage.py loaddata test_users.json

run-example-project:
	poetry run python example_project/manage.py runserver

# PyPI

build-package:
	poetry build

push-pypi-test:
	poetry publish -r test-pypi

push-pypi:
	poetry publish
