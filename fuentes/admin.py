from django.contrib.gis import admin
from fuentes.models import AutorDato, FuenteDato

class FuenteDatoAdmin(admin.ModelAdmin):
        list_display= ('nombre_documento', 'autor', 'fecha', 'fecha_ingreso',
                       'archivo', 'usuario', 'notas')
        fieldsets = (
                (None, {
                      'fields':
                         (
                         ('nombre_documento','autor'),
                         ('fecha','ano'),
                         'frecuencia_actualizacion',
                         ('fecha_ingreso','usuario'),
                         
                         'archivo',
                         'notas',
                         ),
                  }),
            )

admin.site.register(AutorDato)
admin.site.register(FuenteDato, FuenteDatoAdmin)
