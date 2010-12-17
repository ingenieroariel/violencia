# -*- coding: utf-8 -*-
from colonizacion.models import *
from django.contrib.gis import admin

class UsoTerritorioInline(admin.StackedInline):
    model = UsoTerritorio
    extra = 1

class ColonizacionAdmin(admin.ModelAdmin):
#    list_display = ( 'nombre', 'id', 'area_total', 'capital', 'ingresos', 'gastos','cantidad_municipios_pacifico',)
#    search_fields = ['nombre','capital']
#    list_filter = ('fecha_creacion',)
    inlines = [UsoTerritorioInline]
    fieldsets = (
        ("Ubicacion", {
              'fields':
                 (
                 'municipios',
                 'territorios',
                 'referencia_cartografica',
                 'area'
                 )
          }),
          ('Procedencia', {
              'fields': (
                'procedencia',
                'cantidad_personas',
                )
          }),
          ('Causa', {
              'fields': (
                'causa',
                'actor',
                'megaproyecto',
                )
          }),
      )


admin.site.register(Colonizacion,ColonizacionAdmin)
