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
                  'descripcion',
                 ('estado', 'fuente'),
                 )

          }),
      )

admin.site.register(Conflicto, ConflictoAdmin)
