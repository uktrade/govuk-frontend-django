build-package:
	poetry build

push-pypi-test:
	poetry publish -r test-pypi

push-pypi:
	poetry publish

serve-docs:
	poetry run mkdocs serve -f ./docs/mkdocs.yml -a localhost:8001

generate-components:
	poetry run python scripts/generate_components.py
	poetry run isort --remove-redundant-aliase govuk_frontend_django/components
	poetry run autoflake --in-place --remove-unused-variables -r govuk_frontend_django/components
	poetry run black govuk_frontend_django/components

clear-generated-components:
	find govuk_frontend_django/components ! -name '__init__.py' ! -name 'base.py' -type f -exec rm -rf {} +

init-example-project:
	poetry run python example_project/manage.py migrate
	poetry run python example_project/manage.py loaddata test_users.json

run-example-project:
	poetry run python example_project/manage.py runserver
