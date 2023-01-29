from test_site.settings.common import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'tadashimori.pythonanywhere.com'
]