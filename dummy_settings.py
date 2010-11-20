# Django settings for violencia project.

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
)

try:
    from local_settings import *
except ImportError:
    pass
