import os

from .common import *

DEBUG = True

SECRET_KEY = "fm4vx26^1_jx34iiii^j_6&kn*31kazepkj581yr(!6(33hj-s"

TEST_RUNNER = 'backend_plentific.test_runner.TestRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}