# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato
from territorios.models import TerritorioComunidad
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
IMPACTOS = (
    ("","Impacto Ambiental / Suelos"),
    ("","Impacto Ambiental / Rios"),
    ("","Impacto Ambiental / Quebradas"),
    ("","Impacto Ambiental / Cultivos"),
    ("","Impacto Ambiental / Bosques"),
    ("","Impacto Ambiental / Manglares"),
    ("","Impacto Ambiental / Payas"),
    ("","Impacto Ambiental / Nacimiento de agua"),
    ("","Impacto Ambiental / Fauna"),
    ("","Impacto Ambiental / Aire"),
    ("","Impacto Ambiental / Ruido"),
    ("","Impacto Ambiental / Otro"),
    ("","Impactos culturales / Forma de autoridad"),
    ("","Impactos culturales / Fiestas"),
    ("","Impactos culturales / Lengua"),
    ("","Impactos culturales / Comida"),
    ("","Impactos culturales / Cambios de proyecto de vida"),
    ("","Impactos culturales / Otro"),
    ("","Impactos económicos / Ingreso"),
    ("","Impactos económicos / Relaciones laborales"),
    ("","Impactos económicos / Sistema productivo"),
    ("","Impactos económicos / Otro"),
    ("","Impactos sociales / Salud"),
    ("","Impactos sociales / Educación"),
    ("","Impactos sociales / Cambio de roles"),
    ("","Impactos sociales / Movilidad de la población"),
    ("","Impactos sociales / Conflictos - Interetnicos"),
    ("","Impactos sociales / Conflictos - Intraetnicos"),
    ("","Impactos sociales / Conflictos - Otros actores"),
    ("","Impactos sociales / Otro"),
    ("","Impactos en las organizaciones / División"),
    ("","Impactos en las organizaciones / Cambios de objetivos"),
    ("","Impactos en las organizaciones / Corrupción"),
    ("","Impactos en las organizaciones / Perdida de legitimidad"),
    ("","Impactos en las organizaciones / Otro"),
    ("","Territorio Colectivo Indígena titulado / Cambio de uso"),
    ("","Territorio Colectivo Indígena titulado / Formas de despojo"),
    ("","Territorio Colectivo Indigena no titulado / Cambio de uso"),
    ("","Territorio Colectivo Indigena no titulado / Formas de despojo"),
    ("","Territorio Colectivo Comunidades Negras titulado / Cambio de uso"),
    ("","Territorio Colectivo Comunidades Negras titulado / Formas de despojo"),
    ("","Territorio Colectivo Comunidades Negras no titulado / Cambio de uso"),
    ("","Territorio Colectivo Comunidades Negras no titulado / Formas de despojo"),
    ("","Territorios / Areas protegidas - Parque nacional; Santuario de Fauna y Flora"),
    ("","Territorios / Otros"),
)
CUBRIMIENTO_INSTITUCIONES_FINANCIADORAS = (
    ("nacional","Nacional"),
    ("internacional","Internacional"),
)
TIPO_INSTITUCIONES_FINANCIADORAS = (
    ("publica","Pública"),
    ("privada","Privada"),
)
TIPO_CONTRATACIONES_PUBLICAS = (
    ("convocatoria","Convocatoria pública para el proyecto concreto"),
    ("ajudicacion","Ajudicación del proyecto"),
)
TIPOS_MEGAPROYECTOS_OBRAS_INFRAESTRUCTURA = (
    ("maritimo-portuario-nacional","Marítimo y Portuario / Nacional (Licencia Ambiental del Ministerio del Medio Ambiente, Vivienda y Desarrollo TerritorialLA-MAVDT)"),
    ("maritimo-portuario-regional","Marítimo y Portuario / Regional (Licencia Ambiental de la Corporación Autónoma Regional LA-CAR)"),
    ("aereopuertos-internacionales","Aeropuertos / Internacionales y de nuevas pistas (dentro del aeropuerto internacional) (LA-MAVDT)"),
    ("aereopuertos-nacionales","Aeropuertos / Nacionales y de nuevas pistas (dentro del aeropuerto nacional) (LA-CAR)"),
    ("red-vial-nac-mantenimientos-rehabilitacion","Red vial nacional / Mejoramiento y rehabilitación de vías (CAR)"),
    ("red-vial-nac-construccion","Red vial nacional / Construcción y mantenimiento de puentes (CAR)"),
    ("red-vial-sec-mantenimientos-rehabilitacion","Red vial Secundaria y terciaria / Mejoramiento y rehabilitación de vías (CAR)"),
    ("red-vial-sec-construccion","Red vial Secundaria y terciaria / Construcción y mantenimiento de puentes (CAR)"),
    ("red-fluvial-nac-opub-construccion-puertos","Red fluvial nacional / Obras públicas (LA-MAVDT) - Construcción de puertos"),
    ("red-fluvial-nac-opub-cierre-brazos","Red fluvial nacional / Obras públicas (LA-MAVDT) - Cierre de brazos"),
    ("red-fluvial-nac-opub-dragados","Red fluvial nacional / Obras públicas (LA-MAVDT) - Dragados de profundización"),
    ("red-fluvial-nac-opriv-construccion-puertos","Red fluvial nacional / Obras de carácter privado (LA-CAR) - Construcción de puertos"),
    ("red-fluvial-nac-opriv-cierre-brazos","Red fluvial nacional / Obras de carácter privado (LA-CAR) - Cierre de brazos"),
    ("red-fluvial-nac-opriv-dragados","Red fluvial nacional / Obras de carácter privado (LA-CAR) - Dragados de profundización"),
    ("red-ferrea-nacional","Red férrea / nacional y variantes (LA-MAVDT)"),
    ("red-ferrea-regional","Red férrea / regional y variantes (LA-CAR)"),
    ("distritos-riego-mayor-20000h","Distritos de riego / Mayor de 20.000 hectáreas (LA-MAVDT)"),
    ("distritos-riego-entre-5000-20000h","Distritos de riego / Entre 5000 a 20.000 hectáreas (LA-CAR)"),
    ("tratamiento-aguas-res-mayor-200000h","Sistema de tratamiento de aguas residuales / Igual o mayor a 200.000 habitantes (LA-CAR)"),
    ("tratamiento-aguas-res-menor-200000h","Sistema de tratamiento de aguas residuales / Menor de 200.000 habitantes (Plan de Manejo – Municipio)"),
    ("rellenos-sustancias-peligrosas","Rellenos sanitarios (LA-CAR) / Sustancias peligrosas"),
    ("rellenos-area-suceptible-de-titulacion","Rellenos sanitarios (LA-CAR) / En área susceptibles de titulación"),
    ("rellenos-contigua-a-areas-tituladas","Rellenos sanitarios (LA-CAR) / Contigua a áreas tituladas"),
    ("megaproyecots-vivienda","Macroproyectos de Vivienda"),
    ("sector-electrico-hidroelectricas-represas-mayor-200m-m2","Sector Eléctrico / Hidroélectricas - Construcción de presas, represas o embalses con capacidad mayor de 200 millones de metros cúbicos de agua. (LA-MAVDT)"),
    ("sector-electrico-hidroelectricas-represas--menor-200m-m2","Sector Eléctrico / Hidroélectricas - Construcción de presas, represas o embalses con capacidad igual o inferior a 200 millones de metros cúbicos de agua (LA-CAR)"),
    ("sector-electrico-lineas-1","Sector Eléctrico / Lineas - Lineas de transmisión del sistema nacional de interconexión eléctrica, compuesto por el conjunto de líneas con subestaciones que operen a tensiones iguales o superiores a 220 KW. (LA-MAVDT)"),
    ("sector-electrico-lineas-2","Sector Eléctrico / Lineas - Lineas del sistema de transmisión conformado por el conjunto de líneas con sus equipos asociados, que operan a tensiones menores de 220 KV y que no pertenecen a un sistema de distribución local. (LA-CAR)"),
    ("sector-electrico-termoelectricas-1","Sector Eléctrico / Termoeléctricas - Termoeléctricas"),
    ("sector-electrico-termoelectricas-2","Sector Eléctrico / Termoeléctricas - Capacidad mayor o igual a 10MW y menor de 100MW (LA-CAR)"),
    ("sector-electrico-generadores-1","Sector Eléctrico / Centrales Generadoras de Energia Eléctrica - Capacidad igual o superior a 100mw (LA-MAVDT)"),
    ("sector-electrico-generadores-2","Sector Eléctrico / Centrales Generadoras de Energia Eléctrica - Capacidad menor de 100mw (LA-CAR)"),
    ("sector-electrico-fuentes","Sector Eléctrico / Uso de fuentes de energías alternativas virtualmente contaminantes (LA-MAVDT)"),
)

class Afectacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_afectacion")
    object_id = models.PositiveIntegerField(blank=True, null=True)

    content_object = generic.GenericForeignKey()

    tipo = models.CharField(max_length=100, choices=IMPACTOS)
    territorio = models.ForeignKey(TerritorioComunidad, null=True, blank=True, help_text='Solo si selecciono afectacion de Territorio Colectivo')
    descripcion = models.TextField()

    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Afectacion'

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

class Proyecto(models.Model):
    """ Información general """
    municipios = models.ManyToManyField(Municipio, related_name='municipios')
    territorios = models.ManyToManyField(TerritorioComunidad, null=True, blank=True, related_name='territorios')
    area_terrestre = models.CharField(max_length=255, null=True, blank=True)
    area_maritima = models.CharField(max_length=255, null=True, blank=True)
    fecha_iniciacion = models.DateField()
    fecha_finalizacion = models.DateField(null=True, blank=True)
    """ Empresa propietaria"""
    empresa_nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre')
    empresa_representante_legal = models.CharField(max_length=255, null=True, blank=True, verbose_name='Representante legal')
    empresa_accionistas_nacionales = models.BooleanField(verbose_name='Tiene accionistas nacioinales?')
    empresa_accionistas_extranjeros = models.BooleanField(verbose_name='Tiene accionistas en el extranjero?')
    empresa_en_colombia = models.BooleanField(verbose_name='Esta empresa opera en Colombia?')
    empresa_en_extranjero = models.BooleanField(verbose_name='Esta empresa opera en el Extranjero?')
    empresa_otras_actividades = models.BooleanField(verbose_name='Esta empresa tiene otras actividades?')
    empresa_otras_actividades_descripcion = models.TextField(null=True, blank=True, help_text='En caso de que tenga otras actividades', verbose_name='Descripción')
    monto_inversion = models.IntegerField(null=True, blank=True, help_text='Monto de inversión')

    class Meta:
        abstract = True

class InstitucionFinanciadora(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_instituciones")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    cubrimiento = models.CharField(max_length=255, null=True, blank=True, choices=CUBRIMIENTO_INSTITUCIONES_FINANCIADORAS)
    tipo = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_INSTITUCIONES_FINANCIADORAS)
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Instituciones Financiadoras'

class EstadoEjecucion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_estadosejecucion")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()
    """Contratación pública"""
    contratacion_publica = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_CONTRATACIONES_PUBLICAS)
    """ Desarrollo del proyecto """
    fecha_iniciacion = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)
    subcontratista = models.BooleanField(help_text='Tiene subcontratista?')
    subcontratista_nombre_empresa = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre subcontratista')
    subcontratista_objeto = models.TextField(null = True, blank = True, verbose_name='Objeto del subcontratista')
    cesion = models.BooleanField(help_text='Tiene cesión?')
    cesion_nuevo_titular = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nuevo titular de la cesion')
    suspension = models.BooleanField(help_text='Tiene suspensión?')
    suspension_causa = models.CharField(max_length=255, null=True, blank=True, help_text='explique el porqué', verbose_name='Causa de suspensión')
    revocatoria = models.BooleanField(help_text='Tiene revocatoria?')
    revocatoria_causa = models.CharField(max_length=255, null=True, blank=True, help_text='explique el porqué', verbose_name='Causa de revocatoria')

    class Meta:
        verbose_name_plural = 'Estados de ejecución'

class RequisitoLegal(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_requisitos")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()
    """ CONSULTA PREVIA """
    consulta_previa = models.BooleanField(help_text='Se realizo consulta previa?')
    acta_acuerdo = models.FileField(upload_to="uploads/actas_de_acuerdo", null = True, blank = True, verbose_name='acta de acuerdo')
    acta_acuerdo_fecha = models.DateField(null = True, blank = True, verbose_name='fecha')
    acta_acuerdo_suscriptor = models.CharField(max_length=255, null=True, blank=True, verbose_name='quien la suscribe')
    metodologia = models.TextField(null = True, blank = True, verbose_name='Descripción de metodologia')
    participacion = models.TextField(null = True, blank = True, verbose_name='Descripción de participación')
    cumplimientos_acuerdo = models.TextField(null = True, blank = True, verbose_name='Descripción de cumplimientos de acuerdo')
    """ LICENCIA AMBIENTAL """
    impacto_ambiental = models.TextField(null=True, blank=True, verbose_name='LICENCIA AMBIENTAL - descripcion de impacto ambiental')
    impacto_cultural = models.TextField(null=True, blank=True, verbose_name='descripcion de impacto cultural')
    impacto_socioeconomico = models.TextField(null=True, blank=True, verbose_name='descripcion de impacto socioeconomico')
    medidas_prevencion = models.TextField(null=True, blank=True, verbose_name='descripcion de medidas de prevención', help_text='plan de manejo ambiental')
    medidas_mitigacion = models.TextField(null=True, blank=True, verbose_name='descripcion de medidas de mitigación', help_text='plan de manejo ambiental')
    medidas_correccion = models.TextField(null=True, blank=True, verbose_name='descripcion de medidas de correción', help_text='plan de manejo ambiental')
    medidas_compensacion = models.TextField(null=True, blank=True, verbose_name='descripcion de medidas de compensación', help_text='plan de manejo ambiental')
    plan_de_manejo = models.TextField(null=True, blank=True, verbose_name='descripcion del plan de manejo')

    class Meta:
        verbose_name_plural = 'Requicitos legales'

class VinculacionPoblacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_vinculaciones")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()
    """ Empleo """
    empleo_compromiso_consulta_previa = models.BooleanField(verbose_name='compromiso de consulta previa para empleos')
    local = models.BooleanField(verbose_name='Empleo local')
    local_numero = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nº')
    local_tipo_actividades = models.TextField(null = True, blank = True, verbose_name='Descripción de tipo de actividad')
    local_forma_pago = models.CharField(max_length=255, null=True, blank=True, verbose_name='Forma de pago')

    otraregion = models.BooleanField(verbose_name='Empleo de otra región')
    otraregion_numero = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nº')
    otraregion_tipo_actividades = models.TextField(null = True, blank = True, verbose_name='Descripción de tipo de actividad')
    otraregion_forma_pago = models.CharField(max_length=255, null=True, blank=True, verbose_name='Forma de pago')
    """Programas sociales"""
    programas_compromiso_consulta_previa = models.BooleanField(verbose_name='compromiso de consulta previa para programas sociales')
    programa_educacion_monto = models.IntegerField(null = True, blank = True, verbose_name='Monto para Educacion')
    programa_infraestructura_monto = models.IntegerField(null = True, blank = True, verbose_name='Monto para Infraestructura')
    programa_salud_monto = models.IntegerField(null = True, blank = True, verbose_name='Monto para Salud')
    programa_produccion_monto = models.IntegerField(null = True, blank = True, verbose_name='Monto para Produccion')
    programa_otros_monto = models.IntegerField(null = True, blank = True, verbose_name='Monto para Otros')
    programa_otros_cuales = models.CharField(max_length=255, null=True, blank=True, verbose_name='cuales', help_text='En caso de haber llenado el campo anterior')
    """ Subsidios """
    subsidios_consulta_previa = models.BooleanField(verbose_name='compromiso de consulta previa para subsidios')
    subsidios_individuales_monto = models.IntegerField(null = True, blank = True, verbose_name='Monto para subsidios individuales')
    subsidios_colectivos_monto = models.IntegerField(null = True, blank = True, verbose_name='Monto para subsidios colectivos')

    class Meta:
        verbose_name_plural = 'Vinculaciones de población'

class ImplementacionSeguimiento(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_iys")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    tipo = models.CharField(max_length=255, null=True, blank=True, choices=IMPACTOS)
    acciones_seguimiento_regional = models.TextField(null = True, blank = True, verbose_name='Descripción de Acciones de Seguimiento y control - Corporaciones Regionales')
    acciones_seguimiento_ministerio = models.TextField(null = True, blank = True, verbose_name='Descripción de Acciones de Seguimiento y control - Ministerio del Medio Ambiente')

    class Meta:
        verbose_name_plural = 'Implementaciones y Seguimientos'

class ReferenciaCartografica(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_referencias")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()
    referencia = models.FileField(upload_to='uploads/referencias_cartograficas', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Referencias cartograficas'


class ObraInfraestructura(Megaproyecto):
    tipo = models.CharField(max_length=255, choices=TIPOS_MEGAPROYECTOS_OBRAS_INFRAESTRUCTURA)
    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Infraestructura: Obras de infraestructura'

class ProyectoObraInfraestructura(Proyecto):
    nombre = models.CharField(max_length=255, null=True, blank=True)