"""
WSGI config for ScopeDatabase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('C:/Users/Seth/PycharmProjects/ScopeDatabase/PipingScopeDatabase/projsettings/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PipingScopingDatabase.projsettings.dev_settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
