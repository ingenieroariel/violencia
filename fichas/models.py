# -*- coding: utf-8 -*-
from django.db.models.fields import DateTimeField
from django_extensions.db.fields import ModificationDateTimeField
from django_extensions.db.fields import CreationDateTimeField
from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import TextField
from django.db import models
from django.db.models.fields import CharField, IntegerField, SmallIntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PolygonField, PointField
from territorios.models import Departamento, Municipio

#un mockup de como quieren q sea este formulario para ajustar relaciones
class Relato(models.Model):
    departamento = ForeignKey(Departamento)
    municipio = ForeignKey(Municipio)
    corregimiento = CharField(max_length=100)
    ins_deptal = CharField(max_length=255, null=True, blank=True)
    ins_munic =CharField(max_length=255, null=True, blank=True)
    caserio = CharField(max_length=255, null=True, blank=True)

    vereda = CharField(max_length=255, null=True, blank=True)
    lugar = CharField(max_length=255, null=True, blank=True)
    sitio = CharField(max_length=255, null=True, blank=True)
    barrio = CharField(max_length=255, null=True, blank=True)
    direccion = CharField(max_length=255, null=True, blank=True)
#    coordenadas = CharField(max_length=255, null=True, blank=True)
    tipo = CharField(verbose_name='Tipo geografico', max_length=20, choices=(('urbano','Urbano'),('rural','Rural'),('ambos','Ambos'),('sininfo','Sin Inf.')) )
    antecedentes = TextField(null=True, blank=True)
    contexto = TextField(null=True, blank=True)

    ocurrido_en = DateTimeField(verbose_name='Fecha y Hora del hecho')
    duracion_hecho = IntegerField(verbose_name='Duracion del hecho en minutos', default=1)
    
    #Audit fields
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    geom = PointField()

    def __unicode__(self):
        return 'Relato: #%i' % self.id

class Fuente(models.Model):
    relato = ForeignKey(Relato, help_text="Llenar este campo sólo para fuentes directas",related_name='fuentes', null=True, blank=True)
    nombre = CharField(max_length=255)
    tipo = CharField(verbose_name='Tipo de fuente', max_length=1, choices=(('d','Directa'),('i','Indirecta (Medios de Información)')), default='d')
    ubicacion = CharField(max_length=200 ,default='Fuente directa', null=True, blank=True)

    def __unicode__(self):
        return 'Fuente: #%s' % self.nombre
    
class TipoViolencia(models.Model):
    nombre = CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

class GrupoViolencia(models.Model):
    tipo = ForeignKey(TipoViolencia, related_name='grupos')
    nombre = CharField(max_length=255)

    def __unicode__(self):
        return '%s - %s' % (self.tipo.nombre, self.nombre)

class ItemGrupoViolencia(models.Model):
    grupo = ForeignKey(GrupoViolencia, related_name='grupo_items')
    codigo = CharField(max_length=255)
    nombre_tipo = CharField(verbose_name='Nombre de tipo de violencia', max_length=255)

    def __unicode__(self):
        return '%s: %s - %s' % (self.codigo, self.grupo, self.nombre_tipo)

class Victima(models.Model):
    relato = ForeignKey(Relato, related_name='victimas')
    nombre = CharField(max_length=255)
    por_cantidad = CharField(verbose_name='Victimas por cantidad', max_length=1, choices=(('i','Individual'),('c','Colectiva')), default='i')
    tipo_violencia = ManyToManyField(ItemGrupoViolencia, through='RelacionVictima')
    def __unicode__(self):
        return 'Victima: %s' % self.nombre
    
class RelacionVictima(models.Model):
    victima = ForeignKey(Victima, related_name='tipos_violencia')
    tipo_violencia = ForeignKey(ItemGrupoViolencia)

    def __unicode__(self):
        return 'Relacion con victima: %s' % self.victima.nombre

    
