# -*- coding: utf-8 -*-
from desastres_naturales.models import *
from django.contrib.gis import admin

class DesastreNaturalAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
              'fields': (
                'tipo',
                'descripcion_desastre',
                'fecha',
                )
          }),
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
                'poblacion',
                'territorios_afectados',
                'causas_descripcion',
                )
          }),
          ("Afectacion", {
              'fields': (
                'afectacion',
                'descripcion_afectacion',
                )
          }),
          ("Intervención", {
              'fields': (
                'intervencion_fecha',
                'intervencion_clase',
                'intervencion_institucion_organizacion',
                'intervencion_tipo',
                )
          }),
          
      )


admin.site.register(DesastreNatural,DesastreNaturalAdmin)
