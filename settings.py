"""Django settings.

NB: This is a minimal settings module and is only for migration
creation, do not try to serve a site using this configuration.
"""
from pathlib import Path
from typing import List

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY: str = "XXX"
DEBUG: bool = True
ALLOWED_HOSTS: List[str] = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "govuk_frontend_django",
]

MIDDLEWARE: List[str] = []
TEMPLATES: List[str] = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
