# -*- coding: utf-8 -*-
from django.contrib import admin
from megaproyectos.models import *
from estados_ejecucion.models import *
from django.contrib.contenttypes import generic

#class EstadoEjecucionCesionInline(admin.StackedInline):
#    model = EstadoEjecucionInfraestructura
#    extra = 1

class EstadoEjecucionCesionInline(generic.GenericStackedInline):
    model = EstadoEjecucionCesion
    extra = 1
class EstadoEjecucionSuspensionInline(generic.GenericStackedInline):
    model = EstadoEjecucionSuspension
    extra = 1
class EstadoEjecucionRevocatoriaInline(generic.GenericStackedInline):
    model = EstadoEjecucionRevocatoria
    extra = 1
class SubcontratistaInline(generic.GenericStackedInline):
    model = Subcontratista
    extra = 1
class ConcesionInline(generic.GenericStackedInline):
    model = Concesion
    extra = 1



class EstadoEjecucionInfraestructuraAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'fase_tipo', 'fecha_iniciacion', 'fecha_terminacion')
    inlines = [SubcontratistaInline, ConcesionInline, EstadoEjecucionCesionInline, EstadoEjecucionSuspensionInline, EstadoEjecucionRevocatoriaInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'proyecto',
                 'fase_tipo'
                 )
          }),
          (None, {
              'fields':
                 (
                 ('fecha_iniciacion','fecha_terminacion'),
                 'subcontratista',
                 )
          }),
    )

admin.site.register(EstadoEjecucionInfraestructura, EstadoEjecucionInfraestructuraAdmin)
