# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django_extensions.db.fields import ModificationDateTimeField
from django_extensions.db.fields import CreationDateTimeField, AutoSlugField
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
class Territorio(models.Model):
    nombre = models.CharField(max_length=100)
    slug = AutoSlugField('slug', populate_from='nombre', blank=True, null=True)
    geom = models.GeometryField(srid=4326, null=True, blank=True)
    objects = models.GeoManager()
    informacion_adicional = models.TextField(blank=True, null=True)    

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.nombre


class TerritorioPolitico(Territorio):
    fecha_creacion = models.DateField('fecha de creacion', blank=True, null=True)
    presupuesto_anual = models.IntegerField(blank=True, null=True)
    ingresos = models.FloatField('ingresos totales', blank=True, null=True, help_text="millones de pesos")
    gastos = models.FloatField('gastos totales', blank=True, null=True, help_text="millones de pesos")
    objects = models.GeoManager()

    class Meta:
        abstract = True

ESTADISTICA_CHOICES = (
    ('poblacion', 'Poblacion'),
    ('recepcion', 'Recepcion desplazados'),
    ('expulsion', 'Expulsion desplazados'),
)

class Estadistica(models.Model):
    tipo = models.CharField(max_length=255, choices=ESTADISTICA_CHOICES)
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
    rural = models.IntegerField(help_text='habitantes', blank=True, null=True)
    individual = models.IntegerField(help_text='habitante (solo deplazados)', blank=True, null=True)
    masivo = models.IntegerField(help_text='habitantes (solo desplazados)', blank=True, null=True)
    cabecera = models.IntegerField(help_text='habitantes', blank=True, null=True)
    rural = models.IntegerField(help_text='habitantes (solo desplazados)', blank=True, null=True)
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        abstract=True 

    def __unicode__(self):
        return self.tipo

class EstadisticaDepartamento(Estadistica):
    territorio = models.ForeignKey('Departamento')
    
class EstadisticaMunicipio(Estadistica):
    territorio = models.ForeignKey('Municipio')

    def __unicode__(self):
        return "Estadistica "+ self.tipo


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
    titulos_cabecera = models.ForeignKey(TitulosIndividuales, verbose_name="titulos individuales área cabecera", related_name="tit_cab", null=True, blank=True)
    area_rural = models.FloatField(help_text="km2", blank=True, null=True)
    titulos_rural = models.ForeignKey(TitulosIndividuales, verbose_name="titulos individuales área cabecera", related_name="tit_rur", null=True, blank=True)
    fuente_presupuesto = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_presupuesto_mpio")

    objects = models.GeoManager()

class Pueblo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "Pueblo "+self.nombre

class TerritorioComunidad(Territorio):
    departamento = models.ForeignKey(Departamento, null=True, blank=True)
    municipios = models.ManyToManyField(Municipio, null=True, blank=True)
    area = models.FloatField(null=True, blank=True, help_text="Area asignada en caso de ser titulado y area solicitada en caso de no serlo")
    limites = models.TextField(null=True, blank=True) 
    titulado = models.BooleanField(default=False)
    resolucion_constitucion = models.CharField(max_length=255, help_text="Dejar en blanco si no esta titulado", null=True, blank=True)

    objects = models.GeoManager()

    def numero_comunidades(self):
        return self.comunidadnegra_set.count()
    

class TerritorioComunidadIndigena(TerritorioComunidad):
   class Meta:
        verbose_name="Territorio Colectivo Indígena"
        verbose_name_plural="Territorios Colectivos Indígenas"

   objects = models.GeoManager()


class TerritorioComunidadNegra(TerritorioComunidad):
    class Meta:
        verbose_name="Territorio Colectivo Comunidades Negras"
        verbose_name="Territorios Colectivos Comunidades Negras"

    objects = models.GeoManager()

class Comunidad(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_disolucion = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "Comunidad: "+ self.nombre

    class Meta:
         verbose_name_plural = "comunidades"
         abstract=True

class ComunidadNegra(Comunidad):
    territorio = models.ForeignKey('TerritorioComunidadNegra')

class ComunidadIndigena(Comunidad):
    territorio = models.ForeignKey('TerritorioComunidadIndigena')
    pueblo = models.ForeignKey(Pueblo)


SITUACION_CHOICES=(
   ('ampliacion','Ampliacion'),
   ('saneamiento', 'Saneamiento'),
   ('titulacion', 'Solicitud de Titulacion'),
)

class SituacionJuridica(models.Model):
    tipo = models.CharField(max_length=255, choices=SITUACION_CHOICES, blank=True, null=True)
    territorio = models.ForeignKey(TerritorioComunidad)
    fecha = models.DateField(help_text="Fecha de la resolucion o solicitud", blank=True, null=True)
    resolucion = models.CharField(max_length=255, null=True, blank=True, help_text="Numero de resolucion (si existe)")
    area = models.FloatField(help_text='Area en metros cuadrados', null=True, blank=True)
    limites = models.TextField('Limites o linderos')
    estado_tramite = models.CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')
    observaciones = models.TextField(blank=True, null=True)
    poblacion_general = models.IntegerField(help_text='Solo para saneamiento', blank=True, null=True)
    poblacion_afro = models.IntegerField(help_text='Solo para saneamiento', blank=True, null=True)
    poblacion_otros = models.IntegerField(help_text='Solo para saneamiento', blank=True, null=True)
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True, help_text="Campo opcional")

    class Meta:
        abstract = True

class PoblacionSimple(models.Model):
    familias = models.IntegerField(blank=True, null=True)
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
    fuente = models.ForeignKey(FuenteDato) 

    class Meta:
        abstract=True


class PoblacionTerritorioColectivo(PoblacionSimple):
    territorio = models.ForeignKey(TerritorioComunidad, related_name="estadistica_comunidad")

class PoblacionComunidadNegra(PoblacionSimple):
    territorio = models.ForeignKey(ComunidadNegra, related_name="estadistica_asentamiento")
    class Meta:
        verbose_name= "poblacion de comunidad"
        verbose_name_plural= "poblaciones de comunidades"

class PoblacionComunidadIndigena(PoblacionSimple):
    territorio = models.ForeignKey(ComunidadIndigena, related_name="estadistica_asentamiento")
    class Meta:
        verbose_name= "poblacion de comunidad"
        verbose_name_plural= "poblaciones de comunidades"
