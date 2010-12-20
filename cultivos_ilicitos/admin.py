# -*- coding: utf-8 -*-
from megaproyectos.models import Afectacion
from cultivos_ilicitos.models import *
from django.contrib.gis import admin
from django.contrib.contenttypes import generic

class AfectacionInline(generic.GenericStackedInline):
    model = Afectacion
    extra = 1

class ErradicacionInline(admin.StackedInline):
    model = ErradicacionCultivosIlicitos
    extra = 1

class CultivosIlicitosAdmin(admin.ModelAdmin):
#    list_display = ( 'nombre', 'id', 'area_total', 'capital', 'ingresos', 'gastos','cantidad_municipios_pacifico',)
#    search_fields = ['nombre','capital']
#    list_filter = ('fecha_creacion',)
    inlines = [AfectacionInline, ErradicacionInline]
    fieldsets = (
        ("Ubicacion", {
              'fields':
                 (
                 'municipios',
                 'territorios',
                 'referencia_cartografica',
                 )
          }),
          (None, {
              'fields': 
                 (
                 'area',
                 'promotores',
                 )
          }),
          ('Participacion', {
              'fields': (
                ('participacion_comunidad', 'participacion_comunidad_tipo'),
                ('participacion_otros', 'participacion_otros_tipo'),
                  'fuente',
                )
          }),
      )


admin.site.register(CultivosIlicitos,CultivosIlicitosAdmin)
