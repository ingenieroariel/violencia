# -*- coding: utf-8 -*-
from django.db.models.fields import BooleanField
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField
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
TIPOS_MUNICIPIO = ((0,'Fronterizo'),(1,u'Costero'),(2,'Rivereño'),(3,'Del Interior'))
TIPOS_LIMITE = ((0,'Departamento'),(1,'Pais'),(2,'Municipios'),(3,'Comunidades'))
GRUPOS_POBLACIONAL = (('I','Indigena'),('A',u'Afro'), ('O','Otros'))

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

class PoblacionGrande(models.Model):
    total = SmallIntegerField(verbose_name="Población Total", default=0)
    porcentaje_hombres = SmallIntegerField()
    cantidad_mujeres = IntegerField()
    edad_0_9 = SmallIntegerField(verbose_name="Porcentaje de edad entre 0 y 9", default=0)
    edad_10_19 = SmallIntegerField(verbose_name="Edad entre 10 y 19", default=0)
    edad_20_29 = SmallIntegerField(verbose_name="Edad entre 20 y 29", default=0)
    edad_30_39 = SmallIntegerField(verbose_name="Edad entre 30 y 39", default=0)
    edad_40_49 = SmallIntegerField(verbose_name="Edad entre 40 y 49", default=0)
    edad_50_59 = SmallIntegerField(verbose_name="Edad entre 50 y 59", default=0)
    edad_60_69 = SmallIntegerField(verbose_name="Edad entre 60 y 69", default=0)
    edad_70_79 = SmallIntegerField(verbose_name="Edad entre 70 y 79", default=0)
    edad_80_89 = SmallIntegerField(verbose_name="Edad entre 80 y 89", default=0)
    porcentaje_indigena = SmallIntegerField(verbose_name="Porcentaje indigenas")
    cantidad_afro = IntegerField()
    cantidad_otros = IntegerField()
    cantidad_no_informa = IntegerField()
    cantidad_cabecera = IntegerField(verbose_name='Cabecera (No.)')
    cantidad_rural = IntegerField()


class Desplazados(models.Model):
    cantidad_total = SmallIntegerField()
    cantidad_hombres = SmallIntegerField()
    cantidad_mujeres = SmallIntegerField()
    edad_0_5 = SmallIntegerField(verbose_name="Edad entre 0 y 5", default=0)
    edad_6_10 = SmallIntegerField(verbose_name="Edad entre 6 y 10", default=0)
    edad_11_15 = SmallIntegerField(verbose_name="Edad entre 11 y 15", default=0)
    edad_16_20 = SmallIntegerField(verbose_name="Edad entre 16 y 20", default=0)
    edad_21_25 = SmallIntegerField(verbose_name="Edad entre 21 y 25", default=0)
    edad_26_30 = SmallIntegerField(verbose_name="Edad entre 26 y 30", default=0)
    edad_31_35 = SmallIntegerField(verbose_name="Edad entre 31 y 35", default=0)
    edad_36_40 = SmallIntegerField(verbose_name="Edad entre 36 y 40", default=0)
    edad_41_45 = SmallIntegerField(verbose_name="Edad entre 41 y 45", default=0)
    edad_46_50 = SmallIntegerField(verbose_name="Edad entre 46 y 50", default=0)
    edad_51_55 = SmallIntegerField(verbose_name="Edad entre 51 y 55", default=0)
    edad_56_60 = SmallIntegerField(verbose_name="Edad entre 56 y 60", default=0)
    edad_61_65 = SmallIntegerField(verbose_name="Edad entre 61 y 65", default=0)
    edad_66_70 = SmallIntegerField(verbose_name="Edad entre 66 y 70", default=0)
    edad_71_75 = SmallIntegerField(verbose_name="Edad entre 71 y 75", default=0)
    edad_76_80 = SmallIntegerField(verbose_name="Edad entre 76 y 80", default=0)
    edad_81_85 = SmallIntegerField(verbose_name="Edad entre 81 y 85", default=0)
    edad_86_90 = SmallIntegerField(verbose_name="Edad entre 86 y 90", default=0)
    edad_91_95 = SmallIntegerField(verbose_name="Edad entre 91 y 95", default=0)
    cantidad_indigena = SmallIntegerField(verbose_name="Porcentaje indigenas")
    cantidad_afro = IntegerField()
    cantidad_otros = IntegerField()
    cantidad_no_informa = IntegerField()
    cantidad_individual = IntegerField()
    cantidad_cabecera = IntegerField(verbose_name='Cabecera (No.)')
    cantidad_rural = IntegerField()

class RecepcionDesplazados(Desplazados):
    pass

class ExpulsionDesplazados(Desplazados):
    pass
    
class PlanDesarrollo(models.Model):
    existe_plan_desarrollo = BooleanField(default=False)
    periodo = CharField(null=True, blank=True, max_length=255)

    
class IngresoDepartamental(models.Model):
    pass
#   """Ingresos totales"""
#   """ Ingresos Corrientes"""
#   """  Tributarios"""
#    cerveza
#    licores
#    cigarillos_Tabaco
#    registro_anotacion
#    vehiculos_automotores
#    otros
#    """  No Tributarios"""
#    """  Transferencias Corrientes"""
#    del_nivel_nacional
#    otras
#
#    """Gastos totales"""
#    """ Gastos corrientes"""
#    """   Funcionamiento"""
#    servicios_personales
#    gastos_generales
#    transferencias (Nomina y a Entidades)
#    """   Intereses de Deuda Pública"""
#    externa
#    interna
#
#    #(Deficit)/Ahorro Corriente ?? """
#    """Ingresos de Capital"""
#    """ Transferencias"""
#    del_nivel_nacional
#    otras
#
#    cofinanciacion
#    regalias
#    otros
#
#    """Gastos de Capital"""
#    formacion_bruta_capital_fijo
#    inversion_social
#    transferencias_capital
#    otros
#
#    #(Deficit)/Superavit total ??
#
#    """Financiamiento"""
#    """ Credito externo neto"""
#    desembolsos (+)
#    amortizaciones (-)
#    """Credito interno neto"""
#    desembolsos (+)
#    amortizaciones (-)
#
#    variacion_depositos_y_otros


class Departamento(TerritorioPolitico):
    tipo = SmallIntegerField(choices=TIPOS_MUNICIPIO, default=0)
    """Área total"""
    area_total_urbana = TextField()
    area_total_rural = TextField()

    capital = CharField(max_length=255)
    cantidad_municipios_total = IntegerField()
    cantidad_municipios_pacifico = IntegerField()
    fecha_creacion = DateField()

    presupuesto_anual = IntegerField()
    ingresos = ForeignKey(IngresoDepartamental)

    poblacion = ForeignKey(PoblacionGrande)

    recepcion_desplazados = ForeignKey(RecepcionDesplazados)
    expulsion_desplazados = ForeignKey(ExpulsionDesplazados)

    capital_area = CharField(max_length=255)
    rural_area = CharField(max_length=255)

    plan_desarrollo = ForeignKey(PlanDesarrollo)




#TO-DO relacionar prueblos
class Pueblo(models.Model):
    nombre = CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

class PoblacionPequena(models.Model):
    cantidad_hombres = SmallIntegerField()
    cantidad_mujeres = SmallIntegerField()
    edad_0_5 = SmallIntegerField(verbose_name="Edad entre 0 y 5", default=0)
    edad_6_10 = SmallIntegerField(verbose_name="Edad entre 6 y 10", default=0)
    edad_11_15 = SmallIntegerField(verbose_name="Edad entre 11 y 15", default=0)
    edad_16_20 = SmallIntegerField(verbose_name="Edad entre 16 y 20", default=0)
    edad_21_25 = SmallIntegerField(verbose_name="Edad entre 21 y 25", default=0)
    edad_26_30 = SmallIntegerField(verbose_name="Edad entre 26 y 30", default=0)
    edad_31_35 = SmallIntegerField(verbose_name="Edad entre 31 y 35", default=0)
    edad_36_40 = SmallIntegerField(verbose_name="Edad entre 36 y 40", default=0)
    edad_41_45 = SmallIntegerField(verbose_name="Edad entre 41 y 45", default=0)
    edad_46_50 = SmallIntegerField(verbose_name="Edad entre 46 y 50", default=0)
    edad_51_55 = SmallIntegerField(verbose_name="Edad entre 51 y 55", default=0)
    edad_56_60 = SmallIntegerField(verbose_name="Edad entre 56 y 60", default=0)
    edad_61_65 = SmallIntegerField(verbose_name="Edad entre 61 y 65", default=0)
    edad_66_70 = SmallIntegerField(verbose_name="Edad entre 66 y 70", default=0)
    edad_71_75 = SmallIntegerField(verbose_name="Edad entre 71 y 75", default=0)
    edad_76_80 = SmallIntegerField(verbose_name="Edad entre 76 y 80", default=0)
    edad_81_85 = SmallIntegerField(verbose_name="Edad entre 81 y 85", default=0)
    edad_86_90 = SmallIntegerField(verbose_name="Edad entre 86 y 90", default=0)
    edad_91_95 = SmallIntegerField(verbose_name="Edad entre 91 y 95", default=0)
    porcentaje_pueblos = SmallIntegerField()

    def __unicode__(self):
        return 'Hombres: %s, Mujeres: %s, Pueblos: %s %' % (self.cantidad_hombres, self.cantidad_mujeres, self.porcentaje_pueblos)


class IngresoMunicipal(models.Model):
    """Ingresos totales"""
    """ Ingresos corrientes"""
    """  Ingresos tributarios"""
    predial = IntegerField()
    industria_comercio = IntegerField()
    otros_ingresos = IntegerField()
    """ Ingresos no tributarios"""
    """  Transferencias"""
    del_nivel_nacional = IntegerField()
    otras_transferencias = IntegerField()

    """Gastos totales"""
    """ Gastos corrientes"""
    """  Funcionamiento"""
    servicios_personales = IntegerField()
    gastos_generales = IntegerField()
    transferencias_pagadas = IntegerField(verbose_name='Transferencias pagadas (nomina y entidades)')
    intereses_deuda_publica = IntegerField()
    otros_gastos_corrientes = IntegerField()
    deficit_o_ahorro_corriente = IntegerField(choices=((1,'Deficit'),(2,'Ahorro corriente')))
    """  Ingresos de capital"""
    regalias = IntegerField()
    transferencias_nacionales = IntegerField()
    cofinanciacion = IntegerField()
    otros_ingresos_capital = IntegerField()
    """Gastos de capital (inversion)"""
    formacion_brutal_capital_fijo = IntegerField()
    resto_inversiones = IntegerField()

    deficit_o_superavit_total = IntegerField()
    """Financiamiento"""
    credito_interno = IntegerField()
    credito_externo = IntegerField()
    desembolsos = IntegerField()
    amortizaciones = IntegerField()
    """Recursos balance, var. depositos, otros ??"""

"""Plan de ordenamiento (Ley 388 de 1997, Titulo 1, Art 15)"""
class PlanOrdenamiento(models.Model):
    fecha = DateField()
    """Area urbana"""
    suelo_urbano_area = TextField() #gis?
    suelo_urbano_limite = TextField() #gis?
    """Expansión urbana"""
    expansion_urbana_area = TextField() #gis?
    expansion_urbana_limite = TextField(verbose_name='Expansión Urbana Limite (Proyección)') #gis?

    """Area rural"""
    prod_agropecuaria_area  = TextField() #gis?
    prod_agropecuaria_limite  = TextField() #gis?

    """Area o sistema ambiental (bosque protector, importancia ambiental)"""
    sistema_ambiental_area  = TextField() #gis?
    sistema_ambiental_limites  = TextField() #gis?

    sistema_silvo_pastorial_area = TextField() #gis?
    sistema_silvo_pastorial_limites = TextField() #gis?

    sistema_forestal_area = TextField() #gis?
    sistema_forestal_limites = TextField() #gis?

    zonas_vida_area = TextField() #gis?
    zonas_vida_limites = TextField() #gis?

    cuencas_hidrograficas_area = TextField() #gis?
    cuencas_hidrograficas_limite = TextField() #gis?

    uso_cobertura_vegetal_tipo = TextField() #gis?
    uso_cobertura_vegetal_area = TextField() #gis?

    area_rutal_suelos_tipos = TextField() #gis?

    riesgos_amenazas_ubicacion = TextField() #gis?
    riesgos_amenazas_descripcion = TextField() #gis?

    mapa_politico_administrativo = FileField(upload_to='/')
    mapa_uso_generales_del_suelo = FileField(upload_to='/')


"""
    Cantidad de comunidades, asentamientos
    Nombre de comunidades, asentamientos
"""
class Asentamiento(models.Model):
    nombre = CharField(max_length=100)
    fecha_creacion = DateField()
    decha_disolucion = DateField(null=True, blank=True)

    def __unicode__(self):
        return self.nombre
    

class Municipio(TerritorioPolitico):
    departamento = models.ForeignKey(Departamento)
    tipo = SmallIntegerField(choices=TIPOS_MUNICIPIO, default=0)
    fecha_creacion = DateField(null=True, blank=True)

    presupuesto_anual = IntegerField()
    ingresos = ForeignKey(IngresoMunicipal)
    poblacion = ForeignKey(PoblacionGrande)
    recepcion_desplazados = ForeignKey(RecepcionDesplazados)
    expulsion_desplazados = ForeignKey(ExpulsionDesplazados)

    area = IntegerField(verbose_name='Área (km2) total')
    """Cabecera municipal"""
    """ Títulos individuales"""
    cabecera_individuales_cantidad = IntegerField()
    cabecera_area = CharField(max_length=255)
    cabecera_grupo_poblacional = CharField(max_length=2, choices=GRUPOS_POBLACIONAL)

    """Rural"""
    """ Títulos individuales"""
    rural_individuales_cantidad = IntegerField()
    rural_area = CharField(max_length=255)
    rural_grupo_poblacional = CharField(max_length=2, choices=GRUPOS_POBLACIONAL)

    plan_ordenamiento = ForeignKey(PlanOrdenamiento)
    plan_desarrollo = ForeignKey(PlanDesarrollo)


class Limite(models.Model):
    tipo = SmallIntegerField(choices=TIPOS_LIMITE, default=0)
    #puntos?

    class Meta:
        abstract = True

class LimiteMunicipio(Limite):
    municipio = ForeignKey(Municipio, related_name='limites')
    
class LimiteDepartamento(Limite):
    departamento = ForeignKey(Departamento, related_name='limites')

class TerritorioComunidad(Territorio): 
    departamento = models.ForeignKey(Departamento)
    asentamientos = ManyToManyField(Asentamiento)
    poblacion_total = ForeignKey(PoblacionPequena)

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
