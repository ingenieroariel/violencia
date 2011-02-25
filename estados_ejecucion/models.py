# -*- coding: utf-8 -*-
from django.db import models
from megaproyectos.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato

#STACKED INLINES GENERICAS

OPCIONES_ESTADOS_EJECUCION = (
    ("Cesion-completa","Cesión completa"),
    ("Cesion-parcial","Cesión parcial"),
    ("Suspension","Suspensión"),
    ("Revocatoria","Revocatoria"),
    ("Perdida-de-vigencia-de-la-Licencia-Ambiental","Perdida de vigencia de la Licencia Ambiental"),
    ("Integracion-de-dos-Licencias-Ambientales","Integración de dos Licencias Ambientales"),
)

IMPACTOS = (
    ("ambientales","Impacto Ambiental"),
    ("culturales","Impactos culturales"),
    ("economicos","Impactos económicos"),
    ("sociales","Impactos sociales"),
    ("organizaciones","Impactos en las organizaciones"),
)

IMPACTOS2 = (
    ("ia-suelos","Suelos"),
    ("ia-rios","Rios"),
    ("ia-quebradas","Quebradas"),
    ("ia-cultivos","Cultivos"),
    ("ia-bosques","Bosques"),
    ("ia-manglares","Manglares"),
    ("ia-payas","Payas"),
    ("ia-nacimiento-agua","Nacimiento de agua"),
    ("ia-fauna","Fauna"),
    ("ia-aire","Aire"),
    ("ia-ruido","Ruido"),
    ("ia-otro","Otro"),
    ("ic-autoridad","Forma de autoridad"),
    ("ic-fiestas","Fiestas"),
    ("ic-lenguas","Lengua"),
    ("ic-comida","Comida"),
    ("ic-cambios","Cambios de proyecto de vida"),
    ("ic-otro","Otro"),
    ("ie-ingreso","Ingreso"),
    ("ie-relaciones","Relaciones laborales"),
    ("ie-sistema","Sistema productivo"),
    ("ie-otro","Otro"),
    ("is-socuales","Salud"),
    ("is-edicacion","Educación"),
    ("is-cambio-roles","Cambio de roles"),
    ("is-movilidad","Movilidad de la población"),
    ("is-interecnicos","Conflictos - Interetnicos"),
    ("is-intraecnicos","Conflictos - Intraetnicos"),
    ("is-otros-actores","Conflictos - Otros actores"),
    ("is-otros","Otro"),
    ("io-division","División"),
    ("io-cambios","Cambios de objetivos"),
    ("io-corrupcion","Corrupción"),
    ("io-perdida","Perdida de legitimidad"),
    ("io-otro","Otro"),
)

ACCIONES_SEGUIMIENTO_CONTROL = (
    ("corporacion-regional", "Acciones de Seguimiento y Control de la Corporación Regional"),
    ("ministerio-medio-ambiente", "Acciones de Seguimiento y Control del Ministerio del Medio Ambiente"),
)

class OpcionesEstadoEjecucion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_opciones-ej")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    tipo = models.CharField(max_length=255, null = True, blank = True, choices=OPCIONES_ESTADOS_EJECUCION, default='Cesion-completa')

    nuevo_titular = models.CharField(max_length=255, null=True, blank=True, help_text='en Cesión')
    porque = models.CharField(max_length=255, null=True, blank=True, help_text='en Suspensión, Revocatoria')
    cuales = models.CharField(max_length=255, null=True, blank=True, help_text='en Integración de 2 Licencias Ambientales')

    class Meta:
        verbose_name_plural = 'Opciones'
        verbose_name = 'Opcion'

    def __unicode__(self):
        return self.get_tipo_display()

class ImpactoBase(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.nombre

class ImpactoAmbiental(ImpactoBase):
    pass
class ImpactoCultural(ImpactoBase):
    pass
class ImpactoEconomico(ImpactoBase):
    pass
class ImpactoSocial(ImpactoBase):
    pass
class ImpactoOrganizaciones(ImpactoBase):
    pass


class Afectacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_opciones-ej")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    tipo_afectacion = models.CharField(max_length=255, null=True, blank=True, choices=IMPACTOS)
    ambientales = models.ManyToManyField(ImpactoAmbiental, null = True, blank = True, related_name='afectaciones_ambientales')
    culturales = models.ManyToManyField(ImpactoCultural, null = True, blank = True, related_name='afectaciones_culturales')
    economicos = models.ManyToManyField(ImpactoEconomico, null = True, blank = True, related_name='afectaciones_economicos')
    sociales = models.ManyToManyField(ImpactoSocial, null = True, blank = True, related_name='afectaciones_sociales')
    organizaciones = models.ManyToManyField(ImpactoOrganizaciones, null = True, blank = True, related_name='afectaciones_organizaciones')

    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Afectaciones'
        verbose_name = 'Afectacion'

    def __unicode__(self):
        return self.get_tipo_afectacion_display()

class Accion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_opciones-ej")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    accion = models.CharField(max_length=255, null=True, blank=True, choices=ACCIONES_SEGUIMIENTO_CONTROL)
    descripcion = models.TextField(null = True, blank = True, verbose_name='Descripción de las acciones de seguimiento y control')

    class Meta:
        verbose_name_plural = 'Acciones de Seguimiento y Control'
        verbose_name = 'Accion'

    def __unicode__(self):
        return ': ' + self.get_accion_display()

class ConcesionBase(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_subcntrtas")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    nombre = models.CharField(verbose_name='nombre de la empresa', max_length=255, null=True, blank=True)
    resolucion_o_registro = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Concesiones'
        verbose_name = 'Consesion'
        abstract = True

# INFRAESTRUCTURA
TIPOS_ESTADOS_EJECUCION_INFRAESTRUCTURA = (
    ("concesion-convocatoria-publica-para-el-proyecto","Concesión / Convocatoria pública para el proyecto concreto"),
    ("concesion-adjudicacion-del-proyecto","Concesión / Ajudicación del proyecto"),
    ("desarrollo-del-proyecto","Desarrollo / Desarrollo del proyecto"),
    ("x","x / y"),
)

class EstadoEjecucionInfraestructura(models.Model):
    proyecto = models.ForeignKey(ProyectoObraInfraestructura, related_name="estados_ejecucion_proyecto")
    fase_tipo = models.CharField(max_length=255, null=True, blank=True, choices=TIPOS_ESTADOS_EJECUCION_INFRAESTRUCTURA)

    fecha_iniciacion = models.DateField(null=True, blank=True)
    fecha_terminacion = models.DateField(null=True, blank=True)
    subcontratista = models.BooleanField(help_text='Tiene subcontratistas?')

    class Meta:
        verbose_name_plural = 'Estados de ejecucion de infraestructura'
        verbose_name = 'Estado de ejecucion de infraestructura'

    def __unicode__(self):
        return '%s : %s'  % (self.proyecto, self.fase_tipo)

class Subcontratista(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_subcntrtas")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    nombre = models.CharField(verbose_name='nombre de la empresa', max_length=255, null=True, blank=True)
    objeto = models.TextField(verbose_name='objeto de la empresa', null = True, blank = True)

class ConcesionInfraestructura(ConcesionBase):
    pass

#HIDROCARBUROS
TIPOS_ESTADOS_EJECUCION_HIDROCARBUROS = (
    ("concesion-convocatoria-area-exploracion-explotacion-hidrocarburos","Concesión / Convocatoria Área de Exploración y Explotación de Hidrocarburos"),
    ("concesion-adjudicacion-de-proyecto","Concesión / Adjudicación del proyecto"),
    ("exploracion-sismica-con-vias","Exploración/ Exploración sísmica - con vías"),
    ("exploracion-sismica-sin-vias","Exploración / Exploración sísmica - sin vías"),
    ("exploracion-sismica-maritima-hasta-200m","Exploración / Exploración sísmica - áreas marítimas en una profundidad hasta 200 metros"),
    ("exploracion-perforacion-dentro-campos-hidrocarburos","Exploración / Perforación exploratoria - dentro de campos de producción de hidrocarburos"),
    ("exploracion-perforacion-fuera-campos-hidrocarburos","Exploración / Perforación exploratoria - afuera de campos de producción de hidrocarburos"),
    ("explotacion","Explotación"),
    ("x","x / y"),
)

INFORMACION_ADICIONAL = (
    (1,"con obras complementarias"),
    (2,"transporte y conducción líquidos"),
    (3,"transporte y conducción gaseosos"),
    (4,"transporte y conducción liquido y gaseosos"),
    (5,"terminales de entrega y estaciones de transferencias"),
    (6,"Construcción y operación de refinerías"),
)

class EstadoEjecucionHidrocarburo(models.Model):
    proyecto = models.ForeignKey(ProyectoInsdustriaHidrocarburos, related_name="estados_ejecucion_proyecto_hidro")
    fase_tipo = models.CharField(max_length=255, null=True, blank=True, choices=TIPOS_ESTADOS_EJECUCION_HIDROCARBUROS)

    fecha_iniciacion = models.DateField(null=True, blank=True)
    fecha_terminacion = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Estados de ejecucion de hidrocarburos'
        verbose_name = 'Estado de ejecucion de hidrocarburos'

    def __unicode__(self):
        return '%s : %s'  % (self.proyecto, self.fase_tipo)

class ConcesionHidrocarburo(ConcesionBase):
    ecopetrol = models.BooleanField(verbose_name='Tiene(n) Contrato de Asociación con Ecopetrol?')

class EstadoEjecucionExplotacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_hidroxplotacion")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    adicional = models.CommaSeparatedIntegerField(max_length=255, null=True, blank=True, choices=INFORMACION_ADICIONAL, verbose_name='información adicional')
    descripcion =  models.TextField(help_text='cuales obras complementarias, longitud de transporte, ubicación', null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Explotaciones'
        verbose_name = 'Explotacion'

# MINERIA
TIPOS_ESTADOS_EJECUCION_MINERIA = (
    ("Prospeccion","Prospección"),
    ("consesion-(zona-minera)-convocatoria","Concesión (en zona minera de grupos étnicos) / Convocatoria pública"),
    ("consesion-(zona-minera)-hallazgo","Concesión (en zona minera de grupos étnicos) / Hallazgo minero"),
    ("consesion-(zona-minera)-adjudicacion","Concesión (en zona minera de grupos étnicos) / Adjudicación"),
    ("consesion-(concesion-o-titulo-minera)-convocatoria","Concesión (Concesión minera o Titulo minero) / Convocatoria pública"),
    ("consesion-(concesion-o-titulo-minera)-hallazgo","Concesión (Concesión minera o Titulo minero) / Hallazgo minero"),
    ("consesion-(concesion-o-titulo-minera)-adjudicacion","Concesión (Concesión minera o Titulo minero) / Adjudicación"),
    ("exploracion-con-vias","Exploración / con vías"),
    ("exploracion-sin-vias","Exploración / sin vías"),
    ("explotacion","Explotación"),
    ("x","x / y"),
)

class EstadoEjecucionMineria(models.Model):
    proyecto = models.ForeignKey(ProyectoMineria, related_name="estados_ejecucion_proyecto_mine")
    fase_tipo = models.CharField(max_length=255, null=True, blank=True, choices=TIPOS_ESTADOS_EJECUCION_MINERIA)

    fecha_iniciacion = models.DateField(null=True, blank=True)
    fecha_terminacion = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Estados de ejecucion de mineria'
        verbose_name = 'Estado de ejecucion de mineria'

    def __unicode__(self):
        return '%s : %s'  % (self.proyecto, self.fase_tipo)

class ConcesionMineria(ConcesionBase):
    tiene_asociacion = models.BooleanField(verbose_name='Tiene contrato de asociación?')
    descripcion = models.TextField(null = True, blank = True, help_text='Descripcion del contrato de asociacion')

# AGROINDUSTRIA
TIPOS_ESTADOS_EJECUCION_MINERIA = (
    ("praparacion-del-terreno","Preparación del terreno"),
    ("cultivo","Cultivo"),
    ("produccion","Producción"),
    ("transformacion","Transformación"),
    ("comercializacion","Comercialización"),
    ("x","x / y"),
)

class EstadoEjecucionAgroindustria(models.Model):
    proyecto = models.ForeignKey(ProyectoAgroindustria, related_name="estados_ejecucion_proyecto_agro")
    fase_tipo = models.CharField(max_length=255, null=True, blank=True, choices=TIPOS_ESTADOS_EJECUCION_MINERIA)

    fecha_iniciacion = models.DateField(null=True, blank=True)
    fecha_terminacion = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Estados de ejecucion de agroindustria'
        verbose_name = 'Estado de ejecucion de agroindustria'

    def __unicode__(self):
        return '%s : %s'  % (self.proyecto, self.fase_tipo)

class Medida(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_medida")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    descripcion = models.TextField(null = True, blank = True)

class Resultado(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_res")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    descripcion = models.TextField(null = True, blank = True)

class Destino(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_destino")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    descripcion = models.TextField(null = True, blank = True)