"""
WSGI config for database_elegant project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database_elegant.settings")

PROJECT_SRC = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if PROJECT_SRC not in sys.path:
    sys.path.insert(0, PROJECT_SRC)

application = get_wsgi_application()
