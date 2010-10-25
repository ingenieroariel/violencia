from django.contrib.gis import admin

from django.db.models import get_models, get_app
admin.site.register(get_models(get_app('proyectos'))

