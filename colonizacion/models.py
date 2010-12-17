# -*- coding: utf-8 -*-
from gestion.models import Ubicacion
from django.db import models

PROCEDENCIAS = (
    ("pacifico","De la región del pacifico"),
    ("otra","De otra región"),
)

CAUSAS = (
    ("economico","Economico"),
    ("expansion-cultivos-ilicitos","Expansión de cultivos de uso ilícito"),
    ("espontanea","Espontánea"),
    ("ca-guerrilla","Conflicto armado / Guerrilla"),
    ("ca-paramilitares","Conflicto armado / Paramilitares"),
    ("ca-fuerza-publica","Conflicto armado / Fuerza Pública"),
    ("otros","Conflicto armado / Otros"),
    ("proy-desarrollo","Proyectos de desarrollo"),
    ("megaproy","Megaproyecto"),
    ("grupo-religioso","Grupo religioso"),
    ("otro","Otro"),
)

TIPOS_USO_AREA = (
    ("cultivos-ilicitos","Cultivos de uso ilicitos"),
    ("agroconbustibles","Agrocombustibles"),
    ("extracion-forestal","Extraccion forestal"),
    ("mineria","Mineria"),
    ("otros","Otros"),
)

class Colonizacion(Ubicacion):
    procedencia = models.CharField(max_length=50, null=True, blank=True, choices=PROCEDENCIAS)
    cantidad_personas = models.IntegerField(help_text="Por año", null=True, blank=True)

    causa = models.CharField(max_length=50, null=True, blank=True, choices=CAUSAS)
    actor = models.CharField(max_length=255, null=True, blank=True, help_text='Solo si selecciono causa Economica.')
    megaproyecto = models.CharField(max_length=255, null=True, blank=True, help_text='Solo si selecciono causa Megaproyecto.')
    

    class Meta:
        verbose_name_plural = 'Colonizaciones'

class UsoTerritorio(models.Model):
    colonizacion = models.ForeignKey(Colonizacion, related_name='usos_de_territorio')
    tipo_uso_area = models.CharField(max_length=50, null=True, blank=True, choices=TIPOS_USO_AREA)
    area = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Uso del territorio'
        verbose_name_plural = 'Usos del terrotirio'

