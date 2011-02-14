# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from django.contrib.auth.models import User

class AutorDato(models.Model):
    nombre = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True, help_text="Por ejemplo, telefonos de contacto principal, dirección, etc")

    class Meta:
        verbose_name = "Autor de Datos"
        verbose_name_plural = "Autores de Datos"
    
    def __unicode__(self):
        return self.nombre
    
FRECUENCIA_CHOICES=(
     ('diario', 'Cada día'),
     ('mensual', 'Cada mes'),
     ('anual', 'Cada año'),
     ('demanda', 'Sin periodo definido'),
)

class FuenteDato(TimeStampedModel):
    nombre_documento = models.CharField(max_length=255)
    autor = models.ForeignKey(AutorDato)
    fecha = models.DateField(null = True, blank = True, help_text="Fecha en que la fuente creó la información")
    ano = models.PositiveIntegerField(null = True, blank = True, help_text='Si solo tiene el año', verbose_name='Año')
    frecuencia_actualizacion = models.CharField(max_length=255, choices=FRECUENCIA_CHOICES, default='anual')
    fecha_ingreso = models.DateField(help_text="Fecha en que se cargó la información en el sistema, por ejemplo: hoy")
    usuario = models.ForeignKey(User)
    archivo = models.FileField(upload_to="upload", null=True, blank=True)
    notas = models.TextField(blank=True, null=True, help_text="Notas acerca de la captura, por ejemplo: 'No hay archivo porque son muchas fichas físicas")

    class Meta:
        verbose_name = "Fuente de Datos"
        verbose_name_plural = "Fuentes de Datos"

    def __unicode__(self):
        return "%s (%s) - %s" % (self.autor.nombre, self.fecha, self.nombre_documento)
