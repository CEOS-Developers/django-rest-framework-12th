import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "postdb",
        "USER": "AlphaTechnic",
        "PASSWORD": "nea05200",
        "HOST": "localhost",
        "PORT": "3306"
    }
}