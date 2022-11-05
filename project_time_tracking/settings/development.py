import os

from .common import *

ALLOWED_HOSTS = ["*"]
DEBUG = True

SECRET_KEY = "k*m4vk6^1_#h3ux3v^j_6&kn*31kazepkj581yr(!6(33hj-s"


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    },

}
