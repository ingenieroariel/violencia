# -*- coding: utf-8 -*-
from gestion.models import Ubicacion
from django.db import models

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

ACCIONES_AFECTAN_USO_TERRITORIO = (
    ("campamentos","Campamentos"),
    ("bases-fijas","Bases fijas"),
    ("proteccion-megaproy","Protección megaproyectos"),
    ("campos-minados","Campos minados"),
    ("restricciones-movilidad","Restricciones a la movilidad"),
    ("suplantacion","Suplantación de la autonomía y del gobierno local"),
)

class ActorArmado(Ubicacion):
    fuerza_publica = models.CharField(max_length=50, blank=True, null=True, choices=ACTORES_ARMADOS)

    class Meta:
        verbose_name_plural = "Actores armados"

class AccionActorArmado(models.Model):
    actor_armado = models.ForeignKey(ActorArmado, related_name='acciones')
    acciones = models.CharField(max_length=50, blank=True, null=True, choices=ACCIONES_AFECTAN_USO_TERRITORIO)

    class Meta:
        verbose_name_plural = "Acciones de actor armado"

