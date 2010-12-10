# -*- coding: utf-8 -*-
from django.db import models
from fuentes.models import FuenteDato
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.
TIPO_CONFICTOS = (
    ("cultural","Cultural"),
    ("politico-violencia","Político / Violencia"),
    ("politico-pgarmados","Político / Presencia Grupos armados"),
    ("politico-electoral","Político / Político electoral"),
    ("economico","Económico"),
    ("recursos-nat","Recursos Naturales"),
    ("terr-uso","Territorial / Uso"),
    ("terr-delimitacion","Territorial / Delimitación"),
    ("otros","Otros")
)

class Conflicto(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_conflicto")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey()

    categoria = models.CharField(max_length=50, choices=( ("intraetnico","Intraétnico"),("interetnico","Interétnico") ) )
    tipo = models.CharField(max_length=50, choices=TIPO_CONFICTOS)
    """ descripcion """
#    ubicacion = models.TextField(null=True, blank=True)
#    actores = models.TextField(null=True, blank=True)
#    hechos = models.TextField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    estado = models.CharField(max_length=50, null=True, blank=True, choices=( ("abierto","Abierto"),("cerrado","Cerrado") ) )
    fecha = models.DateField(null=True, blank=True)
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="conflictos")

