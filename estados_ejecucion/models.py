# -*- coding: utf-8 -*-
from django.db import models
from megaproyectos.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato
"""
"
"
"         ESTADOS DE EJECUCION
"
"
"""

# TIPOS ESTADOS DE EJECUCION
TIPOS_ESTADOS_EJECUCION_INFRAESTRUCTURA = (
    ("concesion-convocatoria-publica-para-el-proyecto","Concesión / Convocatoria pública para el proyecto concreto"),
    ("concesion-adjudicacion-del-proyecto","Concesión / Ajudicación del proyecto"),
    ("desarrollo-del-proyecto","Desarrollo / Desarrollo del proyecto"),
    ("x","x / y"),
)

class EstadoEjecucionCesion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_cesion")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

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

class Concesion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_subcntrtas")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    nombre = models.CharField(verbose_name='nombre de la empresa', max_length=255, null=True, blank=True)
    resolucion_o_registro = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Concesiones'
        verbose_name = 'Consesion'

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
