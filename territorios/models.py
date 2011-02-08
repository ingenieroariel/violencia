# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django_extensions.db.fields import ModificationDateTimeField
from django_extensions.db.fields import CreationDateTimeField, AutoSlugField
from django.contrib.gis.db.models import MultiPolygonField
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato, AutorDato
from django.template.defaultfilters import yesno
from violencia.territorios.utils import gen_rangos_cantidad
from utils import get_content_types_ids

"""
MODULO 1. LINEA BASE ORDENAMIENTO DEL TERRITORIO Y POBLACION
"""

ESTADOS_TRAMITES_JURIDICOS = (('S','Solicitud'),('N','Negaci�n'),('A','Aprovaci�n'))
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
TERRITORIOS = (
    ("territorio-col-indigena-titulado","Territorio Colectivo Indígena titulado"),
    ("territorio-col-indigena-no-titulado","Territorio Colectivo Indígena no titulado"),
    ("territorio-col-coms-negras-titulado","Territorio Colectivo Comunidades Negras titulado"),
    ("territorio-col-coms-negras-no-titulado","Territorio Colectivo Comunidades Negras no titulado"),
)

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
    ano_creacion = models.IntegerField('año de creacion', blank=True, null=True)
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
    total = models.IntegerField(verbose_name="Población Total", blank=True, null=True, help_text="habitantes")
    hombres = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    mujeres = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_0_a_4 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_5_a_9 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_10_a_14 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_15_a_19 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_20_a_24 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_25_a_29 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_30_a_34 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_35_a_39 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_40_a_44 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_45_a_49 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_50_a_54 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_55_a_59 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_60_a_64 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_65_a_69 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_70_a_74 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_75_a_79 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_80_a_84 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_85_a_89 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_90_o_mas = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    etnia_indigena = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    etnia_afro = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    etnia_otros = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    etnia_no_informa = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    individual = models.IntegerField(help_text='habitante (solo deplazados)', blank=True, null=True)
    masivo = models.IntegerField(help_text='habitantes (solo desplazados)', blank=True, null=True)
    cabecera = models.IntegerField(help_text='habitantes', blank=True, null=True)
    rural = models.IntegerField(help_text='habitantes', blank=True, null=True)
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

class Municipio(TerritorioPolitico):
    departamento = models.ForeignKey(Departamento)
    certificado = models.BooleanField(help_text="poner chulo si es certificado", default=False)
    area_total = models.FloatField(help_text="km2", blank=True, null=True)
    area_cabecera = models.FloatField(help_text="km2", blank=True, null=True)
    titulos_cabecera = models.CharField(max_length=50, null=True, blank=True)
    area_rural = models.FloatField(help_text="km2", blank=True, null=True)
    titulos_rural = models.CharField(max_length=50, null=True, blank=True)
    fuente_presupuesto = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_presupuesto_mpio")

    objects = models.GeoManager()

class TitulosIndividuales(models.Model):
    departamento = models.ForeignKey(Municipio, related_name="titulos_individuales")
    tipo = models.CharField(max_length=50, choices=( ("municipal","Cabecera municipal"),("rural","Rural") ) )
    cantidad = models.IntegerField(blank=True, null=True)
    area_total = models.FloatField(blank=True, null=True, help_text="Suma del área de todos los títulos individuales en km2")
    grupo_poblacional = models.CharField(max_length=255, blank=True, null=True, choices= GRUPO_POBLACIONAL_CHOICES, help_text="Puede seleccionar múltiples grupos dejando presionada la tecla Control")
    fuente_titulos = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Titulos individuales'

    def __unicode__(self):
        return "Cantidad: %s, Area: %s" % (self.cantidad, self.area_total)

class Pueblo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "Pueblo "+self.nombre

class TerritorioComunidad(Territorio):
    municipios = models.ManyToManyField(Municipio, null=True, blank=True)
    area = models.FloatField(null=True, blank=True, help_text="Area en hectáreas asignada en caso de ser titulado y area solicitada en caso de no serlo")
    limites = models.TextField(null=True, blank=True) 
    titulado = models.BooleanField(default=False)
    resolucion_constitucion = models.CharField(max_length=255, help_text="Dejar en blanco si no esta titulado", null=True, blank=True)

    objects = models.GeoManager()

    def __unicode__(self):
        titulacion =  yesno(self.titulado, 'titulado, no titulado')
        label = ''
        try:
            t = self.territoriocomunidadnegra
            label = "%s (%s): %s" % ('Com. Negra',titulacion, self.nombre)
        except:
            label = "%s (%s): %s" % ('Com. Indigena', titulacion, self.nombre)
        return label

class TerritorioComunidadIndigena(TerritorioComunidad):
   class Meta:
        verbose_name="Territorio Colectivo Indígena"
        verbose_name_plural="Territorios Colectivos Indígenas"

   objects = models.GeoManager()

   def numero_comunidades(self):
        return self.comunidadindigena_set.count()

class TerritorioComunidadNegra(TerritorioComunidad):
    class Meta:
        verbose_name="Territorio Colectivo Comunidades Negras"
        verbose_name_plural="Territorios Colectivos Comunidades Negras"

    objects = models.GeoManager()

    def numero_comunidades(self):
        return self.comunidadnegra_set.count()

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

    class Meta:
        verbose_name_plural = "comunidades negras"
        verbose_name = "comunidad negra"

class ComunidadIndigena(Comunidad):
    territorio = models.ForeignKey('TerritorioComunidadIndigena')
    pueblo = models.ForeignKey(Pueblo)

    class Meta:
        verbose_name_plural = "comunidades indigenas"
        verbose_name = "comunidad indigena"


SITUACION_CHOICES=(
   ('ampliacion','Ampliacion'),
   ('saneamiento', 'Saneamiento'),
   ('titulacion', 'Solicitud de Titulacion'),
)

class SituacionJuridica(models.Model):
    territorio = models.ForeignKey(TerritorioComunidad)
    estado_tramite = models.CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')
    fecha = models.DateField(help_text="Fecha de la resolucion o solicitud", blank=True, null=True)
    resolucion = models.CharField(max_length=255, null=True, blank=True, help_text="Numero de resolucion (si existe)")
    area = models.FloatField(help_text='Area en hectáreas', null=True, blank=True)
    limites = models.TextField('Limites o linderos')
    observaciones = models.TextField(blank=True, null=True)
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True, help_text="Campo opcional")

    class Meta:
        abstract = True

#para titulados solo indigenas
class Ampliacion(SituacionJuridica):
    class Meta:
        verbose_name_plural = "Solicitud: Ampliaciones (solo para territorios titulados)"

class Saneamiento(SituacionJuridica):
    poblacion_total = models.IntegerField(blank=True, null=True, help_text="cantidad de poblacion ajena")
    poblacion_afro = models.IntegerField(blank=True, null=True, help_text="cantidad")
    poblacion_otros = models.IntegerField(blank=True, null=True, help_text="cantidad")

    class Meta:
        verbose_name_plural = "Solicitud: Saneamientos (solo para territorios titulados)"

#para no titulados
class SolicitudTitulacion(SituacionJuridica):
    class Meta:
        verbose_name = "Solicitud: Titulacion"
        verbose_name_plural = "Solicitud: Titulacion (Solo para territorios NO titulados)"


class PoblacionSimple(models.Model):
    familias = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(verbose_name="Población Total", blank=True, null=True, help_text="habitantes")
    hombres = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    mujeres = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_0_a_4 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_5_a_9 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_10_a_14 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_15_a_19 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_20_a_24 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_25_a_29 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_30_a_34 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_35_a_39 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_40_a_44 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_45_a_49 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_50_a_54 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_55_a_59 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_60_a_64 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_65_a_69 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_70_a_74 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_75_a_79 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_80_a_84 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_85_a_89 = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)
    edad_90_o_mas = models.DecimalField(help_text="%", max_digits=4, decimal_places=1, blank=True, null=True)    
    fuente = models.ForeignKey(FuenteDato) 

    class Meta:
        abstract=True


class PoblacionTerritorioColectivo(PoblacionSimple):
    territorio = models.ForeignKey(TerritorioComunidad, related_name="estadistica_comunidad")

class PoblacionComunidadNegra(PoblacionSimple):
    territorio = models.ForeignKey(ComunidadNegra, related_name="estadistica_asentamiento")
    class Meta:
        verbose_name= "poblacion de comunidad negra"
        verbose_name_plural= "poblaciones de comunidades negras"

class PoblacionComunidadIndigena(PoblacionSimple):
    territorio = models.ForeignKey(ComunidadIndigena, related_name="estadistica_asentamiento")
    class Meta:
        verbose_name= "poblacion de comunidad"
        verbose_name_plural= "poblaciones de comunidades"

class Ubicacion(models.Model):
    # Este es el foreign key que apunta al objeto al que le queremos poner ubicacion.
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_ubicacio")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    # Agregar ForeignKey a un Territorio, ya sea depto, mpio, o territorio indigena / negro.x
    content_type_ubicacion = models.ForeignKey(ContentType,  limit_choices_to={'id__in':get_content_types_ids()}, null = True, blank = True)
    seleccionador = models.CharField(max_length=255, choices=(("---","---"),) , null = True, blank = True)
    valor = models.PositiveIntegerField(null = True, blank = True)
    objeto = generic.GenericForeignKey('content_type_ubicacion','valor')

    def __unicode__(self):
        return '%s: %s' % ( self.content_type_ubicacion.name, self.objeto.__unicode__() )

    class Meta:
        verbose_name_plural= "Ubicaciones"
    

    # Lo ideal es que primero se seleccione el tipo de territorio y luego el objeto.
    # por ejemplo, primero seleccion "Departamento" y luego "Cauca" o "Territorio Indigena" y luego "Papuchi".
    # A cualquier elemento de la base de datos se le puede agregar una ubicacion ( a algunos se le peude agregar varias).

