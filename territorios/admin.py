# -*- coding: utf-8 -*-
from territorios.models import *
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from django import forms
from django.contrib.contenttypes import generic
from desc.models import IndicadorBasico
from conflictos.models import Conflicto

GMAP = GoogleMap()

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'
    default_lon = -8228293
    default_lat = 508764
    default_zoom = 5

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
    list_filter = ('fecha_creacion',)
    inlines = [EstadisticaDepartamentoInline, IndicadorBasicoInline]
    fieldsets = (
          (None, {
              'fields': 
                 (
                 'nombre', 
                 ('area_total', 'area_rural', 'area_urbana'), 
                'capital',
                 ('cantidad_municipios_total', 'cantidad_municipios_pacifico'),
                  'fecha_creacion',
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
    list_display = ('nombre', 'id', 'departamento', 'area_total',  'ingresos', 'gastos',)
    list_filter = ('departamento','fecha_creacion')
    inlines = [EstadisticaMunicipioInline, TitulosIndividualesInlines, IndicadorBasicoInline]
    fieldsets = (
          (None, {
              'fields': 
                 (
                 ('nombre', 'departamento'),
                 ('area_total', 'area_rural', 'area_cabecera'), 
                  'fecha_creacion',
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

class ComunidadIndigenaInlineAdmin(admin.TabularInline):
    model = ComunidadIndigena
    inlines = [PoblacionComunidadNegraAdmin, IndicadorBasicoInline]

class ComunidadNegraInlineAdmin(admin.TabularInline):
    model = ComunidadNegra
    inlines = [PoblacionComunidadNegraAdmin, IndicadorBasicoInline]

class ConflictoInline(generic.GenericStackedInline):
    model = Conflicto
    extra = 1

class TerritorioComunidadAdmin(GoogleAdmin):
    list_display = ('id', 'nombre', 'departamento', 'titulado', 'resolucion_constitucion', 'numero_comunidades')
    search_fields = ('nombre', 'departamento')
    list_filter = ('departamento','titulado')
    exclude = ('geom','informacion_adicional')
    fieldsets = (
          (None, {
              'fields': 
                 (
                 'nombre', 
                 ('departamento', 'municipios'),
                 ('titulado', 'resolucion_constitucion',), 
                 ('area', 'limites'))
          }),
      )

   

class TerritorioComunidadIndigenaAdmin(TerritorioComunidadAdmin):
    #inlines = [ComunidadIndigenaInlineAdmin, SituacionJuridicaAdmin, PoblacionTerritorioColectivoAdmin]
    inlines = [ComunidadIndigenaInlineAdmin, PoblacionTerritorioColectivoAdmin, SituacionJuridicaSolicitudTitulacionAdmin, SituacionJuridicaAmpliacion, SituacionJuridicaSaneamiento, ConflictoInline]

class TerritorioComunidadNegraAdmin(TerritorioComunidadAdmin):
    #inlines = [ComunidadNegraInlineAdmin, SituacionJuridicaAdmin, PoblacionTerritorioColectivoAdmin]
    inlines = [ComunidadNegraInlineAdmin, PoblacionTerritorioColectivoAdmin, SituacionJuridicaSolicitudTitulacionAdmin, ConflictoInline]


class PuebloAdmin(GoogleAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(TerritorioComunidadIndigena, TerritorioComunidadIndigenaAdmin)
admin.site.register(TerritorioComunidadNegra, TerritorioComunidadNegraAdmin)
admin.site.register(Comunidad, ComunidadAdmin)
admin.site.register([Pueblo, ])
