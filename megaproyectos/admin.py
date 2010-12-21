# -*- coding: utf-8 -*-
from django.contrib import admin
from megaproyectos.models import *
from django.contrib.contenttypes import generic

class InstitucionFinanciadoraInline(generic.GenericStackedInline):
    model = InstitucionFinanciadora
    extra = 1

class EstadoEjecucionInline(generic.GenericStackedInline):
    model = EstadoEjecucion
    extra = 1

class RequisitoLegalInline(generic.GenericStackedInline):
    model = RequisitoLegal
    extra = 1

class VinculacionPoblacionAdmin(generic.GenericStackedInline):
    model = VinculacionPoblacion
    extra = 1

class ImplementacionSeguimientoInline(generic.GenericStackedInline):
    model = ImplementacionSeguimiento
    extra = 1
    
class ReferenciaCartograficaInline(generic.GenericStackedInline):
    model = ReferenciaCartografica
    extra = 1

class ObraInfraestructuraAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Ubicación', {
            'fields':(
                'municipios',
                'nombre_documento',
                'documento',
                'vigencia',
            )
        }),
        ("Obras de infraestructura", {
              'fields':
                 (
                 'tipo',
                 )
          }),
          (None, {
              'fields':
                 (
                 'fuente',
                 )
          }),
      )

class ProyectoObraInfraestructuraAdmin(admin.ModelAdmin):
    inlines = [InstitucionFinanciadoraInline, EstadoEjecucionInline, RequisitoLegalInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, ReferenciaCartograficaInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'nombre',
                 )
          }),
        ('Información General', {
            'fields':(
                'municipios',
                'territorios',
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
        }),
        ("Empresa propietaria", {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'monto_inversion',
                 )
          }),
      )

admin.site.register(ObraInfraestructura, ObraInfraestructuraAdmin)
admin.site.register(ProyectoObraInfraestructura, ProyectoObraInfraestructuraAdmin)
