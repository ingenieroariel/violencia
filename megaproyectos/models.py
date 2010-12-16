# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato
from territorios.models import TerritorioComunidad
from territorios.models import Municipio
from django.db import models


TEMAS_DESAROLLO_LEGISLATIVO = (
    ('oi-maritimo-portuario','Obras de Infraestructura / Marítimo y Portuario'),
    ('oi-aereopuertos','Obras de Infraestructura / Aeropuertos'),
    ('oi-re-vial','Obras de Infraestructura / Red vial'),
    ('oi-red-fluvial-nac','Obras de Infraestructura / Red fluvial nacional'),
    ('oi-red-ferea','Obras de Infraestructura / Red férrea'),
    ('oi-distritos','Obras de Infraestructura / Distritos de riego'),
    ('oi-rellenos','Obras de Infraestructura / Rellenos sanitarios'),
    ('oi-vivienda','Obras de Infraestructura / Macroproyectos de Vivienda'),
    ('oi-sector-electrico','Obras de Infraestructura / Sector Eléctrico'),
    ('ee-ind-hidrocarburos','Economía Extractiva / Industria Hidrocarburos'),
    ('ee-mineria','Economía Extractiva / Mineria'),
    ('ee-aprovechamiento','Economía Extractiva / Aprovechamiento Forestal Persistente'),
    ('ee-extraccion-pesquera','Economía Extractiva / Extracción pesquera'),
    ('ee-agroindustria','Economía de Transformación / Agroindustria'),
)

IMPACTOS = (
    ("","Impacto Ambiental / Suelos"),
    ("","Impacto Ambiental / Rios"),
    ("","Impacto Ambiental / Quebradas"),
    ("","Impacto Ambiental / Cultivos"),
    ("","Impacto Ambiental / Bosques"),
    ("","Impacto Ambiental / Manglares"),
    ("","Impacto Ambiental / Payas"),
    ("","Impacto Ambiental / Nacimiento de agua"),
    ("","Impacto Ambiental / Fauna"),
    ("","Impacto Ambiental / Aire"),
    ("","Impacto Ambiental / Ruido"),
    ("","Impacto Ambiental / Otro"),
    ("","Impactos culturales / Forma de autoridad"),
    ("","Impactos culturales / Fiestas"),
    ("","Impactos culturales / Lengua"),
    ("","Impactos culturales / Comida"),
    ("","Impactos culturales / Cambios de proyecto de vida"),
    ("","Impactos culturales / Otro"),
    ("","Impactos económicos / Ingreso"),
    ("","Impactos económicos / Relaciones laborales"),
    ("","Impactos económicos / Sistema productivo"),
    ("","Impactos económicos / Otro"),
    ("","Impactos sociales / Salud"),
    ("","Impactos sociales / Educación"),
    ("","Impactos sociales / Cambio de roles"),
    ("","Impactos sociales / Movilidad de la población"),
    ("","Impactos sociales / Conflictos - Interetnicos"),
    ("","Impactos sociales / Conflictos - Intraetnicos"),
    ("","Impactos sociales / Conflictos - Otros actores"),
    ("","Impactos sociales / Otro"),
    ("","Impactos en las organizaciones / División"),
    ("","Impactos en las organizaciones / Cambios de objetivos"),
    ("","Impactos en las organizaciones / Corrupción"),
    ("","Impactos en las organizaciones / Perdida de legitimidad"),
    ("","Impactos en las organizaciones / Otro"),
    ("","Territorio Colectivo Indígena titulado / Cambio de uso"),
    ("","Territorio Colectivo Indígena titulado / Formas de despojo"),
    ("","Territorio Colectivo Indigena no titulado / Cambio de uso"),
    ("","Territorio Colectivo Indigena no titulado / Formas de despojo"),
    ("","Territorio Colectivo Comunidades Negras titulado / Cambio de uso"),
    ("","Territorio Colectivo Comunidades Negras titulado / Formas de despojo"),
    ("","Territorio Colectivo Comunidades Negras no titulado / Cambio de uso"),
    ("","Territorio Colectivo Comunidades Negras no titulado / Formas de despojo"),
    ("","Territorios / Areas protegidas - Parque nacional; Santuario de Fauna y Flora"),
    ("","Territorios / Otros"),
)

class Afectacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_afectacion")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey()

    tipo = models.CharField(max_length=100, choices=IMPACTOS)
    territorio = models.ForeignKey(TerritorioComunidad, null=True, blank=True, help_text='Solo si selecciono afectacion de Territorio Colectivo')
    descripcion = models.TextField()

    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Afectacion'
    

class DesarrolloLegislativo(models.Model):
    tema = models.CharField(max_length=50, choices=TEMAS_DESAROLLO_LEGISLATIVO)
    documento = models.FileField(upload_to='uploads/documentos_desarrollo_legislativos', blank=True, null=True)
    fecha = models.DateField(null=True, blank=True)
    decreto = models.CharField(max_length=255, null=True, blank=True)
    resolucion = models.CharField(max_length=255, null=True, blank=True)
    ordenanza = models.CharField(max_length=255, null=True, blank=True)
    jurisprudencia = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Desarrollos Legislativos'

class Megaproyecto(models.Model):
    municipios = models.ManyToManyField(Municipio)
    nombre_documento = models.CharField(max_length=255, null=True, blank=True)
    documento = models.FileField(upload_to='uploads/documentos_megaproyectos', blank=True, null=True)
    vigencia = models.DateField()

    class Meta:
        abstract = True

TIPOS_PROYECTOS_MARITIMO_PORTUARIO = (
    ("nacional","Nacional (Licencia Ambiental del Ministerio del Medio Ambiente, Vivienda y Desarrollo TerritorialLA-MAVDT)"),
    ("regional","Regional (Licencia Ambiental de la Corporación Autónoma Regional LA-CAR)"),
)

class ObrasInfraestructura(Megaproyecto):

    class Meta:
        verbose_name_plural = 'Infraestructura: Obras de infraestructura'

class ProyectoMaritimoPortuario(models.Model):
#    megaproyecto = models.ForeignKey(Megaproyecto)
    tipo = models.CharField(max_length=50, choices=TIPOS_PROYECTOS_MARITIMO_PORTUARIO)