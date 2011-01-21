# -*- coding: utf-8 -*-
from naturales.models import *
from django.contrib.gis import admin

class ParqueNacionalMAVDTInline(admin.StackedInline):
    model = ParqueNacionalMAVDT
    extra = 1

class AfectacionAreaProtegidaInline(admin.StackedInline):
    model = AfectacionAreaProtegida
    extra = 1

class AreaNaturalProtegidaAdmin(admin.ModelAdmin):

    inlines = [ParqueNacionalMAVDTInline, AfectacionAreaProtegidaInline]
    fieldsets = (
        (None, {
            'fields':(
                'area_natural',
                'nombre'
            )
        }),
        (None, {
              'fields':
                 (
                 'traslape',
                 'descripcion_conflictos_uso'
                 )
          }),
      )


class DesastreNaturalAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
              'fields': (
                'tipo',
                'descripcion_desastre',
                'fecha',
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
admin.site.register(AreaNaturalProtegida,AreaNaturalProtegidaAdmin)
