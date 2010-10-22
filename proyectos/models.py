# -*- coding: utf-8 -*-
from django.db import models
from territorios.models import Departamento, Municipio, TerritorioComunidad


class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    representante_legal = models.CharField(max_length=255)
    sede_principal = models.CharField(max_length=255)
    accionistas_nacionales = models.BooleanField()
    accionistas_extranjeros = models.BooleanField()
    opera_en_colombia = models.BooleanField()
    opera_en_extranjero = models.BooleanField()
    otras_actividades = models.TextField()
    
    def __unicode__(self):
        return self.nombre

TIPO_INSTITUCION_CHOICES=(
    ('nacional', 'Nacional'),
    ('internacional', 'Internacional'),
    ('publica', 'Pública'),
    ('privada', 'Privada'),
)

class InstitucionFinanciera(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices= TIPO_INSTITUCION_CHOICES)
    
    def __unicode__(self):
        return "%s (%s)" % (self.nombre, self.tipo)
  
class Financiacion(models.Model):
    monto = models.IntegerField(help_text = "En millones de pesos")
    institucion_financiera = models.ForeignKey(InstitucionFinanciera)
    empresa = models.ForeignKey(Empresa)

    def __unicode__(self):
        return "%s (%s)" % (self.empresa, self.monto)

AREA_PROYECTO_CHOICES = (
     ('maritimo', 'Marítimo'),
     ('terrestre', 'Terrestre'),
)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio)
    territorio= models.ForeignKey(TerritorioComunidad)
    area_proyecto = models.CharField(max_length=50, choices = AREA_PROYECTO_CHOICES)
    inicio = models.DateField()
    final = models.DateField()
    empresa = models.ForeignKey(Empresa)
    fecha_convocatoria = models.DateField()
    fecha_adjudicacion = models.DateField()
    subcontratista = models.BooleanField()
    nombre_subcontratista = models.CharField(max_length=255)
    cesion = models.SmallIntegerField()
    nuevo_titular = models.CharField(max_length=255)
    suspension = models.SmallIntegerField()
    motivo_suspension = models.CharField(max_length=255)
    revocatoria = models.SmallIntegerField()
    motivo_revocatoria = models.CharField(max_length=255)
    requisitos_legales = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nombre

class ConsultaPrevia(models.Model):
    fecha_acuerdo = models.DateField()
    suscriptores = models.TextField()
    acuerdos = models.TextField()
    metodologia = models.TextField()
    participacion = models.TextField()
    cumplimiento_acuerdos = models.TextField()
    conflictos = models.TextField()

    def __unicode__(self):
       return "Consulta Previa #%d (%s)" % (self.pk, self.fecha_acuerdo)

class LicenciaAmbiental(models.Model):
    impacto_ambiental = models.TextField()
    impacto_cultural = models.TextField()
    impacto_socioeconomico = models.TextField()

    def __unicode__(self):
        return "Licencia Ambiental #%d" % self.pk

class PlanManejo(models.Model):
    descripcion = models.TextField()
    medidas_prevencion = models.TextField()
    medidas_mitigacion = models.TextField()
    medidas_correccion = models.TextField()
    medidas_compensacion = models.TextField()

    def __unicode__(self):
        return "Plan de Manejo #%d" % self.pk

class RequisitoLegal(models.Model):
    consulta_previa = models.ForeignKey(ConsultaPrevia)
    licencia_ambiental = models.ForeignKey(LicenciaAmbiental)
    plan_manejo = models.ForeignKey(PlanManejo)

    def __unicode__(self):
        return "Requisito Legal #%d" % self.pk

class Empleo(models.Model):
    compromiso_consulta = models.BooleanField()
    empleo_local = models.BooleanField()
    cantidad = models.IntegerField()
    tipo_actividades = models.TextField()
    salario_medio = models.IntegerField()
    forma_pago = models.CharField(max_length=255)
    empleo_otra_region = models.BooleanField()
    cantidad = models.IntegerField()
    tipo_actividades = models.TextField()
    forma_pago = models.CharField(max_length=255)

    def __unicode__(self):
        return "Empleo #%d" % self.pk

class ProgramaSocial(models.Model):
    compromiso_consulta = models.BooleanField()
    educacion = models.TextField()
    educacion_monto = models.IntegerField()
    infraestructura = models.TextField()
    infraestructura_monto = models.IntegerField()
    salud = models.TextField()
    salud_monto = models.IntegerField()
    produccion = models.TextField()
    produccion_monto = models.IntegerField()
    otros = models.TextField()
    otros_monto = models.IntegerField()

    def __unicode__(self):
        return "Programa Social #%d" % self.pk
        
class Subsidio(models.Model):
    compromiso_consulta = models.BooleanField()
    individuales = models.TextField()
    individuales_monto = models.IntegerField()
    colectivos = models.TextField()
    colectivos_monto = models.IntegerField()

    def __unicode__(self):
        return "Subsidio #%d" % self.pk

class VinculaionPoblacion(models.Model):
    empleo = models.ForeignKey(Empleo)
    programa_social = models.ForeignKey(ProgramaSocial)
    subsidio = models.ForeignKey(Subsidio)

    def __unicode__(self):
        return "Vinculacion Poblacion #%d" % self.pk

MEGAPROYECTO_CHOICES = (
     ('infraestructura', 'Infraestructura'),
     ('electrico', 'Sector Eléctrico'),
     ('extractiva', 'Economía Extractiva'),
     ('agroindustria', 'Agroindustria'),
)

class Megaproyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    tipo_proyecto = models.CharField(max_length=100)
    requisitos_legales = models.ForeignKey(RequisitoLegal)
    tipo = models.CharField(max_length=30, choices=MEGAPROYECTO_CHOICES)

    def __unicode__(self):
        return self.proyecto


class DesarrolloLegislativo(models.Model):
    megaproyecto = models.ForeignKey(Megaproyecto)
    documento = models.CharField(max_length=255)
    fecha = models.DateField()
    decreto = models.CharField(max_length=100)
    resolucion = models.CharField(max_length=100)
    ordenanza = models.CharField(max_length=100)
    jurisprudencia = models.CharField(max_length=50)