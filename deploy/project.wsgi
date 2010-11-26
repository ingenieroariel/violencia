import os, sys
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

os.environ['DJANGO_SETTINGS_MODULE'] = 'violencia.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
