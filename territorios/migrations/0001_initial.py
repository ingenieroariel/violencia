# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EstadisticaDepartamento'
        db.create_table('territorios_estadisticadepartamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hombres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('mujeres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_0_a_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_5_a_9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_10_a_14', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_15_a_19', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_20_a_24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_25_a_29', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_30_a_34', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_35_a_39', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_40_a_44', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_45_a_49', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_50_a_54', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_55_a_59', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_60_a_64', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_65_a_69', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_70_a_74', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_75_a_79', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_80_a_84', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_85_a_89', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_90_o_mas', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_indigena', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_afro', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_otros', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_no_informa', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('individual', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('masivo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cabecera', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rural', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
        ))
        db.send_create_signal('territorios', ['EstadisticaDepartamento'])

        # Adding model 'EstadisticaMunicipio'
        db.create_table('territorios_estadisticamunicipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hombres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('mujeres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_0_a_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_5_a_9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_10_a_14', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_15_a_19', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_20_a_24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_25_a_29', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_30_a_34', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_35_a_39', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_40_a_44', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_45_a_49', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_50_a_54', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_55_a_59', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_60_a_64', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_65_a_69', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_70_a_74', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_75_a_79', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_80_a_84', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_85_a_89', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_90_o_mas', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_indigena', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_afro', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_otros', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('etnia_no_informa', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('individual', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('masivo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cabecera', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rural', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Municipio'])),
        ))
        db.send_create_signal('territorios', ['EstadisticaMunicipio'])

        # Adding model 'Departamento'
        db.create_table('territorios_departamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True)),
            ('informacion_adicional', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ano_creacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('presupuesto_anual', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ingresos', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gastos', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_urbana', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_rural', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('capital', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cantidad_municipios_total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cantidad_municipios_pacifico', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fuente_presupuesto', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fuente_presupuesto_dpto', null=True, to=orm['fuentes.FuenteDato'])),
            ('fuente_poblacion', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fuente_poblacion_dpto', null=True, to=orm['fuentes.FuenteDato'])),
        ))
        db.send_create_signal('territorios', ['Departamento'])

        # Adding model 'Municipio'
        db.create_table('territorios_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True)),
            ('informacion_adicional', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ano_creacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('presupuesto_anual', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ingresos', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gastos', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
            ('certificado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('area_total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_cabecera', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('titulos_cabecera', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('area_rural', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('titulos_rural', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('fuente_presupuesto', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fuente_presupuesto_mpio', null=True, to=orm['fuentes.FuenteDato'])),
        ))
        db.send_create_signal('territorios', ['Municipio'])

        # Adding model 'TitulosIndividuales'
        db.create_table('territorios_titulosindividuales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='titulos_individuales', to=orm['territorios.Municipio'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('area_total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('grupo_poblacional', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fuente_titulos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['TitulosIndividuales'])

        # Adding model 'Pueblo'
        db.create_table('territorios_pueblo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['Pueblo'])

        # Adding model 'TerritorioComunidad'
        db.create_table('territorios_territoriocomunidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True)),
            ('informacion_adicional', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('limites', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('titulado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('resolucion_constitucion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['TerritorioComunidad'])

        # Adding M2M table for field municipios on 'TerritorioComunidad'
        db.create_table('territorios_territoriocomunidad_municipios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territoriocomunidad', models.ForeignKey(orm['territorios.territoriocomunidad'], null=False)),
            ('municipio', models.ForeignKey(orm['territorios.municipio'], null=False))
        ))
        db.create_unique('territorios_territoriocomunidad_municipios', ['territoriocomunidad_id', 'municipio_id'])

        # Adding model 'TerritorioComunidadIndigena'
        db.create_table('territorios_territoriocomunidadindigena', (
            ('territoriocomunidad_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['territorios.TerritorioComunidad'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('territorios', ['TerritorioComunidadIndigena'])

        # Adding model 'TerritorioComunidadNegra'
        db.create_table('territorios_territoriocomunidadnegra', (
            ('territoriocomunidad_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['territorios.TerritorioComunidad'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('territorios', ['TerritorioComunidadNegra'])

        # Adding model 'ComunidadNegra'
        db.create_table('territorios_comunidadnegra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_creacion_ano', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('fecha_disolucion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_disolucion_ano', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidadNegra'])),
        ))
        db.send_create_signal('territorios', ['ComunidadNegra'])

        # Adding model 'ComunidadIndigena'
        db.create_table('territorios_comunidadindigena', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_creacion_ano', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('fecha_disolucion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_disolucion_ano', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidadIndigena'])),
            ('pueblo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Pueblo'])),
        ))
        db.send_create_signal('territorios', ['ComunidadIndigena'])

        # Adding model 'Ampliacion'
        db.create_table('territorios_ampliacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
            ('estado_tramite', self.gf('django.db.models.fields.CharField')(default='S', max_length=2)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resolucion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('limites', self.gf('django.db.models.fields.TextField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['Ampliacion'])

        # Adding model 'Saneamiento'
        db.create_table('territorios_saneamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
            ('estado_tramite', self.gf('django.db.models.fields.CharField')(default='S', max_length=2)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resolucion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('limites', self.gf('django.db.models.fields.TextField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
            ('poblacion_total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('poblacion_afro', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('poblacion_otros', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['Saneamiento'])

        # Adding model 'SolicitudTitulacion'
        db.create_table('territorios_solicitudtitulacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
            ('estado_tramite', self.gf('django.db.models.fields.CharField')(default='S', max_length=2)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('resolucion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('limites', self.gf('django.db.models.fields.TextField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['SolicitudTitulacion'])

        # Adding model 'PoblacionTerritorioColectivo'
        db.create_table('territorios_poblacionterritoriocolectivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('familias', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hombres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('mujeres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_0_a_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_5_a_9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_10_a_14', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_15_a_19', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_20_a_24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_25_a_29', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_30_a_34', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_35_a_39', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_40_a_44', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_45_a_49', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_50_a_54', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_55_a_59', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_60_a_64', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_65_a_69', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_70_a_74', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_75_a_79', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_80_a_84', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_85_a_89', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_90_o_mas', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'])),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estadistica_comunidad', to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('territorios', ['PoblacionTerritorioColectivo'])

        # Adding model 'PoblacionComunidadNegra'
        db.create_table('territorios_poblacioncomunidadnegra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('familias', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hombres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('mujeres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_0_a_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_5_a_9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_10_a_14', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_15_a_19', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_20_a_24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_25_a_29', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_30_a_34', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_35_a_39', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_40_a_44', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_45_a_49', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_50_a_54', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_55_a_59', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_60_a_64', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_65_a_69', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_70_a_74', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_75_a_79', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_80_a_84', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_85_a_89', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_90_o_mas', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'])),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estadistica_asentamiento', to=orm['territorios.ComunidadNegra'])),
        ))
        db.send_create_signal('territorios', ['PoblacionComunidadNegra'])

        # Adding model 'PoblacionComunidadIndigena'
        db.create_table('territorios_poblacioncomunidadindigena', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('familias', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hombres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('mujeres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_0_a_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_5_a_9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_10_a_14', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_15_a_19', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_20_a_24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_25_a_29', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_30_a_34', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_35_a_39', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_40_a_44', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_45_a_49', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_50_a_54', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_55_a_59', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_60_a_64', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_65_a_69', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_70_a_74', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_75_a_79', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_80_a_84', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_85_a_89', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('edad_90_o_mas', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'])),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estadistica_asentamiento', to=orm['territorios.ComunidadIndigena'])),
        ))
        db.send_create_signal('territorios', ['PoblacionComunidadIndigena'])

        # Adding model 'Ubicacion'
        db.create_table('territorios_ubicacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='content_type_ubicacio', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('content_type_ubicacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('seleccionador', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['Ubicacion'])


    def backwards(self, orm):
        
        # Deleting model 'EstadisticaDepartamento'
        db.delete_table('territorios_estadisticadepartamento')

        # Deleting model 'EstadisticaMunicipio'
        db.delete_table('territorios_estadisticamunicipio')

        # Deleting model 'Departamento'
        db.delete_table('territorios_departamento')

        # Deleting model 'Municipio'
        db.delete_table('territorios_municipio')

        # Deleting model 'TitulosIndividuales'
        db.delete_table('territorios_titulosindividuales')

        # Deleting model 'Pueblo'
        db.delete_table('territorios_pueblo')

        # Deleting model 'TerritorioComunidad'
        db.delete_table('territorios_territoriocomunidad')

        # Removing M2M table for field municipios on 'TerritorioComunidad'
        db.delete_table('territorios_territoriocomunidad_municipios')

        # Deleting model 'TerritorioComunidadIndigena'
        db.delete_table('territorios_territoriocomunidadindigena')

        # Deleting model 'TerritorioComunidadNegra'
        db.delete_table('territorios_territoriocomunidadnegra')

        # Deleting model 'ComunidadNegra'
        db.delete_table('territorios_comunidadnegra')

        # Deleting model 'ComunidadIndigena'
        db.delete_table('territorios_comunidadindigena')

        # Deleting model 'Ampliacion'
        db.delete_table('territorios_ampliacion')

        # Deleting model 'Saneamiento'
        db.delete_table('territorios_saneamiento')

        # Deleting model 'SolicitudTitulacion'
        db.delete_table('territorios_solicitudtitulacion')

        # Deleting model 'PoblacionTerritorioColectivo'
        db.delete_table('territorios_poblacionterritoriocolectivo')

        # Deleting model 'PoblacionComunidadNegra'
        db.delete_table('territorios_poblacioncomunidadnegra')

        # Deleting model 'PoblacionComunidadIndigena'
        db.delete_table('territorios_poblacioncomunidadindigena')

        # Deleting model 'Ubicacion'
        db.delete_table('territorios_ubicacion')


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
        'territorios.ampliacion': {
            'Meta': {'object_name': 'Ampliacion'},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'estado_tramite': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limites': ('django.db.models.fields.TextField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resolucion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'territorios.comunidadindigena': {
            'Meta': {'object_name': 'ComunidadIndigena'},
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_creacion_ano': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_disolucion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_disolucion_ano': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pueblo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Pueblo']"}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidadIndigena']"})
        },
        'territorios.comunidadnegra': {
            'Meta': {'object_name': 'ComunidadNegra'},
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_creacion_ano': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_disolucion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_disolucion_ano': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidadNegra']"})
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
        'territorios.estadisticadepartamento': {
            'Meta': {'object_name': 'EstadisticaDepartamento'},
            'cabecera': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edad_0_a_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_10_a_14': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_15_a_19': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_20_a_24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_25_a_29': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_30_a_34': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_35_a_39': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_40_a_44': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_45_a_49': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_50_a_54': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_55_a_59': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_5_a_9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_60_a_64': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_65_a_69': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_70_a_74': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_75_a_79': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_80_a_84': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_85_a_89': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_90_o_mas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_no_informa': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'hombres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'masivo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mujeres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'rural': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.estadisticamunicipio': {
            'Meta': {'object_name': 'EstadisticaMunicipio'},
            'cabecera': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edad_0_a_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_10_a_14': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_15_a_19': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_20_a_24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_25_a_29': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_30_a_34': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_35_a_39': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_40_a_44': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_45_a_49': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_50_a_54': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_55_a_59': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_5_a_9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_60_a_64': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_65_a_69': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_70_a_74': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_75_a_79': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_80_a_84': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_85_a_89': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_90_o_mas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_no_informa': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'etnia_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'hombres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'masivo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mujeres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'rural': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Municipio']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
        'territorios.poblacioncomunidadindigena': {
            'Meta': {'object_name': 'PoblacionComunidadIndigena'},
            'edad_0_a_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_10_a_14': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_15_a_19': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_20_a_24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_25_a_29': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_30_a_34': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_35_a_39': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_40_a_44': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_45_a_49': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_50_a_54': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_55_a_59': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_5_a_9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_60_a_64': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_65_a_69': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_70_a_74': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_75_a_79': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_80_a_84': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_85_a_89': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_90_o_mas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'familias': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']"}),
            'hombres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estadistica_asentamiento'", 'to': "orm['territorios.ComunidadIndigena']"}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.poblacioncomunidadnegra': {
            'Meta': {'object_name': 'PoblacionComunidadNegra'},
            'edad_0_a_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_10_a_14': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_15_a_19': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_20_a_24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_25_a_29': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_30_a_34': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_35_a_39': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_40_a_44': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_45_a_49': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_50_a_54': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_55_a_59': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_5_a_9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_60_a_64': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_65_a_69': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_70_a_74': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_75_a_79': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_80_a_84': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_85_a_89': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_90_o_mas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'familias': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']"}),
            'hombres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estadistica_asentamiento'", 'to': "orm['territorios.ComunidadNegra']"}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.poblacionterritoriocolectivo': {
            'Meta': {'object_name': 'PoblacionTerritorioColectivo'},
            'edad_0_a_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_10_a_14': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_15_a_19': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_20_a_24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_25_a_29': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_30_a_34': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_35_a_39': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_40_a_44': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_45_a_49': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_50_a_54': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_55_a_59': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_5_a_9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_60_a_64': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_65_a_69': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_70_a_74': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_75_a_79': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_80_a_84': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_85_a_89': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'edad_90_o_mas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'familias': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']"}),
            'hombres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estadistica_comunidad'", 'to': "orm['territorios.TerritorioComunidad']"}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.pueblo': {
            'Meta': {'object_name': 'Pueblo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'territorios.saneamiento': {
            'Meta': {'object_name': 'Saneamiento'},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'estado_tramite': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limites': ('django.db.models.fields.TextField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'poblacion_afro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'poblacion_otros': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'poblacion_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resolucion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'territorios.solicitudtitulacion': {
            'Meta': {'object_name': 'SolicitudTitulacion'},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'estado_tramite': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limites': ('django.db.models.fields.TextField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resolucion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
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
        },
        'territorios.territoriocomunidadindigena': {
            'Meta': {'object_name': 'TerritorioComunidadIndigena', '_ormbases': ['territorios.TerritorioComunidad']},
            'territoriocomunidad_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['territorios.TerritorioComunidad']", 'unique': 'True', 'primary_key': 'True'})
        },
        'territorios.territoriocomunidadnegra': {
            'Meta': {'object_name': 'TerritorioComunidadNegra', '_ormbases': ['territorios.TerritorioComunidad']},
            'territoriocomunidad_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['territorios.TerritorioComunidad']", 'unique': 'True', 'primary_key': 'True'})
        },
        'territorios.titulosindividuales': {
            'Meta': {'object_name': 'TitulosIndividuales'},
            'area_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'titulos_individuales'", 'to': "orm['territorios.Municipio']"}),
            'fuente_titulos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'grupo_poblacional': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'territorios.ubicacion': {
            'Meta': {'object_name': 'Ubicacion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_ubicacio'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'content_type_ubicacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seleccionador': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'valor': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['territorios']
