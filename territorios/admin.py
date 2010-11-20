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

class DepartamentoAdmin(GoogleAdmin):
    list_display = ('nombre', 'area_total', 'capital', 'ingresos', 'gastos','cantidad_municipios_pacifico', 'total')
    fieldsets = (
          (None, {
              'fields': 
                 (
                 'nombre', 
                 ('area_total', 'area_rural', 'area_urbana'), 
                'capital',
                 ('cantidad_municipios_total', 'cantidad_municipios_pacifico'),
                  'fecha_creacion',

                 )
                
          }),
          ('Presupuesto', {
              'fields': (('ingresos', 'gastos'),
                          'fuente_presupuesto',
                          )
          }),
          ('Poblacion', {
              'fields': (
                        'total',
                        ('hombres', 'mujeres'),
                        ('edad_0_a_9', 'edad_10_a_19', 'edad_20_a_29'),
                        ('edad_30_a_39', 'edad_40_a_49', 'edad_50_a_59'),
                        ('edad_60_a_69', 'edad_70_a_79', 'edad_80_a_89'),
                        'edad_90_o_mas',
                        ('etnia_indigena', 'etnia_afro'),
                        ('etnia_otros', 'etnia_no_informa'),
                        ('cabecera', 'rural'),
                        'fuente_poblacion',
                        
                        )   
                         
          }),
#          ('Advanced options', {
#              'classes': ('collapse',),
#              'fields': ('geom', )
#          }),
      )




class TitulosIndividualesForm(forms.ModelForm):
    grupo_poblacional = forms.MultipleChoiceField(choices=GRUPO_POBLACIONAL_CHOICES, widget=forms.SelectMultiple,  help_text="Puede seleccionar múltiples grupos dejando presionada la tecla Control")
    class Meta:
        model = TitulosIndividuales

class TitulosIndividualesAdmin(admin.ModelAdmin):
#    form = TitulosIndividualesForm
     pass

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(TitulosIndividuales, TitulosIndividualesAdmin)
admin.site.register(TerritorioIndigena, GoogleAdmin)
admin.site.register(TerritorioIndigenaNoTitulado, GoogleAdmin)
admin.site.register(TerritorioNegro, GoogleAdmin)
admin.site.register(TerritorioNegroNoTitulado, GoogleAdmin)
