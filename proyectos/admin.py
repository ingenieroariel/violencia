from django.db.models import get_models, get_app
from django.contrib import admin

ms = get_models(get_app('proyectos'))
admin.site.register(ms)