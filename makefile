serve-docs:
	poetry run mkdocs serve -a localhost:8001

# GDS components
get-latest-release-tag:
	@gh release list -R $(REPO) | grep "Latest" | awk -F '\t' '{for(i=2; i<=NF; i++) {if($$i~/v?[0-9]+\.[0-9]+\.[0-9]+/) {print $$i; exit}}}'

GOVUK_FRONTEND_VERSION = "v5.7.0"
GOVUK_FRONTEND_JINJA_VERSION = "3.3.0"

generate-components:
	poetry run python scripts/generate_components.py $(GOVUK_FRONTEND_VERSION)
	poetry run isort --remove-redundant-aliase govuk_frontend_django/components
	poetry run autoflake --in-place --remove-unused-variables -r govuk_frontend_django/components
	poetry run black govuk_frontend_django/components

clear-generated-components:
	find govuk_frontend_django/components ! -name '__init__.py' ! -name 'base.py' -type f -exec rm -rf {} +

upgrade-example-project:
	cd example_project && npm install govuk-frontend@$(GOVUK_FRONTEND_VERSION) && npm run build && poetry update

upgrade-components:
	echo "Upgrading components with"
	echo "GOV.UK Frontend: $(GOVUK_FRONTEND_VERSION)"
	echo "GOV.UK Frontend Jinja: $(GOVUK_FRONTEND_JINJA_VERSION)"
	poetry remove govuk_frontend_jinja
	poetry add govuk_frontend_jinja==$(GOVUK_FRONTEND_JINJA_VERSION)
	make clear-generated-components
	make generate-components GOVUK_FRONTEND_VERSION=$(GOVUK_FRONTEND_VERSION)
	make upgrade-example-project GOVUK_FRONTEND_VERSION=$(GOVUK_FRONTEND_VERSION)

# Example project

init-example-project:
	poetry run python example_project/manage.py migrate
	poetry run python example_project/manage.py collectstatic
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

# Formatting/Linting

mypy:
	poetry run mypy govuk_frontend_django

djlint:
	poetry run djlint example_project --reformat

# Testing

tox:
	poetry run tox
