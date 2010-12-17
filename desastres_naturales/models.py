# -*- coding: utf-8 -*-
from gestion.models import Ubicacion
from django.db import models

TIPO_DESASTRE = (
    ("inundacion","Inundación"),
    ("desbordamiento","Desbordamiento de un rio"),
    ("territorio","Terremoto"),
    ("maremoto","Maremoto"),
    ("tsunami","Tsunami"),
    ("incendio-natural","Incendio natural"),
    ("desplazamiento","Deslizamiento"),
    ("sequia","Sequia"),
    ("otro","Otro"),
)

TERRITORIO_AFECTADOS = (
    ("resguardo-indigena","Resguardo Indigena"),
    ("territorio-indigena-notitulado","Territorio Indigena no titulado"),
    ("tierras-colectivas-comunidades-negra-titulado","Tierras Colectivas Comunidades Negras titulado"),
    ("territorio-tradicional-comunidades-negras-no-titulado","Territorio tradicional Comunidades Negras no titulado"),
    ("areas-rpotegidas","Áreas protegidas (parque nacional Natural; Santuario de Fauna y Flora)"),
    ("otras-aras","Otras áreas"),
)

AFECTACIONES = (
    ("danos-materiales","Daño materiales"),
    ("perdida-vida-humana","Perdida de vidas humanas"),
    ("lesiones-personales","Lesiones personales"),
    ("perdida-cultivos","Perdida de cultivos"),
    ("perdida-animales","Perdida de animales domésticos"),
    ("afectacion-comunidades","Afectación de comunicaciónes"),
    ("desplazamiento","Desplazamiento"),
    ("otros","Otros"),
)

CLASES_INTERVENCIONES = (
    ("publica","Pública"),
    ("otra","Otra"),
)

class DesastreNatural(Ubicacion):
    tipo = models.CharField(max_length=50, null=True, blank=True, choices=TIPO_DESASTRE)
    descripcion_desastre = models.TextField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)

    poblacion = models.CharField(max_length=255, null=True, blank=True)
    territorios_afectados = models.CharField(max_length=255, null=True, blank=True, choices=TERRITORIO_AFECTADOS)
    causas_descripcion = models.TextField(null=True, blank=True, verbose_name='Causas')

    afectacion = models.CharField(max_length=50, null=True, blank=True, choices=AFECTACIONES)
    descripcion_afectacion = models.TextField(null=True, blank=True, help_text="En caso de que seleccione Daños materiales")

    intervencion_fecha = models.DateField(null=True, blank=True, verbose_name="fecha")
    intervencion_clase = models.CharField(max_length=50, null=True, blank=True, choices=CLASES_INTERVENCIONES, verbose_name="clase")
    intervencion_institucion_organizacion = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nombres institucion u organizaciones")
    intervencion_tipo = models.CharField(max_length=50, null=True, blank=True, verbose_name="tipo")

    class Meta:
        verbose_name_plural = "Desastres naturales"



