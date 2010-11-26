from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from fichas.models import Departamento, Municipio, Relato, Fuente, Victima, RelacionVictima, TipoViolencia, GrupoViolencia, ItemGrupoViolencia

GMAP = GoogleMap()

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

class RelacionVictimaInline(admin.TabularInline):
    model = RelacionVictima

class RelatoAdmin(GoogleAdmin):
    pass

class VictimaAdmin(admin.ModelAdmin):
    inlines = [RelacionVictimaInline,]

class FuenteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Relato, RelatoAdmin)
admin.site.register(Victima, VictimaAdmin)
admin.site.register(Fuente, FuenteAdmin)
