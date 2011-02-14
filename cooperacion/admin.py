# -*- coding: utf-8 -*-
from cooperacion.models import Cooperacion
from megaproyectos.models import Afectacion
from cooperacion.models import *
from django.contrib.gis import admin
from django.contrib.contenttypes import generic

class AfectacionInline(generic.GenericStackedInline):
    model = Afectacion
    extra = 1

class CooperacionInline(admin.StackedInline):
    model = Cooperacion
    extra = 1

class CooperacionAdmin(admin.ModelAdmin):
    inlines = [AfectacionInline]
    fieldsets = (
          (None, {
              'fields': 
                 (
                 'departamento',
                 )
          }),
          (None, {
              'fields':
                 (
                 'cooperacion',
                 'tipo_proyecto',
                 )
          }),
          ('Participacion', {
              'fields': (
                'periodo_convenio',
                'monto_inversion',
                'cobertura',
                'operadores',
                'fuente',
                )
          }),
      )


admin.site.register(Cooperacion,CooperacionAdmin)
