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
    
    """ servicios publicos """
    cobertura_acueducto_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_acueducto_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo municipios
    cobertura_acueducto_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo municipios
    
    cobertura_alcantarillado_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_alcantarillado_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo municipios
    cobertura_alcantarillado_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo municipios
    
    cobertura_energia_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo municipios
    cobertura_energia_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo municipios
    cobertura_energia_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo municipios
    
    fuente_servicios_publicos = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="servicios_publicos")
    
    """ esperanza de vida """
    esperanza_vida_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo dptos
    esperanza_vida_mujeres = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo dptos
    esperanza_vida_hombres = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True) #solo dptos
    
    mortalidad_total = models.IntegerField(null=True, blank=True) #solo dptos
    mortalidad_infantil = models.IntegerField(help_text="numero total", null=True, blank=True)
    mortalidad_maternoinfantil = models.IntegerField(help_text="numero total", null=True, blank=True)
    
    morbilidad_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion morbilidad")
    morbilidad_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Porcentaje de morbilidad")
    morbimortalidad_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion morbi-mortalidad")
    morbimortalidad_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Porcentaje de morbi-motalidad")
    
    alfabetizacion_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Tasa de alfabetizacion total") 
    alfabetizacion_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Tasa de alfabetizacion urbana") 
    alfabetizacion_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Tasa de alfabetizacion rural")
    
    fuente_esperanza_vida = models.ForeignKey(FuenteDato, null=True, blank=True)
    
    matricula_total = models.IntegerField(null=True, blank=True, help_text="numero total")
    
    class Meta:
        verbose_name_plural = "indicadores basicos"
        
class Educacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_1")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")

    nivel_educativo_preescolar = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Preescolar") 
    nivel_educativo_primaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Basica primaria") 
    nivel_educativo_secundaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Basica secundaria")
    
    nivel_educativo_mediatec = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Media tecnica")
    nivel_educativo_normalista = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Normalista")
    
    nivel_educativo_sup_tecnica = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Superior tecnico")
    nivel_educativo_sup_tecnologica  = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Superior tecnologico")
    nivel_educativo_sup_profesional = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Superior profesional")
    
    instituciones_total = models.IntegerField(null=True, blank=True, help_text="numero total de instituciones educativas") #todo: hacerlo como propiedad count InstitucionEducativa
    
    fuente_nivel_educativo = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="niveles_educativos")
    
    class Meta:
	verbose_name_plural = "indicadores basicos de educacion"
    
class InstitucionEducativa(models.Model):
    indicador_educacion = models.ForeignKey(Educacion, related_name="instituciones")
    nombre = models.CharField(max_length=200)
    es_publica = models.BooleanField(help_text="Desmarque si es privada", default=True)
    fecha_constitucion = models.DateField(blank=True, null=True)
    enfasis = models.CharField(max_length=200,blank=True, null=True)
    etnoeducacion = models.BooleanField(default=True)
    tiene_pei = models.BooleanField(default=True)
    tiene_pec = models.BooleanField(default=True)
    educa_adultos = models.BooleanField(default=False)
    adultos = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Educacion de personas adultas")
    
    """ maestros """
    maestros_vinculados_indigenas = models.IntegerField(null=True, blank=True, verbose_name="Total de maestros indigenas vinculados")
    maestros_vinculados_afro = models.IntegerField(null=True, blank=True, verbose_name="Total de maestros afro vinculados")
    maestros_vinculados_otros = models.IntegerField(null=True, blank=True, verbose_name="Total de otros maestros vinculados")
    maestros_vinculados_ejerciendo = models.IntegerField(null=True, blank=True, verbose_name="Total de maestros vinculados en ejercicio")
    
    maestros_contratados_indigenas = models.IntegerField(null=True, blank=True, verbose_name="Total de maestros indigenas contratados")
    maestros_contratados_afro = models.IntegerField(null=True, blank=True, verbose_name="Total de maestros afro contratados")
    maestros_contratados_otros = models.IntegerField(null=True, blank=True, verbose_name="Total de otros maestros contratados")
    maestros_contratados_ejerciendo = models.IntegerField(null=True, blank=True, verbose_name="Total de maestros contratados en ejercicio")
    
    """poblacion estudiantil"""
    cobertura_preescolar = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_primaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_secundaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_mediavocacional = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    
    cobertura_preescolar_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_primaria_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_secundaria_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    cobertura_mediavocacional_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    
    desercion = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    promocion = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    repitencia = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    analfabetismo = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    
    class Meta:
	verbose_name_plural = "instituciones educativas"
    
    
    
    
    
    
    
    
    

       

