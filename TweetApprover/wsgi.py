# coding = utf-8
"""
WSGI config for TweetApprover project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TweetApprover.settings")
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'TweetApprover.settings'
application = get_wsgi_application()
