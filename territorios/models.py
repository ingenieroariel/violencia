# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django_extensions.db.fields import ModificationDateTimeField
from django_extensions.db.fields import CreationDateTimeField
from django.contrib.gis.db.models import MultiPolygonField
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from fuentes.models import FuenteDato, AutorDato
from violencia.territorios.utils import gen_rangos_cantidad

"""
MODULO 1. LINEA BASE ORDENAMIENTO DEL TERRITORIO Y POBLACION
"""

ESTADOS_TRAMITES_JURIDICOS = (('S','Solicitud'),('A','Aprovaci�n'),('N','Negaci�n'))
TIPOS_MUNICIPIO = ((0,'Fronterizo'),(1,u'Costero'),(2,'Rivere�o'),(3,'Del Interior'))
TIPOS_LIMITE = ((0,'Departamento'),(1,'Pais'),(2,'Municipios'),(3,'Comunidades'))
GRUPOS_POBLACIONAL = (('I','Indigena'),('A',u'Afro'), ('O','Otros'))
TIPOS_ETNICOS = (('INTRA','Intra�tnico'),('INTER','Inter�tnico'))
TIPOS_CONFICTO = ( (0,'Cultural'), (1,'Pol�tico'), (2,'Econ�mico'), (3,'Recursos Naturales'), (4,'Territorial'), (5,'Otros') )
TIPOS_SERVICIOS_PUBLICOS = ( (0, 'Acueducto'), (1, 'Alcantarillado'), (2, 'Energia') )
TIPOS_INSTITUCION = ((0,'Publica'),(1,'Privada'))
TIPOS_CONTRATO = ((0,'Temporal'),(1,'Fijo'))
TIPOS_INSTALACIONES_SALUD = ((0,'Centro de salud'),(1,'Puesto de salud'),(2,'Hospital') )
TIPOS_REGIMEN = ((0,'Subsidiario'),(1,'Contributivo'))

# Create your models here.
class Territorio(TitleSlugDescriptionModel):
    nombre = models.CharField(max_length=100)
    geom = models.PolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return nombre


class TerritorioPolitico(Territorio):
    fecha_creacion = models.DateField('fecha de creacion', blank=True, null=True)
    presupuesto_anual = models.IntegerField(blank=True, null=True)
    ingresos = models.FloatField('ingresos totales', blank=True, null=True, help_text="millones de pesos")
    gastos = models.FloatField('gastos totales', blank=True, null=True, help_text="millones de pesos")

    #poblacion
    total = models.SmallIntegerField(verbose_name="Población Total", blank=True, null=True, help_text="habitantes")
    hombres = models.FloatField(help_text="%", blank=True, null=True)
    mujeres = models.FloatField(help_text="%", blank=True, null=True)
    edad_0_a_9 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_10_a_19 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_20_a_29 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_30_a_39 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_40_a_49 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_50_a_59 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_60_a_69 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_70_a_79 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_80_a_89 = models.SmallIntegerField(help_text="%", blank=True, null=True)
    edad_90_o_mas = models.SmallIntegerField(help_text="%", blank=True, null=True)    
    etnia_indigena = models.SmallIntegerField(help_text="%", blank=True, null=True)
    etnia_afro = models.SmallIntegerField(help_text="%", blank=True, null=True)
    etnia_otros = models.SmallIntegerField(help_text="%", blank=True, null=True)
    etnia_no_informa = models.SmallIntegerField(help_text="%", blank=True, null=True)
    cabecera = models.IntegerField(help_text='habitantes', blank=True, null=True)
    rural = models.IntegerField(help_text='habitantes', blank=True, null=True)

    objects = models.GeoManager()

    class Meta:
        abstract = True

class Departamento(TerritorioPolitico):
    """
    Departamento
    """
    area_total = models.FloatField(help_text="km2", blank=True, null=True)
    area_urbana = models.FloatField(help_text="km2", blank=True, null=True)
    area_rural = models.FloatField(help_text="km2", blank=True, null=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    cantidad_municipios_total = models.IntegerField('cantidad de municipios', blank=True, null=True)
    cantidad_municipios_pacifico = models.IntegerField('cantidad de municipios en el pacifico', blank=True, null=True)
    fuente_presupuesto = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_presupuesto_dpto")
    fuente_poblacion = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_poblacion_dpto")

    @property
    def simplegeom(self):
        return self.geometry.simplify(tolerance=0.04, preserve_topology=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.nombre

class PoblacionPequena(models.Model):
    cantidad_hombres = models.SmallIntegerField()
    cantidad_mujeres = models.SmallIntegerField()
    edad_0_5 = models.SmallIntegerField(verbose_name="Edad entre 0 y 5", default=0)
    edad_6_10 = models.SmallIntegerField(verbose_name="Edad entre 6 y 10", default=0)
    edad_11_15 = models.SmallIntegerField(verbose_name="Edad entre 11 y 15", default=0)
    edad_16_20 = models.SmallIntegerField(verbose_name="Edad entre 16 y 20", default=0)
    edad_21_25 = models.SmallIntegerField(verbose_name="Edad entre 21 y 25", default=0)
    edad_26_30 = models.SmallIntegerField(verbose_name="Edad entre 26 y 30", default=0)
    edad_31_35 = models.SmallIntegerField(verbose_name="Edad entre 31 y 35", default=0)
    edad_36_40 = models.SmallIntegerField(verbose_name="Edad entre 36 y 40", default=0)
    edad_41_45 = models.SmallIntegerField(verbose_name="Edad entre 41 y 45", default=0)
    edad_46_50 = models.SmallIntegerField(verbose_name="Edad entre 46 y 50", default=0)
    edad_51_55 = models.SmallIntegerField(verbose_name="Edad entre 51 y 55", default=0)
    edad_56_60 = models.SmallIntegerField(verbose_name="Edad entre 56 y 60", default=0)
    edad_61_65 = models.SmallIntegerField(verbose_name="Edad entre 61 y 65", default=0)
    edad_66_70 = models.SmallIntegerField(verbose_name="Edad entre 66 y 70", default=0)
    edad_71_75 = models.SmallIntegerField(verbose_name="Edad entre 71 y 75", default=0)
    edad_76_80 = models.SmallIntegerField(verbose_name="Edad entre 76 y 80", default=0)
    edad_81_85 = models.SmallIntegerField(verbose_name="Edad entre 81 y 85", default=0)
    edad_86_90 = models.SmallIntegerField(verbose_name="Edad entre 86 y 90", default=0)
    edad_91_95 = models.SmallIntegerField(verbose_name="Edad entre 91 y 95", default=0)
    porcentaje_pueblos = models.SmallIntegerField()

    def __unicode__(self):
        return 'Hombres: %s, Mujeres: %s, Pueblos: %s %' % (self.cantidad_hombres, self.cantidad_mujeres, self.porcentaje_pueblos)

"""
    Cantidad de comunidades, asentamientos
    Nombre de comunidades, asentamientos
"""
class Asentamiento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    decha_disolucion = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.nombre

GRUPO_POBLACIONAL_CHOICES = (
      ("indigena", "Indigena"),
      ("afro", "Afro"),
      ("otros", "Otros"),
)

class TitulosIndividuales(models.Model):
    cantidad = models.IntegerField(blank=True, null=True)
    area_total = models.FloatField(blank=True, null=True, help_text="Suma del área de todos los títulos individuales en km2")
    grupo_poblacional = models.CharField(max_length=255, blank=True, null=True, choices= GRUPO_POBLACIONAL_CHOICES, help_text="Puede seleccionar múltiples grupos dejando presionada la tecla Control")
    fuente_titulos = models.ForeignKey(FuenteDato, null=True, blank=True)

    def __unicode__(self):
        return "Cantidad: %s, Area: %s" % (self.cantidad, self.area_total)

class Municipio(TerritorioPolitico):
    departamento = models.ForeignKey(Departamento)
    area_total = models.FloatField(help_text="km2", blank=True, null=True)
    area_cabecera = models.FloatField(help_text="km2", blank=True, null=True)
    titulos_cabecera = models.ForeignKey(TitulosIndividuales, verbose_name="titulos individuales área cabecera", related_name="tit_cab")
    area_rural = models.FloatField(help_text="km2", blank=True, null=True)
    titulos_rural = models.ForeignKey(TitulosIndividuales, verbose_name="titulos individuales área cabecera", related_name="tit_rur")
    fuente_presupuesto = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_presupuesto_mpio")
    fuente_poblacion = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_poblacion_mpio")

    objects = models.GeoManager()

class TerritorioComunidad(Territorio):
    departamento = models.ForeignKey(Departamento)
    asentamientos = models.ManyToManyField(Asentamiento)
    poblacion_total = models.ForeignKey(PoblacionPequena)

    objects = models.GeoManager()

class TerritorioComunidadIndigena(TerritorioComunidad):
    objects = models.GeoManager()

class TerritorioComunidadNegra(TerritorioComunidad):
    objects = models.GeoManager()

class Titulacion(models.Model):
    resolucion_fecha = models.DateField()
    resolucion_codigo = models.CharField(max_length=50)
    limites = models.CharField(max_length=255) #gis?
    estado_tramite = models.CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')

class Saneamiento(models.Model):
    ampliacion_resolucion_fecha = models.DateField()
    ampliacion_resolucion_codigo = models.CharField(max_length=50)
    ampliacion_limites = models.CharField(max_length=255) #gis?
    ampliacion_estado_tramite = models.CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')

    saneamiento_resolucion_fecha = models.DateField()
    saneamiento_resolucion_codigo = models.CharField(max_length=50)
    saneamiento_area = models.CharField(max_length=255) #gis?
    saneamiento_poblacion_general = models.IntegerField()
    saneamiento_poblacion_afro = models.IntegerField()
    saneamiento_poblacion_otros = models.IntegerField()
    saneamiento_limites = models.CharField(max_length=255) #gis?
    saneamiento_estado_tramite = models.CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')

class Pueblo(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

class TerritorioIndigena(TerritorioComunidadIndigena):
    departamento = models.ForeignKey(Departamento)
    municipios = models.ManyToManyField(Municipio, related_name='indigena_municipio')
    pueblos = models.ManyToManyField(Pueblo)
    resolucion_constitucion = models.IntegerField()
    area = models.CharField(max_length=255) #gis?
    limites = models.CharField(max_length=255) #gis?
    familias = models.IntegerField("Número de familias", default=0)
    situacion_juridica = models.ForeignKey(Saneamiento)

    objects = models.GeoManager()

    class Meta:
        verbose_name="Territorio Colectivo Indígena: Resguardo"
        verbose_name_plural="Territorios Colectivos Indígenas: Resguardos"

class TerritorioIndigenaNoTitulado(TerritorioComunidadIndigena):
    departamento = models.ForeignKey(Departamento)
    municipios = models.ManyToManyField(Municipio, related_name='indigena_not_municipio')
    pueblos = models.ManyToManyField(Pueblo)
    area_solicitada = models.CharField(max_length=255) #gis?
    familias = models.IntegerField("Número de familias", default=0)
    situacion_juridica = models.ForeignKey(Titulacion)

    objects = models.GeoManager()

    class Meta:
        verbose_name="Territorio Colectivo Indígena No Titulado"
        verbose_name_plural="Territorios Colectivos Indígenas No Titulados"

class TerritorioNegro(TerritorioComunidadNegra):
    departamento = models.ForeignKey(Departamento)
    municipios = models.ManyToManyField(Municipio, related_name='negro_municipio')
    resolucion_constitucion = models.IntegerField()
    area = models.CharField(max_length=255) #gis?
    limites = models.CharField(max_length=255) #gis?

    objects = models.GeoManager()

    class Meta:
        verbose_name="Territorio Colectivo Comunidades Negras: Título Colectivo"
        verbose_name_plural="Territorios Colectivos Comunidades Negras: Títulos Colectivos"

class TerritorioNegroNoTitulado(TerritorioComunidadNegra):
    departamento = models.ForeignKey(Departamento)
    municipios = models.ManyToManyField(Municipio, related_name='negro_not_municipio')
    area_solicitada = models.CharField(max_length=255) #gis?
    situacion_juridica = models.ForeignKey(Titulacion)

    objects = models.GeoManager()

    class Meta:
        verbose_name="Territorio Colectivo Comunidades Negras No Titulado"
        verbose_name_plural="Territorios Colectivos Comunidades Negras No Titulados"

