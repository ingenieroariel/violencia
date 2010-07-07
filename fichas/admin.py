from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from fichas.models import Departamento, Municipio, Relato, Fuente, Victima, RelacionVictima, TipoViolencia, GrupoViolencia, ItemGrupoViolencia

GMAP = GoogleMap()

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

admin.site.register(Departamento, GoogleAdmin)
admin.site.register(Municipio, GoogleAdmin)
admin.site.register(Relato, GoogleAdmin)

admin.site.register([
    Fuente,
    Victima, RelacionVictima,
    TipoViolencia, GrupoViolencia, ItemGrupoViolencia
])
