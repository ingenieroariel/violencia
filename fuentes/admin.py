from django.contrib.gis import admin
from fuentes.models import AutorDato, FuenteDato

class FuenteDatoAdmin(admin.ModelAdmin):
        list_display= ('nombre_documento', 'autor', 'fecha', 'fecha_ingreso',
                       'archivo', 'usuario', 'notas')

admin.site.register(AutorDato)
admin.site.register(FuenteDato, FuenteDatoAdmin)
