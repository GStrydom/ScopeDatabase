from .base_settings import *

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'vz6n^#wx^9-yeblexr38@h$!c&-q=^l*j%0ukqn9-4*pmmssye'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pipingscope_prod',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
    }
}