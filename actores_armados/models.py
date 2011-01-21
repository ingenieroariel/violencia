# -*- coding: utf-8 -*-
from django.db import models
from territorios.models import Municipio

ACTORES_ARMADOS = (
    ("fp-policia","Fuerza pública / Policia"),
    ("fp-ejercito","Fuerza pública / Ejercito"),
    ("fp-armada","Fuerza pública / Armada Nacional"),
    ("fp-fuerza","Fuerza pública  / Fuerza Aerea"),
    ("fp-extrageros","Fuerza pública / Agentes Extranjeros"),
    ("paracos","Paramilitares"),
    ("farc-ep","Guerrilla / FARC-EP"),
    ("eln","Guerrilla / ELN"),
    ("guerrilla-otro","Guerrilla / Otros"),
)


class ActorArmado(models.Model):
    municipio = models.ForeignKey(Municipio, null=True, blank=True)
    actor = models.CharField(max_length=50, blank=True, null=True, choices=ACTORES_ARMADOS)
    acciones = models.ManyToManyField('AccionActorArmado', null=True, blank=True)
    class Meta:
        verbose_name_plural = "Actores armados"

class AccionActorArmado(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Acciones de actor armado"

