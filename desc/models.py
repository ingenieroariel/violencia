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
        verbose_name = "indicador basico de educacion"

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

class SistemaSalud(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_2")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")
    
    """ Régimen subsidiado carnetizado """
    reg_sub_carnetizado_indigena_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Poblacion indigena")
    reg_sub_carnetizado_indigena_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_carnetizado_afro_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Poblacion afro")
    reg_sub_carnetizado_afro_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_carnetizado_otra_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Otra poblacion")
    reg_sub_carnetizado_otra_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    """ Régimen subsidiado vinculado """
    reg_sub_vinculado_indigena_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Poblacion indigena")
    reg_sub_vinculado_indigena_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_vinculado_afro_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Poblacion afro")
    reg_sub_vinculado_afro_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_vinculado_otra_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Otra poblacion")
    reg_sub_vinculado_otra_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    """ Régimen contributivo """
    reg_contributivo_indigena_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Poblacion indigena")
    reg_contributivo_indigena_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_contributivo_afro_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Poblacion afro")
    reg_contributivo_afro_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_contributivo_otra_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Otra poblacion")
    reg_contributivo_otra_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    
    fuente_regimenes = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fregs")
    
    class Meta:
        verbose_name_plural = "indicadores basico de sistemas de salud"
        verbose_name = "indicador basico de sistema de salud"
    
class PromotoresSalud(models.Model):
    sistema_salud = models.ForeignKey(SistemaSalud, related_name="promotores_salud")
    nombre = models.CharField(max_length=200,null=True, blank=True, verbose_name="Nombre de entidad")
    promotores = models.IntegerField(null=True, blank=True, help_text="total")
    tipo_contrato = models.CharField(max_length=50, choices=(("temporal","Temporal"),("fijo","Fijo")) )
    numero_contrato_temporal = models.IntegerField(null=True, blank=True, help_text="solo si selecciono tipo de contrato temporal")
    
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "promotores de salud"
        
class InstalacionesSalud(models.Model):
    sistema_salud = models.ForeignKey(SistemaSalud, related_name="instalaciones_salud")
    tipo = models.CharField(max_length=50, choices=(("centro","Centro de salud"),("puesto","Puesto de salud"),("hospital","Hospital")))
    nombre = models.CharField(max_length=200,null=True, blank=True)
    ubicacion = models.CharField(max_length=200,null=True, blank=True) #todo geo
    nivel_de_atencion = models.IntegerField(null=True, blank=True, choices=((1,"1"),(2,"2"),(3,"3")), help_text="solo si selecciono hospital como tipo de instalacion" )
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "instalaciones de salud"
        
class DerechoPrimeraInfancia(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_3")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")
    
    """proteccion"""
    registro_civil = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Total de registros civiles")
    registro_civil_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Registros civiles de Indigenas")
    registro_civil_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Registros civiles de Afros")
    registro_civil_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Registros civiles de Otros")
    """ salud """
    vacunacion_cobertura_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    vacunacion_cobertura_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    vacunacion_cobertura_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    """ Programa Crecimiento y Desarrollo """
    pcd_cobertura_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    pcd_cobertura_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    pcd_cobertura_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    """ Afiliacion a salud """
    reg_sub_carnetizado_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen subsidiado carnetizado indigena")
    reg_sub_carnetizado_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen subsidiado carnetizado afro")
    reg_sub_carnetizado_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen subsidiado carnetizado otros")
    
    reg_contrib_vinculado_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen contributivo vinculado indigena")
    reg_contrib_vinculado_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen contributivo vinculado afro")
    reg_contrib_vinculado_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen contributivo vinculado otros")
    
    reg_contributivo_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen contributivo  indigena")
    reg_contributivo_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen contributivo afro")
    reg_contributivo_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Regimen contributivo otros")
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "indicadores basicos de derechos de primera infancia"
        verbose_name = "indicador basico de derechos de primera infancia"
    
class ProgramaSeguridadAlimentaria(models.Model):
    derecho = models.ForeignKey(DerechoPrimeraInfancia, related_name="programas")
    descripcion = models.TextField(null=True, blank=True)
    cobertura = models.CharField(max_length=50, choices=(("indigena","Indigena"),("afro","Afro"),("otro","Otro")) )
    monto = models.CharField(max_length=50, null=True, blank=True)
    duracion = models.CharField(max_length=50, null=True, blank=True)
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "programas de seguridad alimentaria"
    
class DerechoAlTrabajo(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_4")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")
    
    desempleo_informal = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    empleo_formal_publico = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    empleo_formal_privado = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    empleo_formal_por_contrado_fijo = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    empleo_formal_por_contrado_temporal = models.DecimalField(help_text="en % (Porcentaje)", max_digits=5, decimal_places=2, null=True, blank=True)
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "indicadores basicos de derecho al trabajo"
        verbose_name = "indicador basicos de derecho al trabajo"
    
class DerechoCultura(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_5")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")
    """ Programas de Protección y Promoción del patrimonio cultural """
    pc_indigenas = models.BooleanField(verbose_name="Tiene Programas de Protección y Promoción del patrimonio cultural en pueblos indigenas?")
    pc_indigenas_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    pc_afro = models.BooleanField(verbose_name="Tiene Programas de Protección y Promoción del patrimonio cultural en pueblos afros?")
    pc_afro_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    """ Programas de acceso a los medios de comunicacion """
    pamc_indigenas = models.BooleanField(verbose_name="Tiene Programas de acceso a los medios de comunicacion en pueblos indigenas?")
    pamc_indigenas_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    pamc_afro = models.BooleanField(verbose_name="Tiene Programas de acceso a los medios de comunicacion en pueblos afros?")
    pamc_afro_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    """ Programas de protección y promoción de lenguas indígenas """
    pl_indigenas = models.BooleanField(verbose_name="Tiene Programas de protección y promoción de lenguas en pueblos indigenas?")
    pl_indigenas_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    
    existencia_tr_indigenas_juzgado = models.CharField(max_length=50, null=True, blank=True, verbose_name="Existencia de traductores indígenas en juzgados")
    existencia_tr_indigenas_hospitales = models.CharField(max_length=50, null=True, blank=True, verbose_name="Existencia de traductores indígenas en hospitales")
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    """ Proyectos Educativos """
    """con_bilinguismo_indigena = models.BooleanField()
    con_bilinguismo_instituciones = models.TextField(blank=True, null=True, verbose_name="Instituciones con bilinguismo indigena", help_text="Solo si marco la casilla anterior. Separadas por coma")
    con_bilinguismo_descripcion = models.TextField(blank=True, null=True, verbose_name="Descripcion", help_text="Solo si marco la casilla anterior. Separadas por coma")"""
    
    class Meta:
        verbose_name_plural = "indicadores basicos de derecho a la cultura"
        verbose_name = "indicador basico de derecho a la cultura"
    
class ProyectoEducativos(models.Model):
    derecho = models.ForeignKey(DerechoCultura, related_name="proyectos_educativos")
    tipo = models.CharField(max_length=100, choices=(("bi","Bilingüismo Indígena"),("ipi", "Interculturalidad en los pueblos indígenas"),("ica","Interculturalidad en las comunidades afro")), null=True, blank=True )
    tiene = models.BooleanField(verbose_name="Tiene?", help_text="Marque la casilla si responde SI")
    instituciones = models.TextField(blank=True, null=True, verbose_name="Instituciones con bilinguismo indigena", help_text="Solo si marco la casilla anterior. Separadas por coma")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripcion", help_text="Solo si marco la casilla anterior. Separadas por coma")
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "proyectos educativos culturales"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

       

