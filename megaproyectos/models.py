# -*- coding: utf-8 -*-
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