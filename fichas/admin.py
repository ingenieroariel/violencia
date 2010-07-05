from django.contrib import admin
from fichas.models import Departamento, Municipio, Relato, Fuente, Victima, RelacionVictima, TipoViolencia, GrupoViolencia, ItemGrupoViolencia

admin.site.register([
    Departamento, Municipio, Relato, Fuente,
    Victima, RelacionVictima,
    TipoViolencia, GrupoViolencia, ItemGrupoViolencia
])