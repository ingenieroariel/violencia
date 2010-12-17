# -*- coding: utf-8 -*-
from actores_armados.models import *
from django.contrib.gis import admin

class AccionesActorArmadoInline(admin.StackedInline):
    model = AccionActorArmado
    extra = 1

class ActorArmadoAdmin(admin.ModelAdmin):
#    list_display = ( 'nombre', 'id', 'area_total', 'capital', 'ingresos', 'gastos','cantidad_municipios_pacifico',)
#    search_fields = ['nombre','capital']
#    list_filter = ('fecha_creacion',)
    inlines = [AccionesActorArmadoInline]
    fieldsets = (
        ("Ubicación", {
              'fields':
                 (
                 'municipios',
                 'territorios',
                 'referencia_cartografica',
                 'area'
                 )
          }),
          (None, {
              'fields': (
                'fuerza_publica',
                )
          }),
          
      )


admin.site.register(ActorArmado,ActorArmadoAdmin)
