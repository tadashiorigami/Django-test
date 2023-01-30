from test_site.settings.common import *
from django.core.management.utils import get_random_secret_key
import os
import sys
import dj_database_url

DEBUG = False

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

DEBUG = os.getenv("DEBUG", "False") == "True"

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")