# -*- coding: utf-8 -*-
from django.contrib import admin
from megaproyectos.models import *
from django.contrib.contenttypes import generic

class EstadoEjecucionInfraestructuraInline(admin.StackedInline):
    model = EstadoEjecucionInfraestructura
    extra = 1

class EstadoEjecucionHidrocarburosInline(admin.StackedInline):
    model = EstadoEjecucionHidrocarburos
    extra = 1

class EstadoEjecucionAgroindustriaInline(admin.StackedInline):
    model = EstadoEjecucionAgroindustria
    extra = 1

class EstadoEjecucionMineriaInline(admin.StackedInline):
    model = EstadoEjecucionMineria
    extra = 1

class TituloMineroInline(admin.StackedInline):
    model = TituloMinero
    extra = 1
class ExploracionInline(admin.StackedInline):
    model = Exploracion
    extra = 1


class RequisitoLegalInline(generic.GenericStackedInline):
    model = RequisitoLegal
    extra = 1

class RequisitoLegalAgroindustriaInline(generic.GenericStackedInline):
    model = RequisitoLegalAgroindustria
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


""" OBRAS DE INFRAESTRUCTURA """

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
    inlines = [EstadoEjecucionInfraestructuraInline, RequisitoLegalInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, ReferenciaCartograficaInline]
    list_filter = ('megaproyecto',)
    fieldsets = (
        (None, {
              'fields':
                 (
                 'megaproyecto',
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
                 'instituciones_financiadoras',
                 )
          }),
      )

""" INDUSTRIAS DE HIDROCARBUROS """

class IndustriaHidrocarburosAdmin(admin.ModelAdmin):
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

class ProyectoInsdustriaHidrocarburosAdmin(admin.ModelAdmin):
    inlines = [EstadoEjecucionHidrocarburosInline, RequisitoLegalInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, ReferenciaCartograficaInline]
    list_filter = ('megaproyecto',)
    fieldsets = (
        (None, {
              'fields':
                 (
                 'megaproyecto',
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
                 'instituciones_financiadoras',
                 )
          }),
      )

""" MINERIA """

class MineriaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Ubicación', {
            'fields':(
                'municipios',
                'nombre_documento',
                'documento',
                'vigencia',
            )
        }),
        ("Minerales", {
              'fields':
                 (
                 'tipo',
                 )
          }),
        ("Otros minerales", {
              'fields':
                 (
                 'mineral',
                 )
          }),
          (None, {
              'fields':
                 (
                 'fuente',
                 )
          }),
      )

class ProyectoMineriaAdmin(admin.ModelAdmin):
    inlines = [EstadoEjecucionMineriaInline, TituloMineroInline, ExploracionInline, RequisitoLegalInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, ReferenciaCartograficaInline]
    list_filter = ('megaproyecto',)
    fieldsets = (
        (None, {
              'fields':
                 (
                 'megaproyecto',
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
                 'instituciones_financiadoras',
                 )
          }),
      )


""" AGROINDUSTRIA """

class AgroindustriaAdmin(admin.ModelAdmin):
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
        ("Otros", {
              'fields':
                 (
                 'cual',
                 )
          }),
          (None, {
              'fields':
                 (
                 'fuente',
                 )
          }),
      )

class ProyectoAgroindustriaAdmin(admin.ModelAdmin):
    inlines = [EstadoEjecucionAgroindustriaInline, RequisitoLegalAgroindustriaInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, ReferenciaCartograficaInline]
    list_filter = ('megaproyecto',)
    fieldsets = (
        (None, {
              'fields':
                 (
                 'megaproyecto',
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
                 'instituciones_financiadoras',
                 )
          }),
      )

admin.site.register(InstitucionFinanciadora)

admin.site.register(ObraInfraestructura, ObraInfraestructuraAdmin)
admin.site.register(IndustriaHidrocarburos, IndustriaHidrocarburosAdmin)
admin.site.register(Mineria, MineriaAdmin)
admin.site.register(Agroindustria, AgroindustriaAdmin)

admin.site.register(ProyectoObraInfraestructura, ProyectoObraInfraestructuraAdmin)
admin.site.register(ProyectoInsdustriaHidrocarburos, ProyectoInsdustriaHidrocarburosAdmin)
admin.site.register(ProyectoMineria, ProyectoMineriaAdmin)
admin.site.register(ProyectoAgroindustria, ProyectoAgroindustriaAdmin)
