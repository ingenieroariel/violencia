# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Sector'
        db.create_table('megaproyectos_sector', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['Sector'])

        # Adding model 'Afectacion'
        db.create_table('megaproyectos_afectacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_afectacion', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'], null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['Afectacion'])

        # Adding model 'DesarrolloLegislativo'
        db.create_table('megaproyectos_desarrollolegislativo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_documento', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('documento', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('nacional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.Sector'], null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('resumen_del_contenido', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['DesarrolloLegislativo'])

        # Adding M2M table for field departamento on 'DesarrolloLegislativo'
        db.create_table('megaproyectos_desarrollolegislativo_departamento', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('desarrollolegislativo', models.ForeignKey(orm['megaproyectos.desarrollolegislativo'], null=False)),
            ('departamento', models.ForeignKey(orm['territorios.departamento'], null=False))
        ))
        db.create_unique('megaproyectos_desarrollolegislativo_departamento', ['desarrollolegislativo_id', 'departamento_id'])

        # Adding model 'PoliticaMegaproyecto'
        db.create_table('megaproyectos_politicamegaproyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_documento', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('documento', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('nacional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('inicio_vigencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fin_vigencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.Sector'], null=True, blank=True)),
            ('resumen_del_contenido', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['PoliticaMegaproyecto'])

        # Adding M2M table for field departamento on 'PoliticaMegaproyecto'
        db.create_table('megaproyectos_politicamegaproyecto_departamento', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('politicamegaproyecto', models.ForeignKey(orm['megaproyectos.politicamegaproyecto'], null=False)),
            ('departamento', models.ForeignKey(orm['territorios.departamento'], null=False))
        ))
        db.create_unique('megaproyectos_politicamegaproyecto_departamento', ['politicamegaproyecto_id', 'departamento_id'])

        # Adding model 'InstitucionFinanciadora'
        db.create_table('megaproyectos_institucionfinanciadora', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cubrimiento', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['InstitucionFinanciadora'])

        # Adding model 'RequisitoLegal'
        db.create_table('megaproyectos_requisitolegal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('consulta_previa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('acta_acuerdo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('acta_acuerdo_fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('acta_acuerdo_suscriptor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('metodologia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('participacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cumplimientos_acuerdo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('conflictos_influencia_directa', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('conflictos_territorio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('conflictos_judicializacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('conflictos_correspondencia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('impacto_ambiental', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('impacto_cultural', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('impacto_socioeconomico', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('medidas_prevencion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('medidas_mitigacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('medidas_correccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('medidas_compensacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plan_de_manejo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['RequisitoLegal'])

        # Adding model 'VinculacionPoblacion'
        db.create_table('megaproyectos_vinculacionpoblacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_vinculaciones', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('empleo_compromiso_consulta_previa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('local', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('local_numero', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('local_tipo_actividades', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('local_forma_pago', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('otraregion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otraregion_numero', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('otraregion_tipo_actividades', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('otraregion_forma_pago', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('programas_compromiso_consulta_previa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('programa_educacion_monto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('programa_infraestructura_monto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('programa_salud_monto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('programa_produccion_monto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('programa_otros_monto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('programa_otros_cuales', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subsidios_consulta_previa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subsidios_individuales_monto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('subsidios_colectivos_monto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['VinculacionPoblacion'])

        # Adding model 'ImplementacionSeguimiento'
        db.create_table('megaproyectos_implementacionseguimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_iys', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acciones_seguimiento_regional', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acciones_seguimiento_ministerio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ImplementacionSeguimiento'])

        # Adding model 'ProyectoObraInfraestructura'
        db.create_table('megaproyectos_proyectoobrainfraestructura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoObraInfraestructura'])

        # Adding M2M table for field instituciones_financiadoras on 'ProyectoObraInfraestructura'
        db.create_table('megaproyectos_proyectoobrainfraestructura_instituciones_finb01d', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectoobrainfraestructura', models.ForeignKey(orm['megaproyectos.proyectoobrainfraestructura'], null=False)),
            ('institucionfinanciadora', models.ForeignKey(orm['megaproyectos.institucionfinanciadora'], null=False))
        ))
        db.create_unique('megaproyectos_proyectoobrainfraestructura_instituciones_finb01d', ['proyectoobrainfraestructura_id', 'institucionfinanciadora_id'])

        # Adding model 'EstadoEjecucionInfraestructura'
        db.create_table('megaproyectos_estadoejecucioninfraestructura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('subcontratista', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subcontratista_nombre_empresa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subcontratista_objeto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cesion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cesion_nuevo_titular', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('suspension', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('suspension_causa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('revocatoria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('revocatoria_causa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.ProyectoObraInfraestructura'])),
            ('contratacion_publica', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['EstadoEjecucionInfraestructura'])

        # Adding model 'ProyectoInsdustriaHidrocarburos'
        db.create_table('megaproyectos_proyectoinsdustriahidrocarburos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoInsdustriaHidrocarburos'])

        # Adding M2M table for field instituciones_financiadoras on 'ProyectoInsdustriaHidrocarburos'
        db.create_table('megaproyectos_proyectoinsdustriahidrocarburos_instituciones1141', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectoinsdustriahidrocarburos', models.ForeignKey(orm['megaproyectos.proyectoinsdustriahidrocarburos'], null=False)),
            ('institucionfinanciadora', models.ForeignKey(orm['megaproyectos.institucionfinanciadora'], null=False))
        ))
        db.create_unique('megaproyectos_proyectoinsdustriahidrocarburos_instituciones1141', ['proyectoinsdustriahidrocarburos_id', 'institucionfinanciadora_id'])

        # Adding model 'EstadoEjecucionHidrocarburos'
        db.create_table('megaproyectos_estadoejecucionhidrocarburos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('subcontratista', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subcontratista_nombre_empresa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subcontratista_objeto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cesion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cesion_nuevo_titular', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('suspension', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('suspension_causa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('revocatoria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('revocatoria_causa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.ProyectoInsdustriaHidrocarburos'])),
            ('concesion_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('concesion_contrato_ecopetrol', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('consesion_resolusion_registro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('exploracion_sismica', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('exploracion_sismica_sin_vias', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('exploracion_sismica_sin_vias_objeto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('exploracion_sismica_sin_vias_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('perforacion_exploratoria', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('exploracion_exploratoria_objeto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('exploracion_exploratoria_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('explotacion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('explotacion_cuales', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('explotacion_logitud', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('explotacion_ubicacion_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['EstadoEjecucionHidrocarburos'])

        # Adding model 'ProyectoMineria'
        db.create_table('megaproyectos_proyectomineria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mineral', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoMineria'])

        # Adding M2M table for field instituciones_financiadoras on 'ProyectoMineria'
        db.create_table('megaproyectos_proyectomineria_instituciones_financiadoras', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectomineria', models.ForeignKey(orm['megaproyectos.proyectomineria'], null=False)),
            ('institucionfinanciadora', models.ForeignKey(orm['megaproyectos.institucionfinanciadora'], null=False))
        ))
        db.create_unique('megaproyectos_proyectomineria_instituciones_financiadoras', ['proyectomineria_id', 'institucionfinanciadora_id'])

        # Adding model 'EstadoEjecucionMineria'
        db.create_table('megaproyectos_estadoejecucionmineria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('subcontratista', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subcontratista_nombre_empresa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('subcontratista_objeto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cesion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cesion_nuevo_titular', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('suspension', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('suspension_causa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('revocatoria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('revocatoria_causa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.ProyectoMineria'])),
            ('prospeccion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('concesion_minera', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['EstadoEjecucionMineria'])

        # Adding model 'TituloMinero'
        db.create_table('megaproyectos_titulominero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.ProyectoMineria'])),
            ('nombre_empresa', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('descripcion_contrato_asociacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resolucion_registro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['TituloMinero'])

        # Adding model 'Exploracion'
        db.create_table('megaproyectos_exploracion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.ProyectoMineria'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('objeto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('la', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('megaproyectos', ['Exploracion'])

        # Adding model 'AFPEspecie'
        db.create_table('megaproyectos_afpespecie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_afp_especies', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volumen', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('peso', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('diametro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['AFPEspecie'])

        # Adding model 'AFPObligacion'
        db.create_table('megaproyectos_afpobligacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_afp_oblig', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['AFPObligacion'])

        # Adding model 'AFPInformeSemestral'
        db.create_table('megaproyectos_afpinformesemestral', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_afp_informe', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('semestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('informe', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('megaproyectos', ['AFPInformeSemestral'])

        # Adding model 'AFPESalvoconducto'
        db.create_table('megaproyectos_afpesalvoconducto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_afp_salvoconducto', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_expedicion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_vencimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('especie', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volumen', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('descripcion_medio_transporte', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['AFPESalvoconducto'])

        # Adding model 'ProyectoAFP'
        db.create_table('megaproyectos_proyectoafp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tipo_permiso', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('numero_permiso', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('titulo_empresa_forestal_o_sociedad', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('vigencia_desde', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('vigencia_hasta', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('extension', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descripcion_derechos_y_tasas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sistema_de_aprovechamiento', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('monto_de_inversion', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('nombre_usuario', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tipo_usuario', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('aval_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('opera_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('opera_en_extrajero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otras_actividades_cuales', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoAFP'])

        # Adding M2M table for field instituciones_financiadoras on 'ProyectoAFP'
        db.create_table('megaproyectos_proyectoafp_instituciones_financiadoras', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectoafp', models.ForeignKey(orm['megaproyectos.proyectoafp'], null=False)),
            ('institucionfinanciadora', models.ForeignKey(orm['megaproyectos.institucionfinanciadora'], null=False))
        ))
        db.create_unique('megaproyectos_proyectoafp_instituciones_financiadoras', ['proyectoafp_id', 'institucionfinanciadora_id'])

        # Adding model 'ProyectoPescaContinental'
        db.create_table('megaproyectos_proyectopescacontinental', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('duracion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_de_operaciones', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cuota', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('especies', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sistema_tecnologico', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('causales', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valorizaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plan_investigacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vigencia', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resultado', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subtipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoPescaContinental'])

        # Adding model 'ProyectoPescaMarina'
        db.create_table('megaproyectos_proyectopescamarina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('duracion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_de_operaciones', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cuota', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('especies', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sistema_tecnologico', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('causales', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valorizaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plan_investigacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vigencia', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resultado', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subtipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoPescaMarina'])

        # Adding model 'ProyectoProcesamientoPesca'
        db.create_table('megaproyectos_proyectoprocesamientopesca', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('duracion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_de_operaciones', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cuota', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('especies', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sistema_tecnologico', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('causales', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valorizaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plan_investigacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vigencia', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resultado', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoProcesamientoPesca'])

        # Adding model 'ProyectoComercializacionPesca'
        db.create_table('megaproyectos_proyectocomercializacionpesca', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('duracion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_de_operaciones', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cuota', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('especies', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sistema_tecnologico', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('causales', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valorizaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plan_investigacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vigencia', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resultado', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoComercializacionPesca'])

        # Adding model 'ProyectoPescaIntegrada'
        db.create_table('megaproyectos_proyectopescaintegrada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('duracion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_de_operaciones', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cuota', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('especies', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sistema_tecnologico', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('causales', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valorizaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plan_investigacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vigencia', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resultado', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoPescaIntegrada'])

        # Adding model 'ProyectoAgroindustria'
        db.create_table('megaproyectos_proyectoagroindustria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_terrestre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_maritima', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fecha_iniciacion', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_empresa_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('financia_empresa_accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('financia_empresa_otras_actividades_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('financia_monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('monto_inversion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['ProyectoAgroindustria'])

        # Adding M2M table for field instituciones_financiadoras on 'ProyectoAgroindustria'
        db.create_table('megaproyectos_proyectoagroindustria_instituciones_financiadoras', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyectoagroindustria', models.ForeignKey(orm['megaproyectos.proyectoagroindustria'], null=False)),
            ('institucionfinanciadora', models.ForeignKey(orm['megaproyectos.institucionfinanciadora'], null=False))
        ))
        db.create_unique('megaproyectos_proyectoagroindustria_instituciones_financiadoras', ['proyectoagroindustria_id', 'institucionfinanciadora_id'])

        # Adding model 'EstadoEjecucionAgroindustria'
        db.create_table('megaproyectos_estadoejecucionagroindustria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megaproyectos.ProyectoAgroindustria'])),
            ('medida_preparacion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('medida_cultivo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('medida_produccion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('medida_trasnformacion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('medida_transformacion_resultado', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('medida_comercializacion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('medida_comercializacion_resultado', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['EstadoEjecucionAgroindustria'])

        # Adding model 'RequisitoLegalAgroindustria'
        db.create_table('megaproyectos_requisitolegalagroindustria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('consulta_previa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('acta_acuerdo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('acta_acuerdo_fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('acta_acuerdo_suscriptor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('metodologia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('participacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cumplimientos_acuerdo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('adecuacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adecuacion_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('concesion_aguas_superficiales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('concesion_aguas_superficiales_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('concesion_aguas_subterraneas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('concesion_aguas_subterraneas_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('permisos_vertimiento', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permisos_vertimiento_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('permisos_emisiones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('permisos_autorizaciones', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permisos_autorizaciones_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('megaproyectos', ['RequisitoLegalAgroindustria'])


    def backwards(self, orm):
        
        # Deleting model 'Sector'
        db.delete_table('megaproyectos_sector')

        # Deleting model 'Afectacion'
        db.delete_table('megaproyectos_afectacion')

        # Deleting model 'DesarrolloLegislativo'
        db.delete_table('megaproyectos_desarrollolegislativo')

        # Removing M2M table for field departamento on 'DesarrolloLegislativo'
        db.delete_table('megaproyectos_desarrollolegislativo_departamento')

        # Deleting model 'PoliticaMegaproyecto'
        db.delete_table('megaproyectos_politicamegaproyecto')

        # Removing M2M table for field departamento on 'PoliticaMegaproyecto'
        db.delete_table('megaproyectos_politicamegaproyecto_departamento')

        # Deleting model 'InstitucionFinanciadora'
        db.delete_table('megaproyectos_institucionfinanciadora')

        # Deleting model 'RequisitoLegal'
        db.delete_table('megaproyectos_requisitolegal')

        # Deleting model 'VinculacionPoblacion'
        db.delete_table('megaproyectos_vinculacionpoblacion')

        # Deleting model 'ImplementacionSeguimiento'
        db.delete_table('megaproyectos_implementacionseguimiento')

        # Deleting model 'ProyectoObraInfraestructura'
        db.delete_table('megaproyectos_proyectoobrainfraestructura')

        # Removing M2M table for field instituciones_financiadoras on 'ProyectoObraInfraestructura'
        db.delete_table('megaproyectos_proyectoobrainfraestructura_instituciones_finb01d')

        # Deleting model 'EstadoEjecucionInfraestructura'
        db.delete_table('megaproyectos_estadoejecucioninfraestructura')

        # Deleting model 'ProyectoInsdustriaHidrocarburos'
        db.delete_table('megaproyectos_proyectoinsdustriahidrocarburos')

        # Removing M2M table for field instituciones_financiadoras on 'ProyectoInsdustriaHidrocarburos'
        db.delete_table('megaproyectos_proyectoinsdustriahidrocarburos_instituciones1141')

        # Deleting model 'EstadoEjecucionHidrocarburos'
        db.delete_table('megaproyectos_estadoejecucionhidrocarburos')

        # Deleting model 'ProyectoMineria'
        db.delete_table('megaproyectos_proyectomineria')

        # Removing M2M table for field instituciones_financiadoras on 'ProyectoMineria'
        db.delete_table('megaproyectos_proyectomineria_instituciones_financiadoras')

        # Deleting model 'EstadoEjecucionMineria'
        db.delete_table('megaproyectos_estadoejecucionmineria')

        # Deleting model 'TituloMinero'
        db.delete_table('megaproyectos_titulominero')

        # Deleting model 'Exploracion'
        db.delete_table('megaproyectos_exploracion')

        # Deleting model 'AFPEspecie'
        db.delete_table('megaproyectos_afpespecie')

        # Deleting model 'AFPObligacion'
        db.delete_table('megaproyectos_afpobligacion')

        # Deleting model 'AFPInformeSemestral'
        db.delete_table('megaproyectos_afpinformesemestral')

        # Deleting model 'AFPESalvoconducto'
        db.delete_table('megaproyectos_afpesalvoconducto')

        # Deleting model 'ProyectoAFP'
        db.delete_table('megaproyectos_proyectoafp')

        # Removing M2M table for field instituciones_financiadoras on 'ProyectoAFP'
        db.delete_table('megaproyectos_proyectoafp_instituciones_financiadoras')

        # Deleting model 'ProyectoPescaContinental'
        db.delete_table('megaproyectos_proyectopescacontinental')

        # Deleting model 'ProyectoPescaMarina'
        db.delete_table('megaproyectos_proyectopescamarina')

        # Deleting model 'ProyectoProcesamientoPesca'
        db.delete_table('megaproyectos_proyectoprocesamientopesca')

        # Deleting model 'ProyectoComercializacionPesca'
        db.delete_table('megaproyectos_proyectocomercializacionpesca')

        # Deleting model 'ProyectoPescaIntegrada'
        db.delete_table('megaproyectos_proyectopescaintegrada')

        # Deleting model 'ProyectoAgroindustria'
        db.delete_table('megaproyectos_proyectoagroindustria')

        # Removing M2M table for field instituciones_financiadoras on 'ProyectoAgroindustria'
        db.delete_table('megaproyectos_proyectoagroindustria_instituciones_financiadoras')

        # Deleting model 'EstadoEjecucionAgroindustria'
        db.delete_table('megaproyectos_estadoejecucionagroindustria')

        # Deleting model 'RequisitoLegalAgroindustria'
        db.delete_table('megaproyectos_requisitolegalagroindustria')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fuentes.autordato': {
            'Meta': {'object_name': 'AutorDato'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'fuentes.fuentedato': {
            'Meta': {'object_name': 'FuenteDato'},
            'ano': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.AutorDato']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            'frecuencia_actualizacion': ('django.db.models.fields.CharField', [], {'default': "'anual'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nombre_documento': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'megaproyectos.afectacion': {
            'Meta': {'object_name': 'Afectacion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_afectacion'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'megaproyectos.afpesalvoconducto': {
            'Meta': {'object_name': 'AFPESalvoconducto'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_afp_salvoconducto'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'descripcion_medio_transporte': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'especie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fecha_expedicion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_vencimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volumen': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.afpespecie': {
            'Meta': {'object_name': 'AFPEspecie'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_afp_especies'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'diametro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'peso': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'volumen': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.afpinformesemestral': {
            'Meta': {'object_name': 'AFPInformeSemestral'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_afp_informe'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.TextField', [], {}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.afpobligacion': {
            'Meta': {'object_name': 'AFPObligacion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_afp_oblig'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.desarrollolegislativo': {
            'Meta': {'object_name': 'DesarrolloLegislativo'},
            'departamento': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['territorios.Departamento']", 'null': 'True', 'blank': 'True'}),
            'documento': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre_documento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resumen_del_contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.Sector']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.estadoejecucionagroindustria': {
            'Meta': {'object_name': 'EstadoEjecucionAgroindustria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medida_comercializacion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medida_comercializacion_resultado': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medida_cultivo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medida_preparacion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medida_produccion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medida_transformacion_resultado': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medida_trasnformacion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.ProyectoAgroindustria']"})
        },
        'megaproyectos.estadoejecucionhidrocarburos': {
            'Meta': {'object_name': 'EstadoEjecucionHidrocarburos'},
            'cesion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cesion_nuevo_titular': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'concesion_contrato_ecopetrol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concesion_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'consesion_resolusion_registro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'exploracion_exploratoria_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exploracion_exploratoria_objeto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exploracion_sismica': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'exploracion_sismica_sin_vias': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'exploracion_sismica_sin_vias_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exploracion_sismica_sin_vias_objeto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'explotacion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'explotacion_cuales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'explotacion_logitud': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'explotacion_ubicacion_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perforacion_exploratoria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.ProyectoInsdustriaHidrocarburos']"}),
            'revocatoria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'revocatoria_causa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subcontratista': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subcontratista_nombre_empresa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subcontratista_objeto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'suspension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suspension_causa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.estadoejecucioninfraestructura': {
            'Meta': {'object_name': 'EstadoEjecucionInfraestructura'},
            'cesion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cesion_nuevo_titular': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contratacion_publica': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.ProyectoObraInfraestructura']"}),
            'revocatoria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'revocatoria_causa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subcontratista': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subcontratista_nombre_empresa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subcontratista_objeto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'suspension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suspension_causa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.estadoejecucionmineria': {
            'Meta': {'object_name': 'EstadoEjecucionMineria'},
            'cesion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cesion_nuevo_titular': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'concesion_minera': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prospeccion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.ProyectoMineria']"}),
            'revocatoria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'revocatoria_causa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subcontratista': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subcontratista_nombre_empresa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'subcontratista_objeto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'suspension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suspension_causa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.exploracion': {
            'Meta': {'object_name': 'Exploracion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'la': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'objeto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.ProyectoMineria']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.implementacionseguimiento': {
            'Meta': {'object_name': 'ImplementacionSeguimiento'},
            'acciones_seguimiento_ministerio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'acciones_seguimiento_regional': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_iys'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.institucionfinanciadora': {
            'Meta': {'object_name': 'InstitucionFinanciadora'},
            'cubrimiento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.politicamegaproyecto': {
            'Meta': {'object_name': 'PoliticaMegaproyecto'},
            'departamento': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['territorios.Departamento']", 'null': 'True', 'blank': 'True'}),
            'documento': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fin_vigencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio_vigencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nacional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre_documento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resumen_del_contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.Sector']", 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.proyectoafp': {
            'Meta': {'object_name': 'ProyectoAFP'},
            'accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aval_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_derechos_y_tasas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones_financiadoras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['megaproyectos.InstitucionFinanciadora']", 'null': 'True', 'blank': 'True'}),
            'monto_de_inversion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre_usuario': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'numero_permiso': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'opera_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'opera_en_extrajero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'otras_actividades_cuales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sistema_de_aprovechamiento': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo_permiso': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo_usuario': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'titulo_empresa_forestal_o_sociedad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vigencia_desde': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'vigencia_hasta': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.proyectoagroindustria': {
            'Meta': {'object_name': 'ProyectoAgroindustria'},
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones_financiadoras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['megaproyectos.InstitucionFinanciadora']", 'null': 'True', 'blank': 'True'}),
            'monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'megaproyectos.proyectocomercializacionpesca': {
            'Meta': {'object_name': 'ProyectoComercializacionPesca'},
            'area_de_operaciones': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'causales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cuota': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'especies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plan_investigacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sistema_tecnologico': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'valorizaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vigencia': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.proyectoinsdustriahidrocarburos': {
            'Meta': {'object_name': 'ProyectoInsdustriaHidrocarburos'},
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones_financiadoras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['megaproyectos.InstitucionFinanciadora']", 'null': 'True', 'blank': 'True'}),
            'monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'megaproyectos.proyectomineria': {
            'Meta': {'object_name': 'ProyectoMineria'},
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones_financiadoras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['megaproyectos.InstitucionFinanciadora']", 'null': 'True', 'blank': 'True'}),
            'mineral': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'megaproyectos.proyectoobrainfraestructura': {
            'Meta': {'object_name': 'ProyectoObraInfraestructura'},
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones_financiadoras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['megaproyectos.InstitucionFinanciadora']", 'null': 'True', 'blank': 'True'}),
            'monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'megaproyectos.proyectopescacontinental': {
            'Meta': {'object_name': 'ProyectoPescaContinental'},
            'area_de_operaciones': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'causales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cuota': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'especies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan_investigacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sistema_tecnologico': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'subtipo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valorizaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vigencia': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.proyectopescaintegrada': {
            'Meta': {'object_name': 'ProyectoPescaIntegrada'},
            'area_de_operaciones': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'causales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cuota': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'especies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plan_investigacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sistema_tecnologico': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'valorizaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vigencia': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.proyectopescamarina': {
            'Meta': {'object_name': 'ProyectoPescaMarina'},
            'area_de_operaciones': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'causales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cuota': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'especies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan_investigacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sistema_tecnologico': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'subtipo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valorizaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vigencia': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.proyectoprocesamientopesca': {
            'Meta': {'object_name': 'ProyectoProcesamientoPesca'},
            'area_de_operaciones': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_maritima': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_terrestre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'causales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cuota': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'especies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_iniciacion': ('django.db.models.fields.DateField', [], {}),
            'financia_empresa_accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_otras_actividades': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financia_empresa_otras_actividades_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financia_empresa_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_empresa_sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financia_monto_inversion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plan_investigacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sistema_tecnologico': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'valorizaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'vigencia': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.requisitolegal': {
            'Meta': {'object_name': 'RequisitoLegal'},
            'acta_acuerdo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'acta_acuerdo_fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'acta_acuerdo_suscriptor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'conflictos_correspondencia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'conflictos_influencia_directa': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'conflictos_judicializacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'conflictos_territorio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'consulta_previa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'cumplimientos_acuerdo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacto_ambiental': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'impacto_cultural': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'impacto_socioeconomico': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'medidas_compensacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'medidas_correccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'medidas_mitigacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'medidas_prevencion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'participacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'plan_de_manejo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.requisitolegalagroindustria': {
            'Meta': {'object_name': 'RequisitoLegalAgroindustria'},
            'acta_acuerdo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'acta_acuerdo_fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'acta_acuerdo_suscriptor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adecuacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adecuacion_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'concesion_aguas_subterraneas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concesion_aguas_subterraneas_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'concesion_aguas_superficiales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concesion_aguas_superficiales_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'consulta_previa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'cumplimientos_acuerdo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'participacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'permisos_autorizaciones': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permisos_autorizaciones_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'permisos_emisiones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'permisos_vertimiento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permisos_vertimiento_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.sector': {
            'Meta': {'object_name': 'Sector'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.titulominero': {
            'Meta': {'object_name': 'TituloMinero'},
            'descripcion_contrato_asociacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_empresa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['megaproyectos.ProyectoMineria']"}),
            'resolucion_registro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'megaproyectos.vinculacionpoblacion': {
            'Meta': {'object_name': 'VinculacionPoblacion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_vinculaciones'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'empleo_compromiso_consulta_previa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'local_forma_pago': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'local_numero': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'local_tipo_actividades': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'otraregion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'otraregion_forma_pago': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'otraregion_numero': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'otraregion_tipo_actividades': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'programa_educacion_monto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'programa_infraestructura_monto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'programa_otros_cuales': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'programa_otros_monto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'programa_produccion_monto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'programa_salud_monto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'programas_compromiso_consulta_previa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subsidios_colectivos_monto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subsidios_consulta_previa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subsidios_individuales_monto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'ano_creacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_rural': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_urbana': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad_municipios_pacifico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad_municipios_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fuente_poblacion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_poblacion_dpto'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_presupuesto': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_presupuesto_dpto'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'gastos': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion_adicional': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ingresos': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'presupuesto_anual': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'territorios.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'ano_creacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_cabecera': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_rural': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'certificado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'fuente_presupuesto': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_presupuesto_mpio'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'gastos': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion_adicional': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ingresos': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'presupuesto_anual': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'titulos_cabecera': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'titulos_rural': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'territorios.territoriocomunidad': {
            'Meta': {'object_name': 'TerritorioComunidad'},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion_adicional': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'limites': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'municipios': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['territorios.Municipio']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resolucion_constitucion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'titulado': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['megaproyectos']
