# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields import CharField
from django.db.models.fields import DateField
from django.db.models.fields import IntegerField
from django.db.models.fields import SmallIntegerField
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.related import ManyToManyField
from violencia.territorios.utils import gen_rangos_cantidad
from django_extensions.db.fields import ModificationDateTimeField
from django_extensions.db.fields import CreationDateTimeField

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
TIPOS_ETNICOS = (('INTRA','Intraétnico'),('INTER','Interétnico'))
TIPOS_CONFICTO = ( (0,'Cultural'), (1,'Político'), (2,'Económico'), (3,'Recursos Naturales'), (4,'Territorial'), (5,'Otros') )
TIPOS_SERVICIOS_PUBLICOS = ( (0, 'Acueducto'), (1, 'Alcantarillado'), (2, 'Energia') )
TIPOS_INSTITUCION = ((0,'Publica'),(1,'Privada'))
TIPOS_CONTRATO = ((0,'Temporal'),(1,'Fijo'))
TIPOS_INSTALACIONES_SALUD = ((0,'Centro de salud'),(1,'Puesto de salud'),(2,'Hospital') )
TIPOS_REGIMEN = ((0,'Subsidiario'),(1,'Contributivo'))

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

    class Meta:
        abstract = True

class RecepcionDesplazados(Desplazados):
    pass

class ExpulsionDesplazados(Desplazados):
    pass

class PlanDesarrollo(models.Model):
    existe_plan_desarrollo = BooleanField(default=False)
    periodo = CharField(null=True, blank=True, max_length=255)


class IngresoDepartamental(models.Model):
    """Ingresos totales"""
    """ Ingresos Corrientes"""
    """  Tributarios"""
    ingreso_tributario_cerveza = IntegerField()
    ingreso_tributario_licores = IntegerField()
    ingreso_tributario_cigarillos_Tabaco = IntegerField()
    ingreso_tributario_registro_anotacion = IntegerField()
    ingreso_tributario_vehiculos_automotores = IntegerField()
    ingreso_tributario_otros = IntegerField()
    """  No Tributarios"""
    """  Transferencias Corrientes"""
    ingreso_no_tributario_nivel_nacional = IntegerField()
    ingreso_no_tributario_otras = IntegerField()

    """Gastos totales"""
    """ Gastos corrientes"""
    """   Funcionamiento"""
    gastos_servicios_personales = IntegerField()
    gastos_generales = IntegerField()
    gastos_transferencias = IntegerField(verbose_name='Gastos Transferencias (Nomina y a Entidades)')
    """   Intereses de Deuda Pública"""
    intereses_deuda_externa = IntegerField()
    intereses_deuda_interna = IntegerField()

    #(Deficit)/Ahorro Corriente ?? """
    """Ingresos de Capital"""
    """ Transferencias"""
    transferencias_nivel_nacional = IntegerField()
    transferencias_otras = IntegerField()

    ingresos_capital_cofinanciacion = IntegerField()
    ingresos_capital_regalias = IntegerField()
    ingresos_capital_otros = IntegerField()

    """Gastos de Capital"""
    gastos_capital_formacion_bruta_capital_fijo = IntegerField()
    gastos_capital_inversion_social = IntegerField()
    gastos_capital_transferencias_capital = IntegerField()
    gastos_capital_otros = IntegerField()

    #(Deficit)/Superavit total ??

    """Financiamiento"""
    """ Credito externo neto"""
    credito_externo_desembolsos = IntegerField(verbose_name='Credito externo desembolsos (+)')
    credito_externo_amortizaciones = IntegerField(verbose_name='Credito externo amortizaciones (-)')
    """Credito interno neto"""
    credito_interno_desembolsos = IntegerField(verbose_name='Credito interno desembolsos (+)')
    credito_interno_amortizaciones = IntegerField(verbose_name='Credito interno amortizaciones (-)')

    variacion_depositos_y_otros = IntegerField()


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

class Titulacion(models.Model):
    resolucion_fecha = DateField()
    resolucion_codigo = CharField(max_length=50)
    limites = CharField(max_length=255) #gis?
    estado_tramite = CharField(max_length=2, choices=ESTADOS_TRAMITES_JURIDICOS, default='S')

class Saneamiento(models.Model):
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

    situacion_juridica = ForeignKey(Saneamiento)

class TerritorioIndioNoTitulado(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='indio_not_municipio')
    pueblos = ManyToManyField(Pueblo)
    area_solicitada = CharField(max_length=255) #gis?
    situacion_juridica = ForeignKey(Titulacion)


class TerritorioNegro(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='negro_municipio')
    resolucion_constitucion = models.IntegerField()
    area = CharField(max_length=255) #gis?
    limites = CharField(max_length=255) #gis?

class TerritorioNegroNoTitulado(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='negro_not_municipio')
    area_solicitada = CharField(max_length=255) #gis?
    situacion_juridica = ForeignKey(Titulacion)


"""CATEGORÍA: CONFLICTOS"""
"""(Información solo accesible para las organizaciones que la cargan y para el Observatorio. NO pública)"""

""" Maybe a new app? """

class Conflicto(models.Model):
    tipo_etnico = CharField(max_length=100, choices=TIPOS_ETNICOS )
    tipo_conflicto = IntegerField(choices=TIPOS_CONFICTO)
    """Descripción"""
    ubicacion = CharField(max_length=200)
    actores = CharField(max_length=200)
    hechos = CharField(max_length=200)
    estado = CharField(max_length=200)
    fecha = DateField()
    fuente = CharField(max_length=200)

    #Audit fields
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    created_by = ForeignKey(User, related_name='conflictos_creados')
    modified_by = ForeignKey(User, related_name='conflictos_modificados')


class PoblacionDesc(models.Model):
    porcentaje = CharField(max_length=255)
    rango = CharField(max_length=255)
    hombres = CharField(max_length=255)
    mujeres = CharField(max_length=255)
    indigena = CharField(max_length=255)
    afro = CharField(max_length=255)
    otros = CharField(max_length=255)
    class Meta:
        abstract = True

class EsperanzaVida(PoblacionDesc):
    total = IntegerField()

class MortalidadTotal(PoblacionDesc):
    total = IntegerField()

class MortalidadInfantil(PoblacionDesc):
    total = IntegerField()

class MortalidadMaternoInfantil(PoblacionDesc):
    total = IntegerField()

class TasaAnalfabetizacion(PoblacionDesc):
    todos_total  = CharField(max_length=255)
    todos_porcentaje = CharField(max_length=255)
    todos_rango = CharField(max_length=255)
    rural_porcentaje = CharField(max_length=255)
    rural_rango = CharField(max_length=255)
    urbano_porcentaje = CharField(max_length=255)
    urbano_rango = CharField(max_length=255)

class Matriculas(PoblacionDesc):
    total = IntegerField()


class EducacionPreescolar(PoblacionDesc):
    total = IntegerField()

class EducacionPrimaria(PoblacionDesc):
    total = IntegerField()

class EducacionSecundaria(PoblacionDesc):
    total = IntegerField()

class EducacionVocacional(PoblacionDesc):
    total = IntegerField()

class EducacionTecnica(PoblacionDesc):
    total = IntegerField()

class EducacionNormalista(PoblacionDesc):
    total = IntegerField()

class EducacionTecnicaTecnologica(PoblacionDesc):
    total = IntegerField()

class EducacionSuperior(PoblacionDesc):
    total = IntegerField()

class PoblacionEstudiantilPreescolar(PoblacionDesc):
    total = IntegerField()

class PoblacionEstudiantilBasicaPrimaria(PoblacionDesc):
    total = IntegerField()

class PoblacionEstudiantilBasicaSecundaria(PoblacionDesc):
    total = IntegerField()

class PoblacionEstudiantilMediaVocacional(PoblacionDesc):
    total = IntegerField()

class CoberturaEstudiantilPreescolar(PoblacionDesc):
    total = IntegerField()

class CoberturaEstudiantilBasicaPrimaria(PoblacionDesc):
    total = IntegerField()

class CoberturaEstudiantilBasicaSecundaria(PoblacionDesc):
    total = IntegerField()

class CoberturaEstudiantilMediaVocacional(PoblacionDesc):
    total = IntegerField()

class CoberturaDesplazadosPreescolar(PoblacionDesc):
    total = IntegerField()

class CoberturaDesplazadosPrimaria(PoblacionDesc):
    total = IntegerField()

class CoberturaDesplazadosSecundaria(PoblacionDesc):
    total = IntegerField()

class CoberturaDesplazadosMedia(PoblacionDesc):
    total = IntegerField()

class EstudiantesDesercion(PoblacionDesc):
    total = IntegerField()

class EstudiantesPromocion(PoblacionDesc):
    total = IntegerField()

class EstudiantesRepitencia(PoblacionDesc):
    total = IntegerField()

class EstudiantesAnalfabetismo(PoblacionDesc):
    total = IntegerField()

class InstitucionEducativa(models.Model):
    nombre = CharField(max_length=255)
    institucion = IntegerField(choices=TIPOS_INSTITUCION)
    fecha_constitucion = DateField()
    enfasis = CharField(max_length=255)
    etnoeducacion_en_pei = BooleanField()
    educacion_especial = BooleanField()
    educacion_especial_porcentaje = IntegerField()
    educacion_adultos = BooleanField()
    educacion_adultos_porcentaje = IntegerField()

    maestros_nombrados_total = IntegerField()
    maestros_nombrados_indigenas = IntegerField()
    maestros_nombrados_afro = IntegerField()
    maestros_nombrados_otros = IntegerField()
    maestros_nombrados_en_ejercicio = IntegerField()
    maestros_temporales_total = IntegerField()
    maestros_temporales_indigena = IntegerField()
    maestros_temporales_afro = IntegerField()
    maestros_temporales_otros = IntegerField()
    maestros_temporales_en_ejercicio = IntegerField()
    poblacion_preescolar = ForeignKey(PoblacionEstudiantilPreescolar)
    poblacion_basica_primaria = ForeignKey(PoblacionEstudiantilBasicaPrimaria)
    poblacion_basica_secundaria = ForeignKey(PoblacionEstudiantilBasicaSecundaria)
    poblacion_media_vocacional = ForeignKey(PoblacionEstudiantilMediaVocacional)
    cobertura_preescolar = ForeignKey(CoberturaEstudiantilPreescolar)
    cobertura_basica_primaria = ForeignKey(CoberturaEstudiantilBasicaPrimaria)
    cobertura_basica_secundaria = ForeignKey(CoberturaEstudiantilBasicaSecundaria)
    cobertura_media_vocacional = ForeignKey(CoberturaEstudiantilMediaVocacional)
    cobertura_desplazados_preescolar = ForeignKey(CoberturaDesplazadosPreescolar)
    cobertura_desplazados_basica_primaria = ForeignKey(CoberturaDesplazadosPrimaria)
    cobertura_desplazados_basica_secundaria = ForeignKey(CoberturaDesplazadosSecundaria)
    cobertura_desplazados_media_vocacional = ForeignKey(CoberturaDesplazadosMedia)
    promocion = ForeignKey(EstudiantesPromocion)
    desercion = ForeignKey(EstudiantesDesercion)
    repitencia = ForeignKey(EstudiantesRepitencia)
    analfabetismo = ForeignKey(EstudiantesAnalfabetismo)

class EntidadContratante(models.Model):
    nombre = CharField(max_length=255)


class Promotores(models.Model):
    entidades = ManyToManyField(EntidadContratante)
    tipo_contrato = IntegerField(choices=TIPOS_CONTRATO)

class Instalaciones(models.Model):
    tipo = IntegerField()
    ubicacion = CharField(max_length=255)
    nivel_de_atencion = CharField(max_length=255)

class EmpresaPrestadoraRegimenSubsidiario(models.Model):
    nombre = CharField(max_length=255)

class Regimen(models.Model):
    tipo = IntegerField(choices=TIPOS_REGIMEN)
    tipo_poblacion = IntegerField(choices=GRUPOS_POBLACIONAL)
    porcentaje = IntegerField()
    empresas = ManyToManyField(EmpresaPrestadoraRegimenSubsidiario)
    
class SistemaSalud(models.Model):
    promotores = ManyToManyField(Promotores)
    instalaciones = ManyToManyField(Instalaciones)
    regimenes = ManyToManyField(Regimen)

class ICBF(models.Model):
    poblacion_indigena_infantil_cobertura = IntegerField()
    poblacion_indigena_infantil_monto = IntegerField()
    poblacion_indigena_infantil_duracion = IntegerField()

    poblacion_indigena_escolar_duracion = IntegerField()
    poblacion_indigena_escolar_cobertura = IntegerField()
    poblacion_indigena_escolar_monto = IntegerField()

    poblacion_indigena_madres_duracion = IntegerField()
    poblacion_indigena_madres_cobertura = IntegerField()
    poblacion_indigena_madres_monto = IntegerField()

    poblacion_indigena_discapacitada_monto = IntegerField()
    poblacion_indigena_discapacitada_cobertura = IntegerField()
    poblacion_indigena_discapacitada_duracion = IntegerField()

    poblacion_indigena_abandono_duracion = IntegerField()
    poblacion_indigena_abandono_monto = IntegerField()
    poblacion_indigena_abandono_cobertura = IntegerField()

    poblacion_indigena_otro_cobertura = IntegerField()
    poblacion_indigena_otro_monto = IntegerField()
    poblacion_indigena_otro_duracion = IntegerField()

    poblacion_afro_infantil_cobertura = IntegerField()
    poblacion_afro_madres_cobertura = IntegerField()
    poblacion_afro_otros_cobertura = IntegerField()
    poblacion_afro_escolar_cobertura = IntegerField()

    poblacion_otro_infantil_cobertura = IntegerField()
    poblacion_otro_madres_cobertura = IntegerField()
    poblacion_otro_otros_cobertura = IntegerField()
    poblacion_otro_escolar_cobertura = IntegerField()

class Economia(models.Model):
    desempleo_informal  = IntegerField()
    desempleo_formal = IntegerField()
    empleo_publico = IntegerField()
    empleo_privado = IntegerField()
    contrato_fijo = IntegerField()
    contrato_temporal = IntegerField()

class Cultura(models.Model):
    existe_promocion_y_proteccion_lengua_indigena = BooleanField()
    descripcion_promocion_y_proteccion_lengua_indigena = TextField()

class Desc(models.Model):
    ingresos_publicos_valor = CharField(max_length=100)
    ingresos_publicos_rango = CharField(max_length=100)

    indice_desarrollo_porcentaje  = CharField(max_length=100)
    indice_desarrollo_rango  = CharField(max_length=100)

    necesidades_insatisfechas_total = CharField(max_length=100)
    necesidades_insatisfechas_porcentaje = CharField(max_length=100)
    necesidades_insatisfechas_rango = CharField(max_length=100)
    necesidades_insatisfechas_total_rural = CharField(max_length=100)
    necesidades_insatisfechas_porcentaje_rural = CharField(max_length=100)
    necesidades_insatisfechas_rango_rutal = CharField(max_length=100)
    necesidades_insatisfechas_total_urbano = CharField(max_length=100)
    necesidades_insatisfechas_porcentaje_urbano = CharField(max_length=100)
    necesidades_insatisfechas_rango_urbano = CharField(max_length=100)

    indice_condiciones_vida_porcentaje = CharField(max_length=100)
    indice_condiciones_vida_rango = CharField(max_length=100)

    esperanza_de_vida = ForeignKey(EsperanzaVida)
    mortalidad_total = ForeignKey(MortalidadTotal)
    mortalidad_infantil = ForeignKey(MortalidadInfantil)
    mortalidad_materno_infantil = ForeignKey(MortalidadMaternoInfantil)
    morbilidad_descripcion  = CharField(max_length=255)
    morbilidad_porcentaje = CharField(max_length=255)
    morbi_mortalidad_descripcion = CharField(max_length=255)
    morbi_mortalidad_porcentaje = CharField(max_length=255)
    tasa_analfabetizacion = ForeignKey(TasaAnalfabetizacion)
    matricula = ForeignKey(Matriculas)

    educacion_preescolar = ForeignKey(EducacionPreescolar)
    educacion_basica_primaria = ForeignKey(EducacionPrimaria)
    educacion_basica_secundaria = ForeignKey(EducacionSecundaria)
    educacion_media_vocacional = ForeignKey(EducacionVocacional)
    educacion_media_tecnica = ForeignKey(EducacionTecnica)
    educacion_normalista = ForeignKey(EducacionNormalista)
    educacion_tecnica_tecnologica = ForeignKey(EducacionTecnicaTecnologica)
    educacion_superior = ForeignKey(EducacionSuperior)

    instituciones_educativas_cabecera = ManyToManyField(InstitucionEducativa, related_name='descs_cabecera')
    instituciones_educativas_rural = ManyToManyField(InstitucionEducativa, related_name='descs_rural')

    sistema_salud = ForeignKey(SistemaSalud)
    icbf = ForeignKey(ICBF)
    economia = ForeignKey(Economia)
    cultura = ForeignKey(Cultura)
    
class ServicioPublico(models.Model):
    desc = ForeignKey(Desc, related_name='servicios_publicos')
    nombre = CharField(max_length=200, choices=TIPOS_SERVICIOS_PUBLICOS)
    cobertura_total = IntegerField()

class CoberturaServicioPublico(models.Model):
    servicio_publico = ForeignKey(ServicioPublico, related_name='cobertura')
    lugar = CharField(max_length=100, choices=(('r','Rural'),('u','Urbano')) )
    porcentaje = IntegerField()
    rango = CharField(max_length=100)


