import os
from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ba_dev7",
        "USER": "postgres",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
