# -*- coding: utf-8 -*-
from django.db.models.fields import DateField
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import SmallIntegerField
from django.db.models.fields.related import ManyToManyField
from django.db.models.fields import CharField
from violencia.territorios.utils import gen_rangos_cantidad
from django.db import models

"""
MODULO 1. LINEA BASE ORDENAMIENTO DEL TERRITORIO Y POBLACION

1.  Territorio Colectivo Indigena titulado
2.  Territorio Colectivo Indigena no titulado
3.  Territorio Colectivo Comunidades Negras titulado
4.  Territorio Colectivo Comunidades Negras no titulado
5.  Municipio
6.  Departamento

"""
#RANGOS_CANTIDAD = gen_rangos_cantidad()
ESTADOS_TRAMITES_JURIDICOS = (('S','Solicitud'),('A','Aprovación'),('N','Negación'))
TIPOS_MUNICIPIO = (('0','Fronterizo'),('1','Costero'),('2','Rivereño'),('3','Del Interior'))
TIPOS_LIMITE = (('0','Departamento'),('1','Pais'),('2','Municipios'),('3','Comunidades'))

# Create your models here.
class Territorio(models.Model):
    nombre = models.CharField(max_length=100)
    geom = models.TextField() #models.MultiPolygonField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return nombre

class TerritorioPolitico(Territorio):

    class Meta:
        abstract = True

class Departamento(TerritorioPolitico):
    pass

#TO-DO relacionar prueblos
class Pueblo(models.Model):
    nombre = CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

class Poblacion(models.Model):
    cantidad_hombres = SmallIntegerField()
    cantidad_mujeres = SmallIntegerField()
    edad_0_5 = SmallIntegerField(verbose_name="Entre 0 y 5", default=0)
    edad_6_10 = SmallIntegerField(verbose_name="Entre 6 y 10", default=0)
    edad_11_15 = SmallIntegerField(verbose_name="Entre 11 y 15", default=0)
    edad_16_20 = SmallIntegerField(verbose_name="Entre 16 y 20", default=0)
    edad_21_25 = SmallIntegerField(verbose_name="Entre 21 y 25", default=0)
    edad_26_30 = SmallIntegerField(verbose_name="Entre 26 y 30", default=0)
    edad_31_35 = SmallIntegerField(verbose_name="Entre 31 y 35", default=0)
    edad_36_40 = SmallIntegerField(verbose_name="Entre 36 y 40", default=0)
    edad_41_45 = SmallIntegerField(verbose_name="Entre 41 y 45", default=0)
    edad_46_50 = SmallIntegerField(verbose_name="Entre 46 y 50", default=0)
    edad_51_55 = SmallIntegerField(verbose_name="Entre 51 y 55", default=0)
    edad_56_60 = SmallIntegerField(verbose_name="Entre 56 y 60", default=0)
    edad_61_65 = SmallIntegerField(verbose_name="Entre 61 y 65", default=0)
    edad_66_70 = SmallIntegerField(verbose_name="Entre 66 y 70", default=0)
    edad_71_75 = SmallIntegerField(verbose_name="Entre 71 y 75", default=0)
    edad_76_80 = SmallIntegerField(verbose_name="Entre 76 y 80", default=0)
    edad_81_85 = SmallIntegerField(verbose_name="Entre 81 y 85", default=0)
    edad_86_90 = SmallIntegerField(verbose_name="Entre 86 y 90", default=0)
    edad_91_95 = SmallIntegerField(verbose_name="Entre 91 y 95", default=0)
    porcentaje_pueblos = SmallIntegerField()

    def __unicode__(self):
        return 'Hombres: %s, Mujeres: %s, Pueblos: %s %' % (self.cantidad_hombres, self.cantidad_mujeres, self.porcentaje_pueblos)

"""
    Cantidad de comunidades, asentamientos
    Nombre de comunidades, asentamientos
"""
class Asentamiento(models.Model):
    nombre = CharField(max_length=100)
    fecha_creacion = DateField()
    decha_disolucion = DateField(null=True, blank=True)

class Municipio(TerritorioPolitico):
    departamento = models.ForeignKey(Departamento)
    tipo = SmallIntegerField(choices=TIPOS_MUNICIPIO, default=0)
    fecha_creacion = DateField(null=True, blank=True)

    presupuesto_anual = IntegerField()
    

class Limite(models.Model):
    municipio = ForeignKey(Municipio, related_name='limites')
    tipo = SmallIntegerField(choices=TIPOS_LIMITE, default=0)
    #puntos?
    
class TerritorioComunidad(Territorio): 
    departamento = models.ForeignKey(Departamento)
    asentamientos = ManyToManyField(Asentamiento)
    poblacion_total = ForeignKey(Poblacion)

    class Meta:
        abstract = True

class SituacionJuridicaTitulacion(models.Model):
    resolucion_fecha = DateField()
    resolucion_codigo = CharField(max_length=50)
    limites = CharField(max_length=255) #gis?
    estado_tramite = CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')

class SituacionJuridicaAmpliacionSanamiento(models.Model):
    ampliacion_resolucion_fecha = DateField()
    ampliacion_resolucion_codigo = CharField(max_length=50)
    ampliacion_limites = CharField(max_length=255) #gis?
    ampliacion_estado_tramite = CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')

    saneamiento_resolucion_fecha = DateField()
    saneamiento_resolucion_codigo = CharField(max_length=50)
    saneamiento_area = CharField(max_length=255) #gis?
    saneamiento_poblacion_general = IntegerField()
    saneamiento_poblacion_afro = IntegerField()
    saneamiento_poblacion_otros = IntegerField()
    saneamiento_limites = CharField(max_length=255) #gis?
    saneamiento_estado_tramite = CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')

class TerritorioIndio(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='indio_municipio')
    pueblos = ManyToManyField(Pueblo)
    resolucion_constitucion = models.IntegerField()
    area = CharField(max_length=255) #gis?
    limites = CharField(max_length=255) #gis?

    situacion_juridica = ForeignKey(SituacionJuridicaAmpliacionSanamiento)

class TerritorioIndioNoTitulado(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='indio_not_municipio')
    pueblos = ManyToManyField(Pueblo)
    area_solicitada = CharField(max_length=255) #gis?
    situacion_juridica = ForeignKey(SituacionJuridicaTitulacion)


class TerritorioNegro(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='negro_municipio')
    resolucion_constitucion = models.IntegerField()
    area = CharField(max_length=255) #gis?
    limites = CharField(max_length=255) #gis?

class TerritorioNegroNoTitulado(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='negro_not_municipio')
    area_solicitada = CharField(max_length=255) #gis?
    situacion_juridica = ForeignKey(SituacionJuridicaTitulacion)