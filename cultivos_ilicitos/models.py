# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato
from territorios.models import TerritorioComunidad
from territorios.models import Municipio
from django.db import models


""" CULTIVOS PARA USO ILÍCITO """
CULTIVOS_PROMOTRES_ILICITOS = (
    ("guerrilla","Guerrilla"),
    ("paramilitares","Paramilitares"),
    ("otros","Otros"),
)

CULTIVOS_TIPO_PARTICIPACION = (
    ("cultivadores","Cultivadores"),
    ("raspachines","Raspachines"),
    ("procesadores","Procesadores"),
)

CULTIVOS_TIPO_ERRADICACION = (
    ("aerea","Aspersión aerea"),
    ("manual","Manual"),
)

CULTIVOS_AFECTACION_TERRITORIOS = (
    ("","Territorio Colectivo Indígena titulado"),
    ("","Territorio Colectivo Indigena no titulado"),
    ("","Territorio Colectivo Comunidades Negras titulado"),
    ("","Territorio Colectivo Comunidades Negras no titulado"),
    ("","Areas protegidas - Parque nacional; Santuario de Fauna y Flora"),
    ("","Otros"),
)

CULTIVOS_TIPOS_INVERSION = (
    ("","Subsidios / Familias en acción"),
    ("","Subsidios / Familias guardabosques"),
    ("","Proyectos productivos"),
)

class CultivosIlicitos(models.Model):
    municipio = models.ForeignKey(Municipio, null=True, blank=True)
    area = models.FloatField(help_text="en hectareas", blank=True, null=True)
    promotores = models.CharField(max_length=200, null=True, blank=True, choices=CULTIVOS_PROMOTRES_ILICITOS)
    """ PARTICIPACION """
    participacion_comunidad = models.BooleanField(help_text='Seleccione si tiene participacion de la comunidad')
    participacion_comunidad_tipo = models.CharField(max_length=200, null=True, blank=True, choices=CULTIVOS_TIPO_PARTICIPACION)
    participacion_otros = models.BooleanField(help_text='Seleccione si tiene participacion de otros')
    participacion_otros_tipo = models.CharField(max_length=200, null=True, blank=True, choices=CULTIVOS_TIPO_PARTICIPACION)

    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cultivos ilicitos'

class ErradicacionCultivosIlicitos(models.Model):
    cultivos_ilicitos = models.ForeignKey(CultivosIlicitos, related_name='erradicaciones')

    erradicacion_tipo = models.CharField(max_length=200, null=True, blank=True, choices=CULTIVOS_TIPO_ERRADICACION)
    territorios = models.ManyToManyField(TerritorioComunidad)
    referencia_cartografica = models.FileField(null=True, blank=True, upload_to='uploads/cultivos_ilicitos/referencias_cartograficas')
    area = models.CharField(max_length=200, null=True, blank=True)

    afectacion = models.CharField(max_length=200, null=True, blank=True, choices=CULTIVOS_AFECTACION_TERRITORIOS)
    afectacion_nombre = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nombre')

    impactos_salud_humana = models.BooleanField(verbose_name='Tiene impactos sobre la salud humana', help_text='Seleccione si responde si')
    impactos_salud_humana_descripcion = models.TextField(null=True, blank=True, verbose_name='Descripcion')
    impactos_ambientales = models.BooleanField(verbose_name='Tiene impactos ambientales', help_text='Seleccione si responde si')
    impactos_ambientales_descripcion = models.TextField(null=True, blank=True, verbose_name='Descripcion')
    impactos_seguridad_alimentaria = models.BooleanField(verbose_name='Tiene impactos sobre la seguridad alimentaria', help_text='Seleccione si responde si')
    impactos_seguridad_alimentaria_descripcion = models.TextField(null=True, blank=True, verbose_name='Descripcion')

    modalidad_ejecucion_directa = models.BooleanField(verbose_name='Posee modalidad de ejecucion directa', help_text='Seleccione si responde si')
    modalidad_ejecucion_contratada = models.BooleanField(verbose_name='Posee modalidad de ejecucion contratada', help_text='Seleccione si responde si')
    modalidad_ejecucion_contratada_quienes = models.TextField(null=True, blank=True)

    consulta_previa = models.BooleanField(verbose_name='Tiene consulta previa?', help_text='Seleccione si responde si')
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Erradicacion de cultivos ilicitos'

class InversionSocialCultivosIlicitos(models.Model):
    cultivos_ilicitos = models.ForeignKey(CultivosIlicitos, related_name='inversiones')

    tipo = models.CharField(max_length=200, null=True, blank=True, choices=CULTIVOS_TIPOS_INVERSION)
    catidad_familias = models.PositiveIntegerField(null=True, blank=True)
    monto_por_municipio = models.PositiveIntegerField(null=True, blank=True, help_text='millones de pesos')

    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)
