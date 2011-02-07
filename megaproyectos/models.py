# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from fuentes.models import FuenteDato
from territorios.models import TerritorioComunidad, Departamento, Municipio, Ubicacion
from django.db import models



CATEGORIA_SECTOR= (
    ('oi','Obras de Infraestructura'),
    ('ee','Economía Extractiva '),
    ('et','Economía de Transformación / '),
)
class Sector(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True, choices= CATEGORIA_SECTOR)

    def __unicode__(self):
        return self.get_categoria_display() + " / " + self.nombre

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

TIPO_EXPLORACION_SISMICA = (
    ("con-vias","con vías (LA-MAVDT)"),
    ("sin-vias","sin vías"),
    ("areas-marítimas","areas marítimas (LA-MAVDT) "),
)

TIPO_PCA = (
    ("permiso","Permiso"),
    ("concesion","Concesión"),
    ("autorizacion","Autorización")
)

TIPO_EXPLOTACION = (
    ("con-obras-complementarias","con obras complementarias (LA-MAVDT)"),
    ("transporte-liquidos","transporte y conducción liquidos (LA-MAVDT)"),
    ("transporte-gaseoso","transporte y conducción gaseosos (LA-MAVDT)"),
    ("transporte-ambos","transporte y conducción liquido y gaseosos (LA-MAVDT)"),
    ("terminales-entrega","terminales de entrega y estaciones de transferencias (LA-MAVDT)"),
    ("contruccion-operacion-refinerias","Construcción y operación de refinerías (LA-MAVDT)"),
)

TIPOS_DE_PERFORACION_EXPLORATORIA = (
    ("dentro","Dentro de campos de producción de hidrocarburos"),
    ("fuera","Afuera de campos de producción de hidrocarburos (LA-MAVDT)"),
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

TIPOS_MINERIA = (
    ("carbon-mayor-800mil-tonxano","Carbon / Mayor de 800.000 ton/año (LA- MAVDT)"),
    ("carbon-menor-800mil-tonxano","Carbon / Menor de 800.000 ton/año (LA-CAR)"),
    ("construccion-mayor-600tonxano","Materiales de Construcción / igual o mayor a 600.000 ton/año (LA- MAVDT)"),
    ("construccion-menor-600tonxano","Materiales de Construcción / menor de 600.000 ton/año (LA -CAR) "),
    ("metales-material-removido-2millones-tonxano","Metales y Piedras preciosas / Material removido igual o mayor a 2.000.000 ton/año (LA MAVDT)"),
    ("metales-material-removido-menor-2millones-tonxano","Metales y Piedras preciosas / Material removido menor de 2.000.000 ton/año (LA-CAR)"),
    ("otros-1millon-tonxano","Otros minerales / Igual o mayor a 1.000.000 ton/año (LA MAVDT)"),
    ("otros-1millon-menor-tonxano","Otros minerales / Menor de 1.000.000 ton/año (LA-CAR)")
)

TIPOS_CONCESION_MINERAS = (
    ("","Titulo minero"),
    ("","Titulo minero"),
)

TIPO_MEGAPROYECTOS_INDUSTRIA_HIDROCARBUROS = (
    ("petroleo","Petroleo"),
    ("petroleo-gas","Petroleo y Gas"),
)

TIPO_EXTRACCION_PUBLICA = (
    ("concesion","Concesión"),
    ("permiso","Permiso"),
    ("asociacion","Asociación"),
)
TIPO_EXTRACCION_PRIVADA = (
    ("autorizacion","Autorización"),
)

TIPOS_AGROINDUSTRIA = (
    ("agro-palma","Agrocombustibles / Palma"),
    ("agro-cana","Agrocombustibles / Caña"),
    ("agro-otros","Agrocombustibles / Otros"),
    ("agro-platano","Alimentaria / Plátano"),
    ("ali-otros","Alimentaria / Otros"),
    ("ali-arracacho","Otros usos / Arracacho"),
    ("ali-otros","Otros usos / Otros")
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

TIPO_LEGISLATIVO = (
    ('ley', 'Ley'),
    ('decreto', 'Decreto'),
    ('resolucion', 'Resolucion'),
    ('ordenanza', 'Ordenanza'),
    ('jurisprudencia', 'Jurisprudencia'),
)

class DesarrolloLegislativo(models.Model):
    nombre_documento = models.CharField(max_length=255, blank=True, null=True)
    documento = models.FileField(upload_to='uploads/documentos_desarrollo_legislativos', blank=True, null=True)
    departamento = models.ManyToManyField(Departamento, null=True, blank=True)
    nacional = models.BooleanField(help_text="Aplica para todo el territorio nacional?", default=False)
    fecha = models.DateField(null=True, blank=True)
    sector = models.ForeignKey(Sector, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True, choices=TIPO_LEGISLATIVO)
    resumen_del_contenido = models.TextField(blank=True, null=True)
 
    class Meta:
        verbose_name = 'Documento de Desarrollo Legislativo'
        verbose_name_plural = 'Documentos de Desarrollo Legislativo'

class PoliticaMegaproyecto(models.Model):
    nombre_documento = models.CharField(max_length=255, blank=True, null=True)
    documento = models.FileField(upload_to='uploads/documentos_megaproyectos', blank=True, null=True)
    departamento = models.ManyToManyField(Departamento, null=True, blank=True)
    nacional = models.BooleanField(help_text="Aplica para todo el territorio nacional?", default=False)
    inicio_vigencia = models.IntegerField(help_text="Anio", blank=True, null=True)
    fin_vigencia = models.IntegerField(help_text="Anio", blank=True, null=True)
    sector = models.ForeignKey(Sector, blank=True, null=True)
    resumen_del_contenido = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name="Documento de Politicas Publicas"
        verbose_name_plural="Documentos de Politicas Publicas"

class InstitucionFinanciadora(models.Model):
    cubrimiento = models.CharField(max_length=255, null=True, blank=True, choices=CUBRIMIENTO_INSTITUCIONES_FINANCIADORAS)
    tipo = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_INSTITUCIONES_FINANCIADORAS)
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Instituciones Financiadoras'

    def __unicode__(self):
        return self.nombre

class ProyectoBase(models.Model):
    """ Información general """
    municipios = models.ManyToManyField(Municipio)
    territorios = models.ManyToManyField(TerritorioComunidad, null=True, blank=True)
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
    
    class Meta:
        abstract = True

class Proyecto(ProyectoBase):
    
    monto_inversion = models.IntegerField(null=True, blank=True, help_text='Monto de inversión')
    instituciones_financiadoras = models.ManyToManyField(InstitucionFinanciadora, null = True, blank = True)

    class Meta:
        abstract = True


class EstadoEjecucion(models.Model):
    
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
        abstract = True

class RequisitoLegalBase(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
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

    class Meta:
        abstract = True

class RequisitoLegal(RequisitoLegalBase):
    
    """ CONFLICTOS """
    conflictos_influencia_directa = models.TextField(null = True, blank = True, verbose_name='Descripción de conclictos area de influencia directa', help_text='conflictos')
    conflictos_territorio = models.TextField(null = True, blank = True, verbose_name='Descripción de conflictos de territorio', help_text='conflictos')
    conflictos_judicializacion = models.TextField(null = True, blank = True, verbose_name='Descripción de conflictos de judicialización', help_text='conflictos')
    conflictos_correspondencia = models.TextField(null = True, blank = True, verbose_name='Descripción de conflictos de Correspondencia de los impactos y los acuerdos', help_text='conflictos')
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

class Ubicacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_ubicacion")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()


""" OBRAS DE INFRAESTRUCTURA """

class ProyectoObraInfraestructura(Proyecto):
    tipo = models.CharField(max_length=255, choices=TIPOS_MEGAPROYECTOS_OBRAS_INFRAESTRUCTURA)
    nombre = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.nombre, self.megaproyecto.nombre_documento)

    class Meta:
        verbose_name_plural = 'Proyectos de Obras de Infraestructura'

class EstadoEjecucionInfraestructura(EstadoEjecucion):
    proyecto = models.ForeignKey(ProyectoObraInfraestructura)
    """Contratación pública"""
    contratacion_publica = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_CONTRATACIONES_PUBLICAS)


""" INDUSTRIAS DE HIDROCARBURO """

class ProyectoInsdustriaHidrocarburos(Proyecto):
    tipo = models.CharField(max_length=255, choices=TIPO_MEGAPROYECTOS_INDUSTRIA_HIDROCARBUROS)
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Proyectos de Industria de Hidrocarburos'

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.nombre, self.megaproyecto.nombre_documento)

class EstadoEjecucionHidrocarburos(EstadoEjecucion):
    proyecto = models.ForeignKey(ProyectoInsdustriaHidrocarburos)
    concesion_empresa_nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre de empresa que hace ka Concesión')
    concesion_contrato_ecopetrol = models.BooleanField(verbose_name='Tiene contrato de asociaciñon con Ecopetrol?')
    consesion_resolusion_registro = models.CharField(max_length=255, null=True, blank=True, verbose_name='Resolución o Registro Nº')
    exploracion_sismica = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_EXPLORACION_SISMICA)
    exploracion_sismica_sin_vias = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_PCA, help_text='en caso de haber seleccionado SIN VIAS')
    exploracion_sismica_sin_vias_objeto = models.TextField(null = True, blank = True, verbose_name='Objeto', help_text='en caso de haber seleccionado SIN VIAS')
    exploracion_sismica_sin_vias_desc = models.TextField(null = True, blank = True, verbose_name='Descripción', help_text='en caso de haber seleccionado SIN VIAS')
    perforacion_exploratoria = models.CharField(max_length=255, null=True, blank=True, choices=TIPOS_DE_PERFORACION_EXPLORATORIA)
    exploracion_exploratoria_objeto = models.TextField(null = True, blank = True, verbose_name='Objeto', help_text='en caso de haber seleccionado Dentro de campos de producción de hidrocarburos')
    exploracion_exploratoria_desc = models.TextField(null = True, blank = True, verbose_name='Descripción', help_text='en caso de haber seleccionado Dentro de campos de producción de hidrocarburos')
    explotacion = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_EXPLOTACION)
    explotacion_cuales = models.TextField(null = True, blank = True, verbose_name='cuales', help_text='En caso de haber escojido Con obras complementarias')
    explotacion_logitud = models.CharField(max_length=255, null=True, blank=True, verbose_name='longitud', help_text='en caso de haber escogido Transporte y conduccion de liquidos')
    explotacion_ubicacion_descripcion = models.TextField(null = True, blank = True, verbose_name='Ubicación', help_text='Descripción')

""" MINERIA """
class ProyectoMineria(Proyecto):
    tipo = models.CharField(max_length=255, choices=TIPOS_MINERIA)
    mineral = models.CharField(max_length=255, null=True, blank=True, help_text='En caso de haber seleccionado: otros minerales')
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Proyectos de Minerias'

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.nombre, self.megaproyecto.nombre_documento)

class EstadoEjecucionMineria(EstadoEjecucion):
    proyecto = models.ForeignKey(ProyectoMineria)
    prospeccion = models.CharField(max_length=255, null = True, blank = True, choices=(("libre","libre"),("excepto","excepto zona minera de grupos étnicos")), verbose_name='Prospección')
    concesion_minera = models.CharField(max_length=255, null=True, blank=True, verbose_name='Concesión minera')

class TituloMinero(models.Model):
    proyecto = models.ForeignKey(ProyectoMineria)
    nombre_empresa = models.CharField(max_length=255, null=True, blank=True)
    descripcion_contrato_asociacion = models.TextField(null = True, blank = True)
    resolucion_registro = models.CharField(max_length=255, null=True, blank=True, verbose_name='Resolución o Registro Nº')

    class Meta:
        verbose_name_plural = 'Titulos mineros'

class Exploracion(models.Model):
    proyecto = models.ForeignKey(ProyectoMineria)
    tipo = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_PCA, help_text='de recursos naturales')
    objeto = models.TextField(null = True, blank = True)
    descripcion = models.TextField(null = True, blank = True)
    la = models.BooleanField(verbose_name='LA si se construyen vías que la requieren (LA)')

    class Meta:
        verbose_name_plural = 'Exploraciones'

""" APROVECHAMIENTO FORESTAL PRESISTENTE """

class AFPEspecie(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_afp_especies")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    volumen = models.CharField(max_length=255, null=True, blank=True)
    peso = models.CharField(max_length=255, null=True, blank=True)
    diametro = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

class AFPObligacion(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_afp_oblig")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    tipo = models.CharField(max_length=255, null=True, blank=True, choices = (('mitigacion','Medidas de Mitigación'),('compensacion','Medidas de Compensación'),('restauracion','Medidas de Restauración')) )
    descripcion = models.TextField(null = True, blank = True)

    class Meta:
        verbose_name = 'Obligacion'
        verbose_name_plural = 'Obligaciones'

class AFPInformeSemestral(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_afp_informe")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    informe = models.TextField()

    class Meta:
        verbose_name = 'Informe semestral'
        verbose_name_plural = 'Informes semestrales'

class AFPESalvoconducto(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type_afp_salvoconducto")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey()

    movilizacion_origen = models.CharField(max_length=255, null=True, blank=True)
    movilizacion_destino = models.CharField(max_length=255, null=True, blank=True)
    renovacion = models.DateField(null = True, blank = True)
    removilizacion_autorizacion = models.BooleanField(verbose_name='tiene autorización de otra(s) CAR(s)?')
    cuales = models.TextField(null = True, blank = True, help_text='solo si selecciono la casilla anterior')
    fecha_expedicion = models.DateField(null = True, blank = True)
    fecha_vencimiento = models.DateField(null = True, blank = True)
    especie = models.CharField(max_length=255, null=True, blank=True)
    volumen = models.IntegerField(help_text='metros cubicos (m2)', null = True, blank = True)
    descripcion_medio_transporte = models.TextField(null = True, blank = True)

    class Meta:
        verbose_name = 'Salvoconducto'
        verbose_name_plural = 'Salvoconductos'

PERMISOS_AFP=(
    ('autorizacion', 'Autorizacion (en tipo propiedad privada)'),
    ('concesion', 'Concesion (en tipo dominio publico)'),
    ('permiso', 'Permiso (en tipo dominio publico)'),
    ('asociacion', 'Asociacion (en tipo dominio publico)'),
)

TIPO_AFP=(
    ('privado', 'Extraccion forestal en propiedad privada individual o colectiva'),
    ('publico', 'Extraccion forestal en dominio publico'),
)
USUARIOS_AFP=(
   ('cabildo', 'Cabildo'),
   ('consejo', 'Consejo comunitario'),
   ('empresa', 'Empresa Forestal'),
   ('sociedad', 'Sociedad (solamente para tipo dominio publico)'),
)
class ProyectoAFP(models.Model):
    tipo = models.CharField(max_length=255, choices=TIPO_AFP, blank=True, null=True)
    tipo_permiso = models.CharField(max_length=255, choices=PERMISOS_AFP, blank=True, null=True)
    numero_permiso = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(help_text='fecha en que se dio autorizacion', null = True, blank = True)
    vigencia_desde = models.DateField(null = True, blank = True)
    vigencia_hasta = models.DateField(null = True, blank = True)
    extension = models.FloatField(help_text="en hectareas",null=True, blank=True)
    descripcion_derechos_y_tasas = models.TextField(null = True, blank = True)
    sistema_de_aprovechamiento = models.CharField(max_length=255, null=True, blank=True, help_text='tecnologia')

    # sistema de financiamiento
    monto_de_inversion = models.FloatField(help_text="en millones de pesos", null=True, blank=True)
    instituciones_financiadoras = models.ManyToManyField(InstitucionFinanciadora, null = True, blank = True)

    # usuario
    nombre_usuario = models.CharField(max_length=255, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=255, choices=USUARIOS_AFP, null=True, blank=True)

    aval_descripcion = models.TextField(verbose_name='Aval del Cabildo o Junta', help_text="Solo para usuarios tipo cabildo o consejo comunitarios", null = True, blank = True)

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.nombre, self.megaproyecto.nombre_documento)

    class Meta:
        verbose_name = 'Proyecto de Aprovechamiento forestal per.'
        verbose_name_plural = 'Proyectos de Aprovechamiento forestal per.'


 
class Nada():
    empresa_forestal = models.CharField(help_text='representante legal', max_length=255, null=True, blank=True)
    ef_accionistas_nacionales = models.BooleanField(verbose_name='Tiene accionistas nacionales?')
    ef_accionistas_extranjeros = models.BooleanField(verbose_name='Tiene accionistas extranjeros?')
    ef_opera_en_colombia = models.BooleanField()
    ef_opera_en_extrajero = models.BooleanField()
    ef_otras_actividades = models.BooleanField(verbose_name='La empresa forestal tiene otras actividades?')
    ef_otras_actividades_cuales = models.TextField(verbose_name='Cuales', help_text='solo en caso de haber seleccionado que tiene otras actividades', null = True, blank = True)

    sociedad = models.CharField(help_text='representante legal', max_length=255, null=True, blank=True)
    soc_sede_principal = models.CharField(max_length=255, null=True, blank=True)
    soc_accionistas_nacionales = models.BooleanField(verbose_name='Tiene accionistas nacionales?')
    soc_accionistas_extranjeros = models.BooleanField(verbose_name='Tiene accionistas extranjeros?')
    soc_opera_en_colombia = models.BooleanField()
    soc_opera_en_extrajero = models.BooleanField()
    soc_otras_actividades = models.BooleanField(verbose_name='La empresa forestal tiene otras actividades?')
    soc_otras_actividades_cuales = models.TextField(verbose_name='Cuales', help_text='solo en caso de haber seleccionado que tiene otras actividades', null = True, blank = True)


""" EXTRACCION PESQUERA """

class ProyectoPesquero(ProyectoBase):
    duracion = models.CharField(max_length=255, null=True, blank=True)
    area_de_operaciones = models.CharField(max_length=255, null=True, blank=True)
    cuota = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cuota o volumen de pesca para el correspondiente período')
    especies = models.TextField(null = True, blank = True)
    sistema_tecnologico = models.TextField(null = True, blank = True)
    causales = models.TextField(null = True, blank = True, verbose_name='Causales de revocación y las sanciones por incumplimiento')
    valorizaciones = models.TextField(null = True, blank = True, verbose_name='Valor de las tasas y derechos y la forma de pago, para cada período')

    plan_investigacion = models.TextField(null = True, blank = True, help_text='descripcion', verbose_name='Plan de investigacion')
    vigencia = models.DateField(null = True, blank = True)
    resultado = models.TextField(null = True, blank = True, help_text='descripcion')

    class Meta:
        abstract = True

class ProyectoPescaContinental(ProyectoPesquero):
    tipo = models.CharField(max_length=255, choices=( ("fluvial","Fluvial"),("lacustre","Lacustre") ))
    subtipo = models.CharField(max_length=255, choices=( ("artesanal","Comercial / Artesanal"),("industrial","Comercial / Industrial"), ("cientifica", "Cientifica") ))

    class Meta:
        verbose_name = 'Proyecto de pesca continental'
        verbose_name_plural = 'Proyectos de pesca continental'

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.tipo, self.megaproyecto.nombre_documento)


class ProyectoPescaMarina(ProyectoPesquero):
    tipo = models.CharField(max_length=255, choices=( ("costera","Costera"),("de-bajura","De bajura"),("de-altura","De altura") ))
    subtipo = models.CharField(max_length=255, choices=( ("artesanal","Comercial / Artesanal"),("industrial","Comercial / Industrial"), ("cientifica", "Cientifica") ))

    class Meta:
        verbose_name = 'Proyecto de pesca marina'
        verbose_name_plural = 'Proyectos de pesca marina'

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.tipo, self.megaproyecto.nombre_documento)

class ProyectoProcesamientoPesca(ProyectoPesquero):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto de procesamiento de pesca'
        verbose_name_plural = 'Proyectos de procesamiento de pesca'

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.nombre, self.megaproyecto.nombre_documento)

class ProyectoComercializacionPesca(ProyectoPesquero):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto de comercializacion de pesca'
        verbose_name_plural = 'Proyectos de comercializacion de pesca'

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.nombre, self.megaproyecto.nombre_documento)

class ProyectoPescaIntegrada(ProyectoPesquero):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto de pesca integrada'
        verbose_name_plural = 'Proyectos de pesca integrada'

    def __unicode__(self):
        return "%s (Megaproyecto: %s)" % (self.nombre, self.megaproyecto.nombre_documento)


""" AGROINDUSTRIA """

class ProyectoAgroindustria(Proyecto):
    tipo = models.CharField(max_length=255, choices=TIPOS_AGROINDUSTRIA)
    nombre = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.tipo, self.nombre)

    class Meta:
        verbose_name_plural = 'Proyectos de Agroindustrias'

class EstadoEjecucionAgroindustria(models.Model):
    proyecto = models.ForeignKey(ProyectoAgroindustria)
    medida_preparacion = models.CharField(max_length=255, null=True, blank=True)
    medida_cultivo = models.CharField(max_length=255, null=True, blank=True)
    medida_produccion = models.CharField(max_length=255, null=True, blank=True, verbose_name='medida Producción')
    medida_trasnformacion = models.CharField(max_length=255, null=True, blank=True, verbose_name='medida Transformación')
    medida_transformacion_resultado = models.CharField(max_length=255, null=True, blank=True, verbose_name='resultado de medida de transformación')
    medida_comercializacion = models.CharField(max_length=255, null=True, blank=True, verbose_name='medida Comercialización')
    medida_comercializacion_resultado = models.CharField(max_length=255, null=True, blank=True, verbose_name='resultado de medida de Comercialización')

    class Meta:
        verbose_name_plural = 'Estados de ejecucion de agroindustria'

class RequisitoLegalAgroindustria(RequisitoLegalBase):
    adecuacion = models.BooleanField(verbose_name='Adecuación del proyecto al Plan de Manejo de humedales, manglares y páramos (de las CARs)')
    adecuacion_descripcion = models.TextField(null = True, blank = True, verbose_name='Descrición de adecuación')
    concesion_aguas_superficiales = models.BooleanField(verbose_name='Concesión de aguas superficiales')
    concesion_aguas_superficiales_descripcion = models.TextField(null = True, blank = True, verbose_name='Descrición de Concesión de aguas superficiales')
    concesion_aguas_subterraneas = models.BooleanField(verbose_name='Concesión de aguas subterráneas')
    concesion_aguas_subterraneas_descripcion = models.TextField(null = True, blank = True, verbose_name='Descrición de Concesión de aguas subterráneas')
    permisos_vertimiento = models.BooleanField(verbose_name='Permisos de vertimientos y disposición de residuos sólidos')
    permisos_vertimiento_descripcion = models.TextField(null = True, blank = True, verbose_name='Descrición de Permisos de vertimientos y disposición de residuos sólidos')
    permisos_emisiones = models.BooleanField(verbose_name='Permisos de emisiones atmosféricas')
    permisos_emisiones = models.TextField(null = True, blank = True, verbose_name='Descrición de Permisos de emisiones atmosféricas')
    permisos_autorizaciones = models.BooleanField(verbose_name='Permisos o autorizaciones de aprovechamientos forestales')
    permisos_autorizaciones_descripcion = models.TextField(null = True, blank = True, verbose_name='Descrición de Permisos o autorizaciones de aprovechamientos forestales')

    class Meta:
        verbose_name_plural = 'Requicitos legales de Agroindustrias'

