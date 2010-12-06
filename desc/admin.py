# -*- coding: utf-8 -*-
from desc.models import *
from django.contrib.gis import admin

class InstitucionEducativaInline(admin.StackedInline):
    model = InstitucionEducativa
    extra = 1
    
class EducacionAdmin(admin.ModelAdmin):
    inlines = (InstitucionEducativaInline,)
    #list_filter = ('object_id', )
    fieldsets = (
          ('Nivel Educativo', {
              'fields':
                 (
                 'content_type',
                 'object_id',

                 ('nivel_educativo_preescolar', 'nivel_educativo_primaria', 'nivel_educativo_secundaria'),
                 ('nivel_educativo_mediatec','nivel_educativo_normalista'),
                 ('nivel_educativo_sup_tecnica','nivel_educativo_sup_tecnologica','nivel_educativo_sup_profesional'),
                  'instituciones_total',
                  'fuente_nivel_educativo',
                 )

          }),
      )



admin.site.register([IndicadorBasico, ])
admin.site.register(Educacion, EducacionAdmin)
