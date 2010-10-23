# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from territorios.models import TerritorioComunidad

class ActividadProductiva(models.Model):
    tipo = models.CharField(max_length=200)
    descripcion = models.TextField()

class Afectacion(models.Model):
    tipo_impacto_ambiental = models.CharField(max_length=200)
    descripcion_impacto_ambiental = models.TextField()
    tipo_impacto_cultural = models.CharField(max_length=200)
    descripcion_impacto_cultural = models.TextField()
    tipo_impacto_economico = models.CharField(max_length=200)
    descripcion_impacto_economico = models.TextField()
    tipo_impacto_social = models.CharField(max_length=200)
    descripcion_impacto_social = models.TextField()
    tipo_impacto_organizacion = models.CharField(max_length=200)
    descripcion_impacto_organizacion = models.TextField()
    
class ModeloAdministracion(models.Model):
    externo = models.BooleanField()
    compartido = models.BooleanField()
    administrador = models.CharField(max_length=255)
    autonomo = models.BooleanField()

class GestionRecursos(models.Model):
    monto_total = models.IntegerField()
    tipo_cooperacion = models.CharField(max_length=200)
    entidades_cooperacion = models.TextField()
    monto_cooperacion = models.IntegerField()

class GestionEconomica(models.Model):
    iniciativa_empresarial = models.CharField(max_length=200)
    territorio = models.ForeignKey(TerritorioComunidad)
    cobertura_poblacional = models.IntegerField()
    actividad_productiva = models.ForeignKey(ActividadProductiva)
    gestion_recursos = models.ForeignKey(GestionRecursos)
    modelo_administracion = models.ForeignKey(ModeloAdministracion)
    afectacion = models.ForeignKey(Afectacion)

class PlanEtnodesarrollo(models.Model):
    nombre = models.CharField(max_length=250)
    cobertura = models.TextField()
    sectores_que_aplican = models.TextField()
    evaluacion_implementacion = models.TextField()
    territorio = models.ForeignKey(TerritorioComunidad)

class ConsejoComunitarioMayor(models.Model):
    representante_legal = models.CharField(max_length=255)
    permanencia = models.IntegerField()
    asamblea = models.TextField()
    comites = models.TextField()
    junta_directiva = models.TextField()
    asociacion_consejo_comunitario = models.TextField()
    reglamento_interno_debil = models.TextField()
    reglamento_interno_fuerte = models.TextField()
    territorio = models.ForeignKey(TerritorioComunidad)

class ConsejoComunitario(models.Model):
    representante_legal = models.CharField(max_length=255)
    permanencia = models.IntegerField()
    asamblea = models.TextField()
    comites = models.TextField()
    junta_directiva = models.TextField()
    asociacion_consejo_comunitario = models.TextField()
    consejo_comunitario_mayor = models.ForeignKey(ConsejoComunitarioMayor)
    territorio = models.ForeignKey(TerritorioComunidad)

AUTORIDAD_CHOICES=(
    ('jaibana', 'Jaibana'),
    ('tachinab', 'Tachinab'),
    ('tonquero', 'Tonquero'),
    ('otro', 'Otro...'),
)

AGENTE_CHOICES = (
    ('hierbatero', 'Hierbatero'),
    ('partera', 'Partera'),
    ('otro', 'Otro...'),
)

class CabildoLocal(models.Model):
    nombre = models.CharField(max_length=255)
    estructura_organizativa = models.TextField()
    autoridades_tradicionales = models.BooleanField()
    tipo_autoridad = models.CharField(max_length = 50, choices = AUTORIDAD_CHOICES)
    cantidad_autoridades = models.IntegerField()
    agentes_salud_tradicional = models.BooleanField()
    tipo_agente_salud = models.CharField(max_length=50, choices= AGENTE_CHOICES)
    cantidad_agentes_salud = models.IntegerField()
    territorio = models.ForeignKey(TerritorioComunidad)

class CabildoMayor(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_resguardos = models.IntegerField()
    nombres_resguardos = models.TextField()
    asociacion_cabildos = models.BooleanField()
    territorio = models.ForeignKey(TerritorioComunidad)

class PlanVida(models.Model):
    nombre = models.CharField(max_length=255)
    cobertura = models.TextField()
    sectores_que_aplican = models.TextField()
    ordenamiento_territorial_area = models.IntegerField(help_text="en hectareas")
    ordenamiento_territorial_descripcion = models.TextField()
    evaluacion_implementacion = models.TextField()
    territorio = models.ForeignKey(TerritorioComunidad)

APLICACION_CHOICES=(
    ('debil', 'Debil'),
    ('fuerte', 'Fuerte'),
)

class JurisdiccionEspecialIndigena(models.Model):
    reglamento_justicia_indigena = models.BooleanField()
    tipo_nivel_aplicacion = models.CharField(max_length=20, choices=APLICACION_CHOICES)
    descripcion_nivel_aplicacion = models.TextField()
    territorio = models.ForeignKey(TerritorioComunidad)

class TransferenciasPresupuestales(models.Model):
    plan_inversion_anual = models.IntegerField(help_text="año")
    monto_educacion = models.IntegerField()
    monto_salud = models.IntegerField()
    monto_saneamieno = models.IntegerField()
    monto_produccion = models.IntegerField()
    monto_otros = models.IntegerField()
    territorio = models.ForeignKey(TerritorioComunidad)

class AccionesExigibilidadDerechos(models.Model):
    movilizacion = models.BooleanField()
    fecha_movilizacion = models.DateField()
    lugar_movilizacion = models.TextField()
    causa_movilizacion = models.TextField()
    participantes_movilizacion = models.IntegerField()
    instancia_movilizacion = models.CharField(max_length=200)
    descripcion_movilizacion = models.TextField()
    resultado_movilizacion = models.TextField()
    accion_juridica = models.BooleanField()
    fecha_accion_juridica = models.DateField()
    lugar_accion_juridica = models.TextField()
    causa_accion_juridica = models.TextField()
    participantes_accion_juridica = models.TextField()
    instancia_accion_juridica = models.TextField()
    descripcion_accion_juridica = models.TextField()
    resultado_accion_juridica = models.TextField()
    estrategia_comunicacion = models.BooleanField()
    fecha_estrategia_comunicacion = models.DateField()
    lugar_estrategia_comunicacion = models.TextField()
    causa_estrategia_comunicacion = models.TextField()
    participantes_estrategia_comunicacion = models.IntegerField()
    instancia_estrategia_comunicacion = models.TextField()
    descripcion_estrategia_comunicacion = models.TextField()
    resultado_estrategia_comunicacion = models.TextField()
    otro = models.CharField(max_length=255)
    fecha_otro = models.DateField()
    causa_otro = models.TextField()
    descripcion_otro = models.TextField()
    resultado_otro = models.TextField()
    territorio = models.ForeignKey(TerritorioComunidad)
