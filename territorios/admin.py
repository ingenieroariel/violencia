# -*- coding: utf-8 -*-
from territorios.models import *
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from django import forms
from django.contrib.contenttypes import generic
from desc.models import IndicadorBasico
from conflictos.models import Conflicto
from actores_armados.models import ActorArmado

GMAP = GoogleMap()

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'
    default_lon = -8228293
    default_lat = 508764
    default_zoom = 5


class ActorArmadoInline(admin.StackedInline):
    model = ActorArmado
    extra = 1

class EstadisticaMunicipioInline(admin.StackedInline):
    model = EstadisticaMunicipio

class EstadisticaDepartamentoInline(admin.StackedInline):
    model = EstadisticaDepartamento

class TitulosIndividualesInlines(admin.StackedInline):
    model = TitulosIndividuales
    extra = 2

class IndicadorBasicoInline(generic.GenericStackedInline):
    model = IndicadorBasico
    extra = 1

class DepartamentoAdmin(GoogleAdmin):
    list_display = ( 'nombre', 'id', 'area_total', 'capital', 'ingresos', 'gastos','cantidad_municipios_pacifico',)
    search_fields = ['nombre','capital']
    list_filter = ('ano_creacion',)
    inlines = [EstadisticaDepartamentoInline, IndicadorBasicoInline]
    fieldsets = (
          (None, {
              'fields': 
                 (
                 'nombre', 
                 ('area_total', 'area_rural', 'area_urbana'), 
                'capital',
                 ('cantidad_municipios_total', 'cantidad_municipios_pacifico'),
                  'ano_creacion',
                  'informacion_adicional',
                 )
          }),
          ('Presupuesto', {
              'fields': (('ingresos', 'gastos'),
                          'fuente_presupuesto',
                          )
          }),
      )

class MunicipioAdmin(GoogleAdmin):
    list_display = ('nombre', 'id', 'departamento', 'area_total',  'ingresos', 'gastos','certificado')
    list_filter = ('departamento','ano_creacion', 'certificado')
    inlines = [EstadisticaMunicipioInline, TitulosIndividualesInlines, IndicadorBasicoInline, ActorArmadoInline]
    fieldsets = (
          (None, {
              'fields': 
                 (
                 ('nombre', 'departamento'),
                 ('area_total', 'area_rural', 'area_cabecera'), 
                 ('ano_creacion', 'certificado'),
                  'informacion_adicional',
                 )
                
          }),
          ('Presupuesto', {
              'fields': (('ingresos', 'gastos'),
                          'fuente_presupuesto',
                          )
          }),
      )

class PoblacionComunidadIndigenaAdmin(admin.StackedInline):    
    model = PoblacionComunidadIndigena
    extra = 1

class PoblacionComunidadNegraAdmin(admin.StackedInline):    
    model = PoblacionComunidadNegra
    extra = 1

class PoblacionTerritorioColectivoAdmin(admin.StackedInline):
    model = PoblacionTerritorioColectivo
    extra = 1

class SituacionJuridicaAdmin(admin.StackedInline):
    model = SituacionJuridica
    extra=1

class SituacionJuridicaSolicitudTitulacionAdmin(admin.StackedInline):
    model = SolicitudTitulacion
    extra = 1

class SituacionJuridicaAmpliacion(admin.StackedInline):
    model = Ampliacion
    extra = 1

class SituacionJuridicaSaneamiento(admin.StackedInline):
    model = Saneamiento
    extra = 1

class ComunidadInlineAdmin(admin.TabularInline):
    model = Comunidad

class ComunidadAdmin(GoogleAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_disolucion')

#TODO: eliminar comentario cuando se verifiquen dependencias
#class ComunidadIndigenaInlineAdmin(admin.TabularInline):
#    model = ComunidadIndigena
#    inlines = [PoblacionComunidadNegraAdmin, IndicadorBasicoInline]
#
#class ComunidadNegraInlineAdmin(admin.TabularInline):
#    model = ComunidadNegra
#    inlines = [PoblacionComunidadNegraAdmin, IndicadorBasicoInline]

class ConflictoInline(generic.GenericStackedInline):
    model = Conflicto
    extra = 1

class TerritorioComunidadAdmin(GoogleAdmin):
    list_display = ('nombre', 'titulado', 'resolucion_constitucion', 'numero_comunidades', 'municipios_del_territorio')
    exclude = ('geom','informacion_adicional')
    fieldsets = (
          (None, {
              'fields': 
                 (
                 'nombre', 
                 ( 'municipios'),
                 ('titulado', 'resolucion_constitucion',), 
                 ('area', 'limites'))
          }),
      )

class TerritorioComunidadIndigenaAdmin(TerritorioComunidadAdmin):
    inlines = [PoblacionTerritorioColectivoAdmin, SituacionJuridicaSolicitudTitulacionAdmin, SituacionJuridicaAmpliacion, SituacionJuridicaSaneamiento, ConflictoInline]

class TerritorioComunidadNegraAdmin(TerritorioComunidadAdmin):
    inlines = [PoblacionTerritorioColectivoAdmin, SituacionJuridicaSolicitudTitulacionAdmin, ConflictoInline]


class PuebloAdmin(GoogleAdmin):
    list_display = ('nombre', 'descripcion')

class ComunidadNegraInline(admin.StackedInline):
    model = PoblacionComunidadNegra
    extra = 1

class ComunidadNegraAdmin(GoogleAdmin):
    inlines = [ComunidadNegraInline]
    fieldsets = (
          (None, {
              'fields':
                 (
                 'nombre',
                 ('fecha_creacion', 'fecha_creacion_ano',),
                 ('fecha_disolucion', 'fecha_disolucion_ano',),
                 'territorio')
          }),
      )

class ComunidadIndigenaInline(admin.StackedInline):
    model = PoblacionComunidadIndigena
    extra = 1

class ComunidadIndigenaAdmin(GoogleAdmin):
    list_display = ('nombre', 'pueblo', 'territorio')
    inlines = [ComunidadIndigenaInline]
    list_filter = ('territorio',)
    fieldsets = (
          (None, {
              'fields':
                 (
                 'nombre',
                 ('fecha_creacion', 'fecha_creacion_ano',),
                 ('fecha_disolucion', 'fecha_disolucion_ano',),
                 'territorio')
          }),
      )

admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(TerritorioComunidadIndigena, TerritorioComunidadIndigenaAdmin)
admin.site.register(TerritorioComunidadNegra, TerritorioComunidadNegraAdmin)
admin.site.register([Pueblo, ])
admin.site.register(ComunidadNegra, ComunidadNegraAdmin)
admin.site.register(ComunidadIndigena, ComunidadIndigenaAdmin)
