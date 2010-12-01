# -*- coding: utf-8 -*-

from django.db import models
from fuentes.models import FuenteDato
from territorios.models import Departamento, Municipio
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class IndicadorBasico(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")

    ingreso_per_capita = models.IntegerField(null=True, blank=True)
    fuente_ingreso_per_capita = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="per")
    indice_desarrollo_humano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    fuente_indice_desarrollo_humano = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="desa")
    necesidades_insatisfechas_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    necesidades_insatisfechas_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    necesidades_insatisfechas_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    fuente_necesidades_insatisfechas = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="insat")
    indice_condiciones_de_vida= models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    fuente_indice_condiciones_de_vida = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="condic")
    
    class Meta:
        verbose_name_plural = "indicadores basicos"
