# -*- coding: utf-8 -*-
from django.contrib import admin
from megaproyectos.models import *
from estados_ejecucion.models import *
from django.contrib.contenttypes import generic

class OpcionesEstadoEjecucionInline(generic.GenericStackedInline):
    model = OpcionesEstadoEjecucion
    extra = 1

class AfectacionesInline(generic.GenericStackedInline):
    model = Afectacion
    extra = 1

class AccionesInline(generic.GenericStackedInline):
    model = Accion
    extra = 1

class SubcontratistaInline(generic.GenericStackedInline):
    model = Subcontratista
    extra = 1
class ConcesionInfraestructuraInline(generic.GenericStackedInline):
    model = ConcesionInfraestructura
    extra = 1

class ConcesionHidrocarburosInline(generic.GenericStackedInline):
    model = ConcesionHidrocarburo
    extra = 1
class EstadoEjecucionExplotacionInline(generic.GenericStackedInline):
    model = EstadoEjecucionExplotacion
    extra = 1

class ConcesionMineriaInline(generic.GenericStackedInline):
    model = ConcesionMineria
    extra = 1

class MedidaInline(generic.GenericStackedInline):
    model = Medida
    extra = 1
class ResultadoInline(generic.GenericStackedInline):
    model = Resultado
    extra = 1
class DestinoInline(generic.GenericStackedInline):
    model = Destino
    extra = 1

class EstadoEjecucionInfraestructuraAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'fase_tipo', 'fecha_iniciacion', 'fecha_terminacion')
    inlines = [SubcontratistaInline, OpcionesEstadoEjecucionInline, AfectacionesInline, AccionesInline, ConcesionInfraestructuraInline]
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


class EstadoEjecucionHidrocarburoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'fase_tipo', 'fecha_iniciacion', 'fecha_terminacion')
    inlines = [ConcesionHidrocarburosInline, EstadoEjecucionExplotacionInline, SubcontratistaInline]
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
                 )
          }),
    )

class EstadoEjecucionMineriaAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'fase_tipo', 'fecha_iniciacion', 'fecha_terminacion')
    inlines = [ConcesionMineriaInline, EstadoEjecucionExplotacionInline, SubcontratistaInline]
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
                 )
          }),
    )

class EstadoEjecucionAgroindustriaAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'fase_tipo', 'fecha_iniciacion', 'fecha_terminacion')
    inlines = [MedidaInline, ResultadoInline, DestinoInline]
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
                 )
          }),
    )

admin.site.register(EstadoEjecucionInfraestructura, EstadoEjecucionInfraestructuraAdmin)
admin.site.register(EstadoEjecucionHidrocarburo, EstadoEjecucionHidrocarburoAdmin)
admin.site.register(EstadoEjecucionMineria, EstadoEjecucionMineriaAdmin)
admin.site.register(EstadoEjecucionAgroindustria, EstadoEjecucionAgroindustriaAdmin)
#admin.site.register(ImpactoAmbiental)
#admin.site.register(ImpactoCultural)
#admin.site.register(ImpactoEconomico)
#admin.site.register(ImpactoSocial)
#admin.site.register(ImpactoOrganizaciones)
