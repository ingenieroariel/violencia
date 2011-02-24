# -*- coding: utf-8 -*-
from megaproyectos.models import Afectacion
from cultivos_ilicitos.models import *
from django.contrib.gis import admin
from django.contrib.contenttypes import generic
from django import forms

class AfectacionInline(generic.GenericStackedInline):
    model = Afectacion
    extra = 1

class ErradicacionInline(admin.StackedInline):
    model = ErradicacionCultivosIlicitos
    extra = 1

class InversionInline(admin.StackedInline):
    model = InversionSocialCultivosIlicitos
    extra = 1

class CultivosIlicitosAdmin(admin.ModelAdmin):
    list_display = ( 'municipio', 'tipo', 'get_promotores')
#    search_fields = ['nombre','capital']
    list_filter = ('municipio',)
    inlines = [AfectacionInline, ErradicacionInline, InversionInline]
    fieldsets = (
            (None, {
              'fields':
                 (
                 'municipio',
                 'tipo',
                 )
          }),
          (None, {
              'fields': 
                 (
                 'area',
                 'promotores',
                 )
          }),
          ('Participacion', {
              'fields': (
                'participacion_comunidad',
                'comunidad_tipo',
                ('participacion_otros','participacion_otros_cuales'),
                'otros_tipo',
                'fuente',
                )
          }),
      )


admin.site.register(CultivosIlicitos,CultivosIlicitosAdmin)
admin.site.register(Promotores)
admin.site.register(TipoParticipacion)
