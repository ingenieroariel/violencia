# -*- coding: utf-8 -*-
from territorios.models import *
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from django import forms

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


class DepartamentoAdmin(GoogleAdmin):
    list_display = ('id', 'nombre', 'area_total', 'capital', 'ingresos', 'gastos','cantidad_municipios_pacifico',)
    search_fields = ['nombre','capital']
    list_filter = ('fecha_creacion',)
    inlines = [EstadisticaDepartamentoInline,]
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
    list_display = ('id', 'nombre', 'departamento', 'area_total',  'ingresos', 'gastos',)
    list_filter = ('departamento','fecha_creacion')
    inlines = [EstadisticaMunicipioInline,]
    fieldsets = (
          (None, {
              'fields': 
                 (
                 'nombre', 
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

class ComunidadInlineAdmin(admin.TabularInline):
    model = Comunidad

class ComunidadAdmin(GoogleAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_disolucion')

class ComunidadIndigenaInlineAdmin(admin.TabularInline):
    model = ComunidadIndigena
    inlines = [PoblacionComunidadNegraAdmin,]

class ComunidadNegraInlineAdmin(admin.TabularInline):
    model = ComunidadNegra
    inlines = [PoblacionComunidadNegraAdmin,]

class TerritorioComunidadAdmin(GoogleAdmin):
    list_display = ('id', 'nombre', 'departamento')
    search_fields = ('nombre', 'departamento')
    list_filter = ('departamento',)
    exclude = ('geom','informacion_adicional')

class TerritorioComunidadIndigenaAdmin(TerritorioComunidadAdmin):
    inlines = [ComunidadIndigenaInlineAdmin, SituacionJuridicaAdmin, PoblacionTerritorioColectivoAdmin]

class TerritorioComunidadNegraAdmin(TerritorioComunidadAdmin):
    inlines = [ComunidadNegraInlineAdmin, SituacionJuridicaAdmin, PoblacionTerritorioColectivoAdmin]


class PuebloAdmin(GoogleAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(TerritorioComunidadIndigena, TerritorioComunidadIndigenaAdmin)
admin.site.register(TerritorioComunidadNegra, TerritorioComunidadNegraAdmin)
admin.site.register(Comunidad, ComunidadAdmin)
admin.site.register([Pueblo, ])
