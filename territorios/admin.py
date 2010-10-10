from territorios.models import *
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap

GMAP = GoogleMap()

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'
    default_lon = -8228293
    default_lat = 508764
    default_zoom = 5
    
admin.site.register(TerritorioIndio, GoogleAdmin)
admin.site.register(TerritorioIndioNoTitulado, GoogleAdmin)
admin.site.register(TerritorioNegro, GoogleAdmin)
admin.site.register(TerritorioNegroNoTitulado, GoogleAdmin)


""" BEGIN InstitucionEducativa """
class PoblacionPreescolarStacked(admin.StackedInline):
    model = PoblacionEstudiantilPreescolar
    extra = 1
    max_num=1

class PoblacionBasicaPrimariaStacked(admin.StackedInline):
    model = PoblacionEstudiantilBasicaPrimaria
    extra = 1
    max_num=1

class PoblacionBasicaSecundariaStacked(admin.StackedInline):
    model = PoblacionEstudiantilBasicaSecundaria
    extra = 1
    max_num=1

class PoblacionMediaVocacionalStacked(admin.StackedInline):
    model = PoblacionEstudiantilMediaVocacional
    extra = 1
    max_num=1

class CoberturaPreescolarStacked(admin.StackedInline):
    model = CoberturaEstudiantilPreescolar
    extra = 1
    max_num=1

class CoberturaPrimariaStacked(admin.StackedInline):
    model = CoberturaEstudiantilBasicaPrimaria
    extra = 1
    max_num=1

class CoberturaSecundariaStacked(admin.StackedInline):
    model = CoberturaEstudiantilBasicaSecundaria
    extra = 1
    max_num=1

class CoberturaMediaVocacionalStacked(admin.StackedInline):
    model = CoberturaEstudiantilMediaVocacional
    extra = 1
    max_num=1

class CoberturaDesplazadosPreescolarStacked(admin.StackedInline):
    model = CoberturaDesplazadosPreescolar
    extra = 1
    max_num=1

class CoberturaDesplazadosPrimariaStacked(admin.StackedInline):
    model = CoberturaDesplazadosPrimaria
    extra = 1
    max_num=1

class CoberturaDesplazadosSecundariaStacked(admin.StackedInline):
    model = CoberturaDesplazadosSecundaria
    extra = 1
    max_num=1

class CoberturaDesplazadosMediaStacked(admin.StackedInline):
    model = CoberturaDesplazadosMedia
    extra = 1
    max_num=1

class EstudiantesDesercionStacked(admin.StackedInline):
    model = EstudiantesDesercion
    extra = 1
    max_num=1

class EstudiantesPromocionStacked(admin.StackedInline):
    model = EstudiantesPromocion
    extra = 1
    max_num=1

class EstudiantesRepitenciaStacked(admin.StackedInline):
    model = EstudiantesRepitencia
    extra = 1
    max_num=1

class EstudiantesAnalfabetismoStacked(admin.StackedInline):
    model = EstudiantesAnalfabetismo
    extra = 1
    max_num=1
    
class InstitucionEducativaAdmin(admin.ModelAdmin):
    inlines = [PoblacionPreescolarStacked,PoblacionBasicaPrimariaStacked,PoblacionBasicaSecundariaStacked,PoblacionMediaVocacionalStacked,
    CoberturaPreescolarStacked,CoberturaPrimariaStacked,CoberturaSecundariaStacked,CoberturaMediaVocacionalStacked,
    CoberturaDesplazadosPreescolarStacked,CoberturaDesplazadosPrimariaStacked,CoberturaDesplazadosMediaStacked,CoberturaDesplazadosMediaStacked,
    EstudiantesDesercionStacked,EstudiantesPromocionStacked,EstudiantesRepitenciaStacked,EstudiantesAnalfabetismoStacked]

admin.site.register(InstitucionEducativa, InstitucionEducativaAdmin)
"""  END InstitucionEducativa """


""" BEGIN Desc """
class EsperanzaVidaStacked(admin.StackedInline):
    model = EsperanzaVida
    extra = 1
    max_num=1

class MortalidadInfantilStacked(admin.StackedInline):
    model = MortalidadInfantil
    extra = 1
    max_num=1

class MortalidadMaternoInfantilStacked(admin.StackedInline):
    model = MortalidadMaternoInfantil
    extra = 1
    max_num=1

class MortalidadTotalStacked(admin.StackedInline):
    model = MortalidadTotal
    extra = 1
    max_num=1

class TasaAnalfabetizacionStacked(admin.StackedInline):
    model = TasaAnalfabetizacion
    extra = 1
    max_num=1

class MatriculasStacked(admin.StackedInline):
    model = Matriculas
    extra = 1
    max_num=1

class EducacionPreescolarStacked(admin.StackedInline):
    model = EducacionPreescolar
    extra = 1
    max_num=1

class EducacionPrimariaStacked(admin.StackedInline):
    model = EducacionPrimaria
    extra = 1
    max_num=1

class EducacionSecundariaStacked(admin.StackedInline):
    model = EducacionSecundaria
    extra = 1
    max_num=1

class EducacionVocacionalStacked(admin.StackedInline):
    model = EducacionVocacional
    extra = 1
    max_num=1

class EducacionTecnicaStacked(admin.StackedInline):
    model = EducacionTecnica
    extra = 1
    max_num=1

class EducacionNormalistaStacked(admin.StackedInline):
    model = EducacionNormalista
    extra = 1
    max_num=1

class EducacionTecnicaTecnologicaStacked(admin.StackedInline):
    model = EducacionTecnicaTecnologica
    extra = 1
    max_num=1

class EducacionSuperiorStacked(admin.StackedInline):
    model = EducacionSuperior
    extra = 1
    max_num=1


class ICBFStacked(admin.StackedInline):
    model = ICBF
    extra = 1
    max_num=1

class EconomiaStacked(admin.StackedInline):
    model = Economia
    extra = 1
    max_num=1

class EconomiaStacked(admin.StackedInline):
    model = Economia
    extra = 1
    max_num=1

class CulturaStacked(admin.StackedInline):
    model = Cultura
    extra = 1
    max_num=1

class ServicioPublicoStacked(admin.StackedInline):
    model = ServicioPublico
    extra = 3
    max_num=3


class DescAdmin(admin.ModelAdmin):
    inlines = [EsperanzaVidaStacked,MortalidadInfantilStacked,MortalidadMaternoInfantilStacked,MortalidadTotalStacked,
    TasaAnalfabetizacionStacked,MatriculasStacked,EducacionPreescolarStacked,EducacionPrimariaStacked,EducacionSecundariaStacked,
    EducacionVocacionalStacked,EducacionTecnicaStacked,EducacionNormalistaStacked,EducacionTecnicaTecnologicaStacked,EducacionSuperiorStacked,
    ICBFStacked,EconomiaStacked,CulturaStacked,ServicioPublicoStacked]

admin.site.register(Desc, DescAdmin)
""" END BEGIN Desc """
