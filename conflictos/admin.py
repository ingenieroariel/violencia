# -*- coding: utf-8 -*-
from conflictos.models import *
from django.contrib.gis import admin

class ConflictoAdmin(admin.ModelAdmin):
    fieldsets = (
          (None, {
              'fields':
                  (
                    'categoria',
                    'tipo'
                  )
          }),
          ('Descripción', {
              'fields':
                 (
                 'ubicacion', 'actores','hechos',
                 ('estado','fecha','fuente'),
                 )

          }),
      )

admin.site.register(Conflicto, ConflictoAdmin)