# -*- coding: utf-8 -*-
from django.db import models
from megaproyectos.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato

#STACKED INLINES GENERICAS
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

class EstadoEjecucionCesion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_cesion")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    tipo = models.CharField(max_length=255, null=True, blank=True, choices=( ("completa","Completa"),("parcial","Parcial") ))
    nuevo_titular = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cesiones'
        verbose_name = 'Cesion'

class EstadoEjecucionSuspension(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_cesion")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    por_que = models.TextField(help_text='describa el porque de la suspension', null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Suspensiones'
        verbose_name = 'Suspension'

class EstadoEjecucionRevocatoria(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_revocatoria")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    por_que = models.TextField(help_text='describa el porque de la revocatoria', null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Revocatorias'
        verbose_name = 'Revocatoria'

class Subcontratista(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_subcntrtas")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    nombre = models.CharField(verbose_name='nombre de la empresa', max_length=255, null=True, blank=True)
    objeto = models.TextField(verbose_name='objeto de la empresa', null = True, blank = True)

class ConcesionInfraestructura(ConcesionBase):
    pass

class LicenciaAmbiental(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_subcntrtas")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    perdida = models.TextField(null = True, blank = True, verbose_name='Perdida de vigencia')
    integracion = models.BooleanField(verbose_name='Integra dos Licencias Ambientales?')
    cuales = models.TextField(null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Licencias Ambientales'
        verbose_name = 'Licencia Ambiental'

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