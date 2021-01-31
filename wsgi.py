"""
WSGI config for typeidea1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('TYPEIDEA_PROFILE', 'develop.%s' % profile)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea1.settings')

application = get_wsgi_application()
