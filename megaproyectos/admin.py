# -*- coding: utf-8 -*-
from django.contrib import admin
from megaproyectos.models import *
from territorios.models import Ubicacion
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
    
class UbicacionInline(generic.GenericStackedInline):
    model = Ubicacion
    extra = 1


class PoliticaMegaproyectoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
              'fields':
                 (
                 'nombre_documento',
                 'documento',
                 'inicio_vigencia',
                 'fin_vigencia',
                 'sector',
                 'resumen_del_contenido',
                 )
          }),
          ('Ubicacion', {
              'fields':
                 (
                 'nacional',
                 'departamento',
                 )
          }),
    )
class DesarrolloLegislativoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
              'fields':
                 (
                 'nombre_documento',
                 'documento',
                 'fecha',
                 'tipo',
                 'sector',
                 )
          }),
          ('Ubicacion', {
              'fields':
                 (
                 'nacional',
                 'departamento',
                 )
          }),
    )


""" OBRAS DE INFRAESTRUCTURA """

class ProyectoObraInfraestructuraAdmin(admin.ModelAdmin):
    inlines = [EstadoEjecucionInfraestructuraInline, RequisitoLegalInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'tipo',
                 'nombre',
                 )
          }),
        ('Información General', {
            'fields':(
                'area_proyecto',
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
        }),
        ("Empresa propietaria", {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 'empresa_sede_principal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'monto_inversion',
                 'instituciones_financiadoras',
                 )
          }),
        ("Financiacion del proyecto", {
              'fields':
                 (
                 'financia_empresa_nombre',
                 'financia_empresa_representante_legal',
                 'financia_empresa_sede_principal',
                 ('financia_empresa_accionistas_nacionales','financia_empresa_accionistas_extranjeros'),
                 ('financia_empresa_en_colombia','financia_empresa_en_extranjero'),
                 ('financia_empresa_otras_actividades','financia_empresa_otras_actividades_descripcion'),
                 'financia_monto_inversion',
                 )
          }),
      )

""" INDUSTRIAS DE HIDROCARBUROS """

class ProyectoInsdustriaHidrocarburosAdmin(admin.ModelAdmin):
    inlines = [EstadoEjecucionHidrocarburosInline, RequisitoLegalInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'tipo',
                 'nombre',
                 )
          }),
        ('Información General', {
            'fields':(
                'area_proyecto',
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
        }),
        ("Empresa propietaria", {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 'empresa_sede_principal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'monto_inversion',
                 'instituciones_financiadoras',
                 )
          }),
          ("Financiacion del proyecto", {
              'fields':
                 (
                 'financia_empresa_nombre',
                 'financia_empresa_representante_legal',
                 'financia_empresa_sede_principal',
                 ('financia_empresa_accionistas_nacionales','financia_empresa_accionistas_extranjeros'),
                 ('financia_empresa_en_colombia','financia_empresa_en_extranjero'),
                 ('financia_empresa_otras_actividades','financia_empresa_otras_actividades_descripcion'),
                 'financia_monto_inversion',
                 )
          }),
      )

""" MINERIA """

class ProyectoMineriaAdmin(admin.ModelAdmin):
    inlines = [EstadoEjecucionMineriaInline, TituloMineroInline, ExploracionInline, RequisitoLegalInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'tipo',
                 'nombre',
                 )
          }),
        ('Información General', {
            'fields':(
                'area_proyecto',
                ('fecha_iniciacion','fecha_finalizacion'),
            )
        }),
        ("Empresa propietaria", {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 'empresa_sede_principal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'monto_inversion',
                 'instituciones_financiadoras',
                 )
          }),
          ("Financiacion del proyecto", {
              'fields':
                 (
                 'financia_empresa_nombre',
                 'financia_empresa_representante_legal',
                 'financia_empresa_sede_principal',
                 ('financia_empresa_accionistas_nacionales','financia_empresa_accionistas_extranjeros'),
                 ('financia_empresa_en_colombia','financia_empresa_en_extranjero'),
                 ('financia_empresa_otras_actividades','financia_empresa_otras_actividades_descripcion'),
                 'financia_monto_inversion',
                 )
          }),
      )


""" AGROINDUSTRIA """
class ProyectoAgroindustriaAdmin(admin.ModelAdmin):
    inlines = [EstadoEjecucionAgroindustriaInline, RequisitoLegalAgroindustriaInline, VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'tipo',
                 'nombre',
                 )
          }),
        ('Información General', {
            'fields':(
                'area_proyecto',
                ('fecha_iniciacion','fecha_finalizacion'),
            )
        }),
        ("Empresa propietaria", {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 'empresa_sede_principal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'monto_inversion',
                 'instituciones_financiadoras',
                 )
          }),
          ("Financiacion del proyecto", {
              'fields':
                 (
                 'financia_empresa_nombre',
                 'financia_empresa_representante_legal',
                 'financia_empresa_sede_principal',
                 ('financia_empresa_accionistas_nacionales','financia_empresa_accionistas_extranjeros'),
                 ('financia_empresa_en_colombia','financia_empresa_en_extranjero'),
                 ('financia_empresa_otras_actividades','financia_empresa_otras_actividades_descripcion'),
                 'financia_monto_inversion',
                 )
          }),
      )


""" APROVECHAMIENTO FORESTAL PRESISTENTE """
class AFPEspecieInline(generic.GenericStackedInline):
    model = AFPEspecie
    extra = 1

class AFPObligacionInline(generic.GenericStackedInline):
    model = AFPObligacion
    extra = 1

class AFPInformeSemestralInline(generic.GenericStackedInline):
    model = AFPInformeSemestral
    extra = 1

class AFPESalvoconductoInline(generic.GenericStackedInline):
    model = AFPESalvoconducto
    extra = 1

class ProyectoAFPAdmin(admin.ModelAdmin):
    inlines = [AFPEspecieInline, AFPObligacionInline, AFPInformeSemestralInline, AFPESalvoconductoInline, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'tipo',
                 ('tipo_permiso', 'numero_permiso'),
                 'fecha', 
                 ('vigencia_desde', 'vigencia_hasta'),
                 'extension',
                 'descripcion_derechos_y_tasas',
                 'sistema_de_aprovechamiento'
                 )
          }),
        ('Financiacion', {
             'fields':
                (
                  'monto_de_inversion',
                  'instituciones_financiadoras',
                )
          }),
        ('Usuario', {
             'fields':
                (
                  'nombre_usuario',
                  'tipo_usuario',
                  'aval_descripcion',
                  'representante_legal',
                  'accionistas_nacionales',
                  'accionistas_extranjeros',
                  ( 'opera_en_colombia', 'opera_en_extrajero'),
                  ('otras_actividades', 'otras_actividades_cuales'),
                )
          }),


        )


""" EXTRACCION PESQUERA """

class ProyectoPescaContinentalAdmin(admin.ModelAdmin):
    inlines = [VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'tipo',
                 'subtipo',
                 )
          }),
          ('Información General', {
            'fields':(
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
          }),
          ('Permiso', {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'duracion',
                 'area_de_operaciones',
                 'cuota',
                 'especies',
                 'sistema_tecnologico',
                 'causales',
                 'valorizaciones',
                 )
          }),
          (None, {
             'fields': (
                'plan_investigacion',
                'vigencia',
                'resultado'
                )
           }),
        )

class ProyectoPescaMarinaAdmin(admin.ModelAdmin):
    inlines = [VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'tipo',
                 'subtipo',
                 )
          }),
          ('Información General', {
            'fields':(
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
          }),
          ('Permiso', {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'duracion',
                 'area_de_operaciones',
                 'cuota',
                 'especies',
                 'sistema_tecnologico',
                 'causales',
                 'valorizaciones',
                 )
          }),
          (None, {
             'fields': (
                'plan_investigacion',
                'vigencia',
                'resultado'
                )
           }),
        )

class ProyectoProcesamientoPescaAdmin(admin.ModelAdmin):
    inlines = [VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'nombre',
                 )
          }),
          ('Información General', {
            'fields':(
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
          }),
          ('Permiso', {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'duracion',
                 'area_de_operaciones',
                 'cuota',
                 'especies',
                 'sistema_tecnologico',
                 'causales',
                 'valorizaciones',
                 )
          }),
          (None, {
             'fields': (
                'plan_investigacion',
                'vigencia',
                'resultado'
                )
           }),
        )

class ProyectoComercializacionPescaAdmin(admin.ModelAdmin):
    inlines = [VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'nombre',
                 )
          }),
          ('Información General', {
            'fields':(
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
          }),
          ('Permiso', {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'duracion',
                 'area_de_operaciones',
                 'cuota',
                 'especies',
                 'sistema_tecnologico',
                 'causales',
                 'valorizaciones',
                 )
          }),
          (None, {
             'fields': (
                'plan_investigacion',
                'vigencia',
                'resultado'
                )
           }),
        )

class ProyectoPescaIntegradaAdmin(admin.ModelAdmin):
    inlines = [VinculacionPoblacionAdmin, ImplementacionSeguimientoInline, UbicacionInline]
    fieldsets = (
        (None, {
              'fields':
                 (
                 'nombre',
                 )
          }),
          ('Información General', {
            'fields':(
                ('area_terrestre','area_maritima'),
                ('fecha_iniciacion','fecha_finalizacion'),
            )
          }),
          ('Permiso', {
              'fields':
                 (
                 'empresa_nombre',
                 'empresa_representante_legal',
                 ('empresa_accionistas_nacionales','empresa_accionistas_extranjeros'),
                 ('empresa_en_colombia','empresa_en_extranjero'),
                 ('empresa_otras_actividades','empresa_otras_actividades_descripcion'),
                 'duracion',
                 'area_de_operaciones',
                 'cuota',
                 'especies',
                 'sistema_tecnologico',
                 'causales',
                 'valorizaciones',
                 )
          }),
          (None, {
             'fields': (
                'plan_investigacion',
                'vigencia',
                'resultado'
                )
           }),
        )



admin.site.register(InstitucionFinanciadora)

admin.site.register(PoliticaMegaproyecto, PoliticaMegaproyectoAdmin)
admin.site.register(DesarrolloLegislativo, DesarrolloLegislativoAdmin)
admin.site.register(Sector)

admin.site.register(ProyectoObraInfraestructura, ProyectoObraInfraestructuraAdmin)
admin.site.register(ProyectoInsdustriaHidrocarburos, ProyectoInsdustriaHidrocarburosAdmin)
admin.site.register(ProyectoMineria, ProyectoMineriaAdmin)
admin.site.register(ProyectoAgroindustria, ProyectoAgroindustriaAdmin)
admin.site.register(ProyectoAFP, ProyectoAFPAdmin)
admin.site.register(ProyectoPescaContinental, ProyectoPescaContinentalAdmin)
admin.site.register(ProyectoPescaMarina, ProyectoPescaMarinaAdmin)
admin.site.register(ProyectoProcesamientoPesca, ProyectoProcesamientoPescaAdmin)
admin.site.register(ProyectoComercializacionPesca, ProyectoComercializacionPescaAdmin)
admin.site.register(ProyectoPescaIntegrada, ProyectoPescaIntegradaAdmin)
