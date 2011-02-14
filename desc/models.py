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

    ingresos_publicos_per_capita = models.IntegerField(null=True, blank=True)
    fuente_ingreso_per_capita = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="per")
    indice_desarrollo_humano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    fuente_indice_desarrollo_humano = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="desa")
    necesidades_basicas_insatisfechas_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    necesidades_basicas_insatisfechas_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    necesidades_basicas_insatisfechas_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    fuente_necesidades_basicas_insatisfechas = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="insat")
    indice_condiciones_de_vida= models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    fuente_indice_condiciones_de_vida = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="condic")
    
    """ servicios publicos """
    cobertura_acueducto_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    cobertura_acueducto_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo municipios
    cobertura_acueducto_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo municipios
    
    cobertura_alcantarillado_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    cobertura_alcantarillado_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo municipios
    cobertura_alcantarillado_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo municipios
    
    cobertura_energia_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo municipios
    cobertura_energia_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo municipios
    cobertura_energia_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo municipios
    
    fuente_servicios_publicos = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="servicios_publicos")
    
    """ esperanza de vida """
    esperanza_vida_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo dptos
    esperanza_vida_mujeres = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo dptos
    esperanza_vida_hombres = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True) #solo dptos
    fuente_esperanza_vida = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="bb")
    
    mortalidad_total = models.FloatField(help_text="en % (Porcentaje)", null=True, blank=True) #solo dptos
    mortalidad_infantil = models.FloatField(help_text="en % (Porcentaje)", null=True, blank=True)
    mortalidad_maternoinfantil = models.FloatField(help_text="en % (Porcentaje)", null=True, blank=True)
    
    fuente_mortalidad = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="bbb")

    morbilidad_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion morbilidad")
    morbilidad_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Porcentaje de morbilidad")
    morbimortalidad_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion morbi-mortalidad")
    morbimortalidad_porcentaje = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Porcentaje de morbi-motalidad")
    
    fuente_morbilidad = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="bbbb")

    alfabetizacion_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Tasa de alfabetizacion total") 
    alfabetizacion_urbano = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Tasa de alfabetizacion urbana") 
    alfabetizacion_rural = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Tasa de alfabetizacion rural")
    
    fuente_alfabetizacion = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="bbbbb")
    
    matricula_total = models.IntegerField(null=True, blank=True, help_text="numero total")
    fuente_matricula = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="bbbbbb")
    
    class Meta:
        verbose_name_plural = "indicadores basicos"
        
class Educacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_1")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey()

    nivel_educativo_preescolar = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Preescolar") 
    nivel_educativo_primaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Basica primaria") 
    nivel_educativo_secundaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Basica secundaria")
    
    nivel_educativo_mediatec = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Media Vocacional - tecnica")
    nivel_educativo_normalista = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Media Vocacional - Normalista")
    nivel_educativo_media_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Total Media Vocacional")
    
    nivel_educativo_sup_tecnica = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Superior tecnica")
    nivel_educativo_sup_tecnologica  = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Superior tecnologica")
    nivel_educativo_sup_profesional = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Superior profesional")
    nivel_educativo_sup_total = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Superior total")
    
    instituciones_total = models.IntegerField(null=True, blank=True, help_text="numero total de instituciones educativas") #todo: hacerlo como propiedad count InstitucionEducativa
    
    fuente_nivel_educativo = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="niveles_educativos")
    """ maestros """
    maestros_vinculados_indigenas = models.IntegerField(null=True, blank=True, verbose_name="indigenas", help_text="cantidad")
    maestros_vinculados_afro = models.IntegerField(null=True, blank=True, verbose_name="afro", help_text="cantidad")
    maestros_vinculados_otros = models.IntegerField(null=True, blank=True, verbose_name="otros", help_text="cantidad")
    maestros_vinculados_ejerciendo = models.IntegerField(null=True, blank=True, verbose_name="en ejercicio", help_text="cantidad")
    maestros_vinculados_total = models.IntegerField(null=True, blank=True, verbose_name="TOTAL de maestros vinculados", help_text="cantidad")

    maestros_contratados_indigenas = models.IntegerField(null=True, blank=True, verbose_name="indigenas", help_text="cantidad")
    maestros_contratados_afro = models.IntegerField(null=True, blank=True, verbose_name="afro", help_text="cantidad")
    maestros_contratados_otros = models.IntegerField(null=True, blank=True, verbose_name="otros", help_text="cantidad")
    maestros_contratados_ejerciendo = models.IntegerField(null=True, blank=True, verbose_name="en ejercicio", help_text="cantidad")
    maestros_contratados_total = models.IntegerField(null=True, blank=True, verbose_name="TOTAL de maestros contratados", help_text="cantidad")

    maestros_nombrados_indigenas = models.IntegerField(null=True, blank=True, verbose_name="indigenas", help_text="cantidad")
    maestros_nombrados_afro = models.IntegerField(null=True, blank=True, verbose_name="afro", help_text="cantidad")
    maestros_nombrados_otros = models.IntegerField(null=True, blank=True, verbose_name="otros", help_text="cantidad")
    maestros_nombrados_ejerciendo = models.IntegerField(null=True, blank=True, verbose_name="en ejercicio", help_text="cantidad")
    maestros_nombrados_total = models.IntegerField(null=True, blank=True, verbose_name="TOTAL de maestros vinculados", help_text="cantidad")

    fuente_maestros = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_maestros")

    """poblacion estudiantil"""
    cobertura_preescolar = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    cobertura_primaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Cobertura básica primaria")
    cobertura_secundaria = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Cobertura básica secundaria")
    cobertura_mediavocacional = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    total_poblacion_estudiantil = models.DecimalField(help_text="en % (Porcentage)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Cobertura total de poblacion estudiantil")


    fuente_poblacion_estudiantil = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_pobestudiantil")

    cobertura_preescolar_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    cobertura_primaria_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Cobertura básica primaria desplazados")
    cobertura_secundaria_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Cobertura básica secundaria desplazados")
    cobertura_mediavocacional_desplazados = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    total_poblacion_estudiantil_desplazada = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Cobertura total de poblacion estudiantil deplazada")


    fuente_poblacion_estudiantil_desplazados = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_pobestudiantildes")

    desercion = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    promocion = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    repitencia = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    analfabetismo = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)

    fuente_poblacion_estudiantil_otros = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuente_pobestudiantiliotro")
    
    
    class Meta:
        verbose_name_plural = "Educación"
        verbose_name = "Educación"

    def __unicode__(self):
        return "DESC de %s" % (self.content_object.nombre)

    def get_total_instituciones(self):
        return self.instituciones.all().count()
    total_instituciones = property(get_total_instituciones)

    def get_nombre_municipio(self):
        return self.content_object.nombre
    municipio = property(get_nombre_municipio)

class InstitucionEducativa(models.Model):
    indicador_educacion = models.ForeignKey(Educacion, related_name="instituciones")
    nombre = models.CharField(max_length=200)
    es_publica = models.BooleanField(help_text="Desmarque si es privada", default=True)
    fecha_constitucion = models.DateField(blank=True, null=True)
    enfasis = models.CharField(max_length=200,blank=True, null=True)
    etnoeducacion = models.BooleanField()
    tiene_pei = models.BooleanField(help_text="tiene Proyecto Educativo Institucional")
    tiene_pec = models.BooleanField(help_text="tiene Proyecto Educativo Comunitario")
    educa_adultos = models.BooleanField(verbose_name="Educacion para adultos", help_text="Seleccione si la institucion educa adultos")
    #depende de Educacion de personas adultas:
    adultos = models.DecimalField(help_text="porcentaje de adultos entre los alumnos de la institucion", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Educacion de personas adultas")
    
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="instituciones")
    
    class Meta:
        verbose_name_plural = "instituciones educativas"

    def __unicode__(self):
        return "%s (Municipio: %s)" % (self.nombre, self.indicador_educacion.content_object.nombre)

#    def total_maestros_vinculados(self):
#        return self.maestros_vinculados_indigenas + self.maestros_vinculados_afro + self.maestros_vinculados_ejerciendo + self.maestros_vinculados_otros
#    tmv = property(total_maestros_vinculados)

class SistemaSalud(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_2")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey()
    
    """ Régimen subsidiado carnetizado """
    reg_sub_carnetizado_total_porcentaje = models.DecimalField(help_text="% de la poblacion total del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion total")
    reg_sub_carnetizado_indigena_porcentaje = models.DecimalField(help_text="% de indigenas del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion indigena")
    reg_sub_carnetizado_indigena_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_carnetizado_afro_porcentaje = models.DecimalField(help_text="% de afros del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion afro")
    reg_sub_carnetizado_afro_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_carnetizado_otra_porcentaje = models.DecimalField(help_text="% de otros del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Otra poblacion")
    reg_sub_carnetizado_otra_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    """ Régimen subsidiado vinculado """
    reg_sub_vinculado_total_porcentaje = models.DecimalField(help_text="% de la poblacion total del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion total")
    reg_sub_vinculado_indigena_porcentaje = models.DecimalField(help_text="% de indigenas del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion indigena")
    reg_sub_vinculado_indigena_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_vinculado_afro_porcentaje = models.DecimalField(help_text="% de afros del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion afro")
    reg_sub_vinculado_afro_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_sub_vinculado_otra_porcentaje = models.DecimalField(help_text="% de otros del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Otra poblacion")
    reg_sub_vinculado_otra_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    """ Régimen contributivo """

    reg_contributivo_total_porcentaje = models.DecimalField(help_text="% de la poblacion total del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion total")
    reg_contributivo_indigena_porcentaje = models.DecimalField(help_text="% de indigenas del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion indigena")
    reg_contributivo_indigena_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_contributivo_afro_porcentaje = models.DecimalField(help_text="% de afros del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Poblacion afro")
    reg_contributivo_afro_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    reg_contributivo_otra_porcentaje = models.DecimalField(help_text="% de otros del municipio", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Otra poblacion")
    reg_contributivo_otra_empresas = models.TextField(null=True, blank=True, verbose_name="Nombre de empresas prestadoras", help_text="separadas por coma")
    
    fuente_regimenes = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fregs")

    def get_cantidad_promotores_salud(self):
        return self.promotores_salud.all().aggregate(total=models.Sum('promotores'))['total']
    total_promotores_de_salud = property(get_cantidad_promotores_salud)

    def get_cantidad_entidades_contratantes(self):
        return self.promotores_salud.all().count()
    entidades_contratantes = property(get_cantidad_entidades_contratantes)

    def get_nombre_municipio(self):
        return self.content_object.nombre
    municipio = property(get_nombre_municipio)

    def get_cantidad_contratos_temporal(self):
        return self.promotores_salud.filter(tipo_contrato='temporal').count()
    contratos_temporales = property(get_cantidad_contratos_temporal)

    def get_cantidad_contratos_fijo(self):
        return self.promotores_salud.filter(tipo_contrato='fijo').count()
    contratos_fijos = property(get_cantidad_contratos_fijo)

    def get_total_puestos_salud(self):
        return self.instalaciones_salud.filter(tipo='puesto').count()
    puestos_de_salud = property(get_total_puestos_salud)

    def get_total_centros_salud(self):
        return self.instalaciones_salud.filter(tipo='centro').count()
    centros_de_salud = property(get_total_centros_salud)

    def get_total_hospitales(self):
        return self.instalaciones_salud.filter(tipo='hospital').count()
    total_hospitales = property(get_total_hospitales)

    class Meta:
        verbose_name_plural = "Sistemas de salud"
        verbose_name = "sistema de salud"
    
class PromotoresSalud(models.Model):
    sistema_salud = models.ForeignKey(SistemaSalud, related_name="promotores_salud")
    nombre = models.CharField(max_length=200,null=True, blank=True, verbose_name="Nombre de entidad")
    promotores = models.IntegerField(null=True, blank=True, help_text="total", default=0)
    tipo_contrato = models.CharField(max_length=50, choices=(("temporal","Temporal"),("fijo","Fijo")) )
    numero_contrato = models.IntegerField(null=True, blank=True)
    
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "promotores de salud"
        verbose_name = "promotores de salud - entidad contratante"

    def __unicode__(self):
        return '%s (contrato: %s)' % (self.nombre, self.tipo_contrato)
        
class InstalacionesSalud(models.Model):
    sistema_salud = models.ForeignKey(SistemaSalud, related_name="instalaciones_salud")
    tipo = models.CharField(max_length=50, choices=(("centro","Centro de salud"),("puesto","Puesto de salud"),("hospital","Hospital")))
    nombre = models.CharField(max_length=200,null=True, blank=True)
    ubicacion = models.CharField(max_length=200,null=True, blank=True) #todo geo
    nivel_de_atencion = models.IntegerField(null=True, blank=True, choices=((1,"1"),(2,"2"),(3,"3")), help_text="solo si selecciono hospital como tipo de instalacion" )
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "instalaciones de salud"

    def __unicode__(self):
        return '%s: %s' % (self.tipo, self.nombre)
        
class DerechoPrimeraInfancia(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_3")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")
    
    """proteccion"""
    registro_civil = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Total de registros civiles")
    registro_civil_indigena = models.DecimalField(help_text="porcentaje de indigenas del municipio en edad de primera infancia", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Registros civiles de Indigenas")
    registro_civil_afro = models.DecimalField(help_text="porcentaje de afros del municipio en edad de primera infancia", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Registros civiles de Afros")
    registro_civil_otros = models.DecimalField(help_text="porcentaje de otros del municipio en edad de primera infancia", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Registros civiles de Otros")
    fuente_registro_civil = models.ForeignKey(FuenteDato, null=True, blank=True, related_name='fuente_registro_civil')
    
    """ salud """
    vacunacion_cobertura_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    vacunacion_cobertura_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    vacunacion_cobertura_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    vacunacion_covertura_total = models.IntegerField(verbose_name='total', null=True, blank=True)
    fuente_vacunacion = models.ForeignKey(FuenteDato, null=True, blank=True, related_name='fuente_vacunacion')
    
    """ Programa Crecimiento y Desarrollo """
    pcd_cobertura_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    pcd_cobertura_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    pcd_cobertura_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    pcd_cobertura_total = models.IntegerField(verbose_name='total', null=True, blank=True)
    fuente_crecimiento_y_desarrollo = models.ForeignKey(FuenteDato, null=True, blank=True, related_name='fuentes_coberturas')

    """ Afiliacion a salud """
    reg_sub_carnetizado_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen subsidiado carnetizado indigena")
    reg_sub_carnetizado_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen subsidiado carnetizado afro")
    reg_sub_carnetizado_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen subsidiado carnetizado otros")
    reg_sub_carnetizado_total = models.IntegerField(verbose_name='total', null=True, blank=True)

    reg_contrib_vinculado_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen contributivo vinculado indigena")
    reg_contrib_vinculado_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen contributivo vinculado afro")
    reg_contrib_vinculado_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen contributivo vinculado otros")
    reg_contrib_vinculado_total = models.IntegerField(verbose_name='total', null=True, blank=True)

    reg_contributivo_indigena = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen contributivo  indigena")
    reg_contributivo_afro = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen contributivo afro")
    reg_contributivo_otros = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Regimen contributivo otros")
    reg_contributivo_total = models.IntegerField(verbose_name='total', null=True, blank=True)
    fuente_afiliacion_salud = models.ForeignKey(FuenteDato, null=True, blank=True, related_name='fuentes_regimen')

    
    class Meta:
        verbose_name_plural = "Derechos de primera infancia"
        verbose_name = "Derecho de primera infancia"
    
class ProgramaSeguridadAlimentaria(models.Model):
    derecho = models.ForeignKey(DerechoPrimeraInfancia, related_name="programas")
    nombre = models.CharField(max_length=200,null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    monto = models.CharField(help_text="Millones de pesos", max_length=50, null=True, blank=True)
    duracion = models.CharField(max_length=50, null=True, blank=True)

    cobertura_total = models.IntegerField(null=True, blank=True, help_text="% de población del municipio en edad de primera infancia")
    cobertura_indigena = models.IntegerField(null=True, blank=True, help_text="% de población indigena en edad de primera infancia")
    cobertura_afro = models.IntegerField(null=True, blank=True, help_text="% de población afro en edad de primera infancia")
    cobertura_otros = models.IntegerField(null=True, blank=True, help_text="% de población otros en edad de primera infancia")

    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "programas de seguridad alimentaria"
    
class DerechoAlTrabajo(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_4")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")
    
    desempleo = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    trabajo_informal = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    trabajo_formal = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="Trabajo formal (Empleo)")

    empleo_formal_publico = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    empleo_formal_privado = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    empleo_formal_por_contrado_fijo = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    empleo_formal_por_contrado_temporal = models.DecimalField(help_text="en % (Porcentaje)", max_digits=4, decimal_places=1, null=True, blank=True)
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Derecho al trabajo"
        verbose_name = "Derechos al trabajo"
    
class DerechoCultura(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_5")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey("tipo_de_territorio", "codigo")
    """ Programas de Protección y Promoción del patrimonio cultural """
    pc_indigenas = models.BooleanField(verbose_name="Tiene Programas de Protección y Promoción del patrimonio cultural en pueblos indigenas?")
    pc_indigenas_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    pc_afro = models.BooleanField(verbose_name="Tiene Programas de Protección y Promoción del patrimonio cultural en comunidades afros?")
    pc_afro_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    fuente_pc = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuentes_pc", verbose_name="Fuente")
    """ Programas de acceso a los medios de comunicacion """
    pamc_indigenas = models.BooleanField(verbose_name="Tiene Programas de acceso a los medios de comunicacion en pueblos indigenas?")
    pamc_indigenas_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    pamc_afro = models.BooleanField(verbose_name="Tiene Programas de acceso a los medios de comunicacion en comunidades afros?")
    pamc_afro_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    fuente_pamc = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuentes_pamc", verbose_name="Fuente")
    """ Programas de protección y promoción de lenguas indígenas """
    pl_indigenas = models.BooleanField(verbose_name="Tiene Programas de protección y promoción de lenguas en pueblos indigenas?")
    pl_indigenas_descripcion = models.TextField(null=True, blank=True, verbose_name="Descripcion del programa", help_text="Solo si marco la casilla anterior")
    fuente_pl = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuentes_pl", verbose_name="Fuente")
    
    existen_tr_indigenas_juzgado = models.BooleanField(help_text="Seleccione casilla si existen", verbose_name="Existen traductores indígenas en juzgados?")
    total_tr_indigenas_juzgado = models.CharField(max_length=50, null=True, blank=True, verbose_name="Total", help_text="si selecciono la casilla anterior")
    existen_tr_indigenas_hospitales = models.BooleanField(help_text="Seleccione casilla si existen", verbose_name="Existen traductores indígenas en hospitales?")
    total_tr_indigenas_hospitales = models.CharField(max_length=50, null=True, blank=True, verbose_name="total", help_text="si selecciono la casilla anterior")
    fuente_tr = models.ForeignKey(FuenteDato, null=True, blank=True, related_name="fuentes_tl", verbose_name="Fuente")
    
    class Meta:
        verbose_name_plural = "Derecho a la cultura"
        verbose_name = "Derechos a la cultura"
    
class ProyectoEducativo(models.Model):
    derecho = models.ForeignKey(DerechoCultura, related_name="proyectos_educativos")
    tipo = models.CharField(max_length=100,default="bi", choices=(("bi","Bilingüismo Indígena"),("ipi", "Interculturalidad en los pueblos indígenas"),("ica","Interculturalidad en las comunidades afro")), verbose_name="Seleccione proyecto" )
    tiene = models.BooleanField(verbose_name="Existe este programa?", help_text="Marque la casilla si responde SI")
    instituciones = models.TextField(blank=True, null=True, verbose_name="Instituciones educativas", help_text="Solo si marco la casilla anterior. Separadas por coma")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripcion", help_text="Solo si marco la casilla anterior. Separadas por coma")
    
    fuente= models.ForeignKey(FuenteDato, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "proyectos educativos culturales"
