SHELL := /bin/bash

manage = poetry run python manage.py

build:
	poetry install --no-root

init:
	$(manage) loaddata example/fixtures/test_users.json

run:
	./scripts/run.sh

shell:
	$(manage) shell

superuser:
	$(manage) createsuperuser
