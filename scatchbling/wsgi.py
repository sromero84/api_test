"""
WSGI config for element project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import site
from os.path import exists

# Add the site-packages of the chosen virtualenv to work with
VENV_PACKAGES = '/var/www/scatchbling/lib/python2.7/site-packages'
if exists(VENV_PACKAGES):
    site.addsitedir(VENV_PACKAGES)

# Add the app's directory to the PYTHONPATH
PROJECT_PATH = '/var/www/scatchbling'
APP_PATH = '/var/www/scatchbling/scatchbling'
if exists(PROJECT_PATH):
    sys.path.append(PROJECT_PATH)
if exists(APP_PATH):
    sys.path.append(APP_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scatchbling.settings")

# Activate your virtual env
ACTIVATE_PATH = "/var/www/scatchbling_env/bin/activate_this.py"
if exists(ACTIVATE_PATH):
    activate_env=os.path.expanduser(ACTIVATE_PATH)
    execfile(activate_env, dict(__file__=activate_env))
else:
    print 'WARNING: wsgi.py cannot locate file %s' % ACTIVATE_PATH

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
