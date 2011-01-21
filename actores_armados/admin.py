# -*- coding: utf-8 -*-
from actores_armados.models import *
from django.contrib.gis import admin

class ActorArmadoAdmin(admin.ModelAdmin):
#    list_display = ( 'nombre', 'id', 'area_total', 'capital', 'ingresos', 'gastos','cantidad_municipios_pacifico',)
#    search_fields = ['nombre','capital']
#    list_filter = ('fecha_creacion',)
    fieldsets = (
          (None, {
              'fields': (
                'municipio',
                'actor',
                'acciones',
                )
          }),
          
      )

admin.site.register(AccionActorArmado)
admin.site.register(ActorArmado,ActorArmadoAdmin)
