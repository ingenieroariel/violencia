# -*- coding: utf-8 -*-
from territorios.models import Municipio, TERRITORIOS, Ubicacion
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

class DesastreNatural(models.Model):
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

""" AREAS NATURALES PROTEGICA """

AREAS_NATURALES = (
    ("parque-nacional","Parque nacional"),
    ("reserva-natural","Reserva natural"),
    ("area-natural-unica","Area natural única"),
    ("santuario-de-flora","Santuario de flora"),
    ("santuario-de-fauna","Santuario de fauna"),
    ("via-parque","Via parque"),
)

AFECTACIONES_AREA_PROTEGIDA = (
    ("investigaciones-cientificas","Investigaciones cientificas"),
    ("explotacion-recursos-naturales","Explotación de recursos naturales"),
    ("cultivos-ilicitos-siembra","Cultivos de uso ilícito / Siembra"),
    ("cultivos-ilicitos-procesamiento","Cultivos de uso ilícito / Procesamiento"),
    ("cultivos-ilicitos-fumigaciones","Cultivos de uso ilícito / Fumigaciones"),
    ("conflicto-armado","Conflicto armado"),
    ("deforestacion","Deforestación"),
    ("ganaderia","Ganaderia"),
    ("impactos-turismo","Impactos del turismo"),
    ("asentamientos-humanos","Asentamientos humanos"),
)

class AreaNaturalProtegida(models.Model):
    area_natural = models.CharField(max_length=50, choices=AREAS_NATURALES)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    """ UBICACION """
    municipios = models.ManyToManyField(Municipio)
    resolucion_creacion = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    traslape = models.CharField(max_length=255, null=True, blank=True, choices=TERRITORIOS)
    descripcion_conflictos_uso = models.TextField(null=True, blank=True, verbose_name='Descripción de conflictos en uso')

    class Meta:
        verbose_name_plural = 'Areas naturales protegidas'

    def __unicode__(self):
        return self.nombre

class ParqueNacionalMAVDT(models.Model):
    area_natural = models.ForeignKey(AreaNaturalProtegida, related_name='parques')
    plan_de_manejo = models.CharField(max_length=255, null=True, blank=True)
    participantes = models.CharField(max_length=255, null=True, blank=True)
    participantes_descripcion = models.CharField(max_length=255, null=True, blank=True, verbose_name='Descripción')
    acuerdos_uso_manejo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Acuerdos de uso y manejo')

    regimen_especial_manejo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Regimen especial de manejo', help_text='Cuando hay traslapes con Reguardos indígenas')

    concesion_turistica = models.BooleanField(help_text='Seleccione sí responde SI')
    concesion_turistica_entidad = models.CharField(max_length=255, null=True, blank=True, help_text='En caso de tener concesión turistica', verbose_name='Entidad')
    concesion_turistica_representante_legal = models.CharField(max_length=255, null=True, blank=True, help_text='En caso de tener concesión turistica', verbose_name='Representante legal')
    representante_opera_en_colombia = models.BooleanField(help_text='Seleccione sí responde SI')
    representante_opera_en_extranjero = models.BooleanField(help_text='Seleccione sí responde SI')
    representante_actividades_economicas = models.TextField(null=True, blank=True, verbose_name='Describa actividades economicas del representante')

    class Meta:
        verbose_name = 'Parque Nacional MAVDT'
        verbose_name_plural = 'Parques Nacionales MAVDT'

class AfectacionAreaProtegida(models.Model):
    area_natural = models.ForeignKey(AreaNaturalProtegida, related_name='afectaciones')
    afectacion = models.CharField(max_length=50, choices=AFECTACIONES_AREA_PROTEGIDA)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Afectacion area protegida'
        verbose_name_plural = 'Afectaciones area protegida'
