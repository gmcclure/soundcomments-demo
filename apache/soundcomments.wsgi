import os
import sys

sys.path.append('/home/gmcclure/.virtualenvs/soundcomments/lib/python2.6/site-packages')
sys.path.append('/var/www/apps/soundcomments')
sys.path.append('/var/www/apps/')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/apps/soundcomments/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'soundcomments.settings-deploy'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
