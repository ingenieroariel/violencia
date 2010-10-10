# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PoblacionGrande'
        db.create_table('territorios_poblaciongrande', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('porcentaje_hombres', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('edad_0_9', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_10_19', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_20_29', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_30_39', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_40_49', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_50_59', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_60_69', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_70_79', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_80_89', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('porcentaje_indigena', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_afro', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_no_informa', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_cabecera', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_rural', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['PoblacionGrande'])

        # Adding model 'RecepcionDesplazados'
        db.create_table('territorios_recepciondesplazados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad_total', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_hombres', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_mujeres', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('edad_0_5', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_6_10', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_11_15', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_16_20', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_21_25', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_26_30', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_31_35', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_36_40', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_41_45', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_46_50', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_51_55', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_56_60', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_61_65', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_66_70', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_71_75', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_76_80', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_81_85', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_86_90', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_91_95', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('cantidad_indigena', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_afro', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_no_informa', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_individual', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_cabecera', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_rural', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['RecepcionDesplazados'])

        # Adding model 'ExpulsionDesplazados'
        db.create_table('territorios_expulsiondesplazados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad_total', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_hombres', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_mujeres', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('edad_0_5', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_6_10', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_11_15', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_16_20', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_21_25', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_26_30', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_31_35', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_36_40', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_41_45', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_46_50', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_51_55', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_56_60', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_61_65', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_66_70', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_71_75', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_76_80', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_81_85', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_86_90', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_91_95', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('cantidad_indigena', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_afro', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_no_informa', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_individual', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_cabecera', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_rural', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['ExpulsionDesplazados'])

        # Adding model 'PlanDesarrollo'
        db.create_table('territorios_plandesarrollo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('existe_plan_desarrollo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('periodo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['PlanDesarrollo'])

        # Adding model 'IngresoDepartamental'
        db.create_table('territorios_ingresodepartamental', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingreso_tributario_cerveza', self.gf('django.db.models.fields.IntegerField')()),
            ('ingreso_tributario_licores', self.gf('django.db.models.fields.IntegerField')()),
            ('ingreso_tributario_cigarillos_Tabaco', self.gf('django.db.models.fields.IntegerField')()),
            ('ingreso_tributario_registro_anotacion', self.gf('django.db.models.fields.IntegerField')()),
            ('ingreso_tributario_vehiculos_automotores', self.gf('django.db.models.fields.IntegerField')()),
            ('ingreso_tributario_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('ingreso_no_tributario_nivel_nacional', self.gf('django.db.models.fields.IntegerField')()),
            ('ingreso_no_tributario_otras', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_servicios_personales', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_generales', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_transferencias', self.gf('django.db.models.fields.IntegerField')()),
            ('intereses_deuda_externa', self.gf('django.db.models.fields.IntegerField')()),
            ('intereses_deuda_interna', self.gf('django.db.models.fields.IntegerField')()),
            ('transferencias_nivel_nacional', self.gf('django.db.models.fields.IntegerField')()),
            ('transferencias_otras', self.gf('django.db.models.fields.IntegerField')()),
            ('ingresos_capital_cofinanciacion', self.gf('django.db.models.fields.IntegerField')()),
            ('ingresos_capital_regalias', self.gf('django.db.models.fields.IntegerField')()),
            ('ingresos_capital_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_capital_formacion_bruta_capital_fijo', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_capital_inversion_social', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_capital_transferencias_capital', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_capital_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('credito_externo_desembolsos', self.gf('django.db.models.fields.IntegerField')()),
            ('credito_externo_amortizaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('credito_interno_desembolsos', self.gf('django.db.models.fields.IntegerField')()),
            ('credito_interno_amortizaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('variacion_depositos_y_otros', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['IngresoDepartamental'])

        # Adding model 'Departamento'
        db.create_table('territorios_departamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('tipo', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('area_total_urbana', self.gf('django.db.models.fields.TextField')()),
            ('area_total_rural', self.gf('django.db.models.fields.TextField')()),
            ('capital', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cantidad_municipios_total', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_municipios_pacifico', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')()),
            ('presupuesto_anual', self.gf('django.db.models.fields.IntegerField')()),
            ('ingresos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.IngresoDepartamental'])),
            ('poblacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PoblacionGrande'])),
            ('recepcion_desplazados', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.RecepcionDesplazados'])),
            ('expulsion_desplazados', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.ExpulsionDesplazados'])),
            ('capital_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rural_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('plan_desarrollo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PlanDesarrollo'])),
        ))
        db.send_create_signal('territorios', ['Departamento'])

        # Adding model 'Pueblo'
        db.create_table('territorios_pueblo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('territorios', ['Pueblo'])

        # Adding model 'PoblacionPequena'
        db.create_table('territorios_poblacionpequena', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad_hombres', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cantidad_mujeres', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('edad_0_5', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_6_10', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_11_15', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_16_20', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_21_25', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_26_30', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_31_35', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_36_40', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_41_45', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_46_50', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_51_55', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_56_60', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_61_65', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_66_70', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_71_75', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_76_80', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_81_85', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_86_90', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('edad_91_95', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('porcentaje_pueblos', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('territorios', ['PoblacionPequena'])

        # Adding model 'IngresoMunicipal'
        db.create_table('territorios_ingresomunicipal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('predial', self.gf('django.db.models.fields.IntegerField')()),
            ('industria_comercio', self.gf('django.db.models.fields.IntegerField')()),
            ('otros_ingresos', self.gf('django.db.models.fields.IntegerField')()),
            ('del_nivel_nacional', self.gf('django.db.models.fields.IntegerField')()),
            ('otras_transferencias', self.gf('django.db.models.fields.IntegerField')()),
            ('servicios_personales', self.gf('django.db.models.fields.IntegerField')()),
            ('gastos_generales', self.gf('django.db.models.fields.IntegerField')()),
            ('transferencias_pagadas', self.gf('django.db.models.fields.IntegerField')()),
            ('intereses_deuda_publica', self.gf('django.db.models.fields.IntegerField')()),
            ('otros_gastos_corrientes', self.gf('django.db.models.fields.IntegerField')()),
            ('deficit_o_ahorro_corriente', self.gf('django.db.models.fields.IntegerField')()),
            ('regalias', self.gf('django.db.models.fields.IntegerField')()),
            ('transferencias_nacionales', self.gf('django.db.models.fields.IntegerField')()),
            ('cofinanciacion', self.gf('django.db.models.fields.IntegerField')()),
            ('otros_ingresos_capital', self.gf('django.db.models.fields.IntegerField')()),
            ('formacion_brutal_capital_fijo', self.gf('django.db.models.fields.IntegerField')()),
            ('resto_inversiones', self.gf('django.db.models.fields.IntegerField')()),
            ('deficit_o_superavit_total', self.gf('django.db.models.fields.IntegerField')()),
            ('credito_interno', self.gf('django.db.models.fields.IntegerField')()),
            ('credito_externo', self.gf('django.db.models.fields.IntegerField')()),
            ('desembolsos', self.gf('django.db.models.fields.IntegerField')()),
            ('amortizaciones', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['IngresoMunicipal'])

        # Adding model 'PlanOrdenamiento'
        db.create_table('territorios_planordenamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('suelo_urbano_area', self.gf('django.db.models.fields.TextField')()),
            ('suelo_urbano_limite', self.gf('django.db.models.fields.TextField')()),
            ('expansion_urbana_area', self.gf('django.db.models.fields.TextField')()),
            ('expansion_urbana_limite', self.gf('django.db.models.fields.TextField')()),
            ('prod_agropecuaria_area', self.gf('django.db.models.fields.TextField')()),
            ('prod_agropecuaria_limite', self.gf('django.db.models.fields.TextField')()),
            ('sistema_ambiental_area', self.gf('django.db.models.fields.TextField')()),
            ('sistema_ambiental_limites', self.gf('django.db.models.fields.TextField')()),
            ('sistema_silvo_pastorial_area', self.gf('django.db.models.fields.TextField')()),
            ('sistema_silvo_pastorial_limites', self.gf('django.db.models.fields.TextField')()),
            ('sistema_forestal_area', self.gf('django.db.models.fields.TextField')()),
            ('sistema_forestal_limites', self.gf('django.db.models.fields.TextField')()),
            ('zonas_vida_area', self.gf('django.db.models.fields.TextField')()),
            ('zonas_vida_limites', self.gf('django.db.models.fields.TextField')()),
            ('cuencas_hidrograficas_area', self.gf('django.db.models.fields.TextField')()),
            ('cuencas_hidrograficas_limite', self.gf('django.db.models.fields.TextField')()),
            ('uso_cobertura_vegetal_tipo', self.gf('django.db.models.fields.TextField')()),
            ('uso_cobertura_vegetal_area', self.gf('django.db.models.fields.TextField')()),
            ('area_rutal_suelos_tipos', self.gf('django.db.models.fields.TextField')()),
            ('riesgos_amenazas_ubicacion', self.gf('django.db.models.fields.TextField')()),
            ('riesgos_amenazas_descripcion', self.gf('django.db.models.fields.TextField')()),
            ('mapa_politico_administrativo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('mapa_uso_generales_del_suelo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('territorios', ['PlanOrdenamiento'])

        # Adding model 'Asentamiento'
        db.create_table('territorios_asentamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')()),
            ('decha_disolucion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('territorios', ['Asentamiento'])

        # Adding model 'Municipio'
        db.create_table('territorios_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
            ('tipo', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('presupuesto_anual', self.gf('django.db.models.fields.IntegerField')()),
            ('ingresos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.IngresoMunicipal'])),
            ('poblacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PoblacionGrande'])),
            ('recepcion_desplazados', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.RecepcionDesplazados'])),
            ('expulsion_desplazados', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.ExpulsionDesplazados'])),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('cabecera_individuales_cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('cabecera_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cabecera_grupo_poblacional', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('rural_individuales_cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('rural_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rural_grupo_poblacional', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('plan_ordenamiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PlanOrdenamiento'])),
            ('plan_desarrollo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PlanDesarrollo'])),
        ))
        db.send_create_signal('territorios', ['Municipio'])

        # Adding model 'LimiteMunicipio'
        db.create_table('territorios_limitemunicipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='limites', to=orm['territorios.Municipio'])),
        ))
        db.send_create_signal('territorios', ['LimiteMunicipio'])

        # Adding model 'LimiteDepartamento'
        db.create_table('territorios_limitedepartamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='limites', to=orm['territorios.Departamento'])),
        ))
        db.send_create_signal('territorios', ['LimiteDepartamento'])

        # Adding model 'Titulacion'
        db.create_table('territorios_titulacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resolucion_fecha', self.gf('django.db.models.fields.DateField')()),
            ('resolucion_codigo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('limites', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estado_tramite', self.gf('django.db.models.fields.CharField')(default='S', max_length=2)),
        ))
        db.send_create_signal('territorios', ['Titulacion'])

        # Adding model 'Saneamiento'
        db.create_table('territorios_saneamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ampliacion_resolucion_fecha', self.gf('django.db.models.fields.DateField')()),
            ('ampliacion_resolucion_codigo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ampliacion_limites', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ampliacion_estado_tramite', self.gf('django.db.models.fields.CharField')(default='S', max_length=2)),
            ('saneamiento_resolucion_fecha', self.gf('django.db.models.fields.DateField')()),
            ('saneamiento_resolucion_codigo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('saneamiento_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('saneamiento_poblacion_general', self.gf('django.db.models.fields.IntegerField')()),
            ('saneamiento_poblacion_afro', self.gf('django.db.models.fields.IntegerField')()),
            ('saneamiento_poblacion_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('saneamiento_limites', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('saneamiento_estado_tramite', self.gf('django.db.models.fields.CharField')(default='S', max_length=2)),
        ))
        db.send_create_signal('territorios', ['Saneamiento'])

        # Adding model 'TerritorioIndio'
        db.create_table('territorios_territorioindio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
            ('poblacion_total', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PoblacionPequena'])),
            ('resolucion_constitucion', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('limites', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('situacion_juridica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Saneamiento'])),
        ))
        db.send_create_signal('territorios', ['TerritorioIndio'])

        # Adding M2M table for field asentamientos on 'TerritorioIndio'
        db.create_table('territorios_territorioindio_asentamientos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorioindio', models.ForeignKey(orm['territorios.territorioindio'], null=False)),
            ('asentamiento', models.ForeignKey(orm['territorios.asentamiento'], null=False))
        ))
        db.create_unique('territorios_territorioindio_asentamientos', ['territorioindio_id', 'asentamiento_id'])

        # Adding M2M table for field municipios on 'TerritorioIndio'
        db.create_table('territorios_territorioindio_municipios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorioindio', models.ForeignKey(orm['territorios.territorioindio'], null=False)),
            ('municipio', models.ForeignKey(orm['territorios.municipio'], null=False))
        ))
        db.create_unique('territorios_territorioindio_municipios', ['territorioindio_id', 'municipio_id'])

        # Adding M2M table for field pueblos on 'TerritorioIndio'
        db.create_table('territorios_territorioindio_pueblos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorioindio', models.ForeignKey(orm['territorios.territorioindio'], null=False)),
            ('pueblo', models.ForeignKey(orm['territorios.pueblo'], null=False))
        ))
        db.create_unique('territorios_territorioindio_pueblos', ['territorioindio_id', 'pueblo_id'])

        # Adding model 'TerritorioIndioNoTitulado'
        db.create_table('territorios_territorioindionotitulado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
            ('poblacion_total', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PoblacionPequena'])),
            ('area_solicitada', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('situacion_juridica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Titulacion'])),
        ))
        db.send_create_signal('territorios', ['TerritorioIndioNoTitulado'])

        # Adding M2M table for field asentamientos on 'TerritorioIndioNoTitulado'
        db.create_table('territorios_territorioindionotitulado_asentamientos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorioindionotitulado', models.ForeignKey(orm['territorios.territorioindionotitulado'], null=False)),
            ('asentamiento', models.ForeignKey(orm['territorios.asentamiento'], null=False))
        ))
        db.create_unique('territorios_territorioindionotitulado_asentamientos', ['territorioindionotitulado_id', 'asentamiento_id'])

        # Adding M2M table for field municipios on 'TerritorioIndioNoTitulado'
        db.create_table('territorios_territorioindionotitulado_municipios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorioindionotitulado', models.ForeignKey(orm['territorios.territorioindionotitulado'], null=False)),
            ('municipio', models.ForeignKey(orm['territorios.municipio'], null=False))
        ))
        db.create_unique('territorios_territorioindionotitulado_municipios', ['territorioindionotitulado_id', 'municipio_id'])

        # Adding M2M table for field pueblos on 'TerritorioIndioNoTitulado'
        db.create_table('territorios_territorioindionotitulado_pueblos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorioindionotitulado', models.ForeignKey(orm['territorios.territorioindionotitulado'], null=False)),
            ('pueblo', models.ForeignKey(orm['territorios.pueblo'], null=False))
        ))
        db.create_unique('territorios_territorioindionotitulado_pueblos', ['territorioindionotitulado_id', 'pueblo_id'])

        # Adding model 'TerritorioNegro'
        db.create_table('territorios_territorionegro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
            ('poblacion_total', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PoblacionPequena'])),
            ('resolucion_constitucion', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('limites', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('territorios', ['TerritorioNegro'])

        # Adding M2M table for field asentamientos on 'TerritorioNegro'
        db.create_table('territorios_territorionegro_asentamientos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorionegro', models.ForeignKey(orm['territorios.territorionegro'], null=False)),
            ('asentamiento', models.ForeignKey(orm['territorios.asentamiento'], null=False))
        ))
        db.create_unique('territorios_territorionegro_asentamientos', ['territorionegro_id', 'asentamiento_id'])

        # Adding M2M table for field municipios on 'TerritorioNegro'
        db.create_table('territorios_territorionegro_municipios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorionegro', models.ForeignKey(orm['territorios.territorionegro'], null=False)),
            ('municipio', models.ForeignKey(orm['territorios.municipio'], null=False))
        ))
        db.create_unique('territorios_territorionegro_municipios', ['territorionegro_id', 'municipio_id'])

        # Adding model 'TerritorioNegroNoTitulado'
        db.create_table('territorios_territorionegronotitulado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
            ('poblacion_total', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.PoblacionPequena'])),
            ('area_solicitada', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('situacion_juridica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Titulacion'])),
        ))
        db.send_create_signal('territorios', ['TerritorioNegroNoTitulado'])

        # Adding M2M table for field asentamientos on 'TerritorioNegroNoTitulado'
        db.create_table('territorios_territorionegronotitulado_asentamientos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorionegronotitulado', models.ForeignKey(orm['territorios.territorionegronotitulado'], null=False)),
            ('asentamiento', models.ForeignKey(orm['territorios.asentamiento'], null=False))
        ))
        db.create_unique('territorios_territorionegronotitulado_asentamientos', ['territorionegronotitulado_id', 'asentamiento_id'])

        # Adding M2M table for field municipios on 'TerritorioNegroNoTitulado'
        db.create_table('territorios_territorionegronotitulado_municipios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('territorionegronotitulado', models.ForeignKey(orm['territorios.territorionegronotitulado'], null=False)),
            ('municipio', models.ForeignKey(orm['territorios.municipio'], null=False))
        ))
        db.create_unique('territorios_territorionegronotitulado_municipios', ['territorionegronotitulado_id', 'municipio_id'])

        # Adding model 'Conflicto'
        db.create_table('territorios_conflicto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_etnico', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipo_conflicto', self.gf('django.db.models.fields.IntegerField')()),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('actores', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hechos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('fuente', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='conflictos_creados', to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='conflictos_modificados', to=orm['auth.User'])),
        ))
        db.send_create_signal('territorios', ['Conflicto'])

        # Adding model 'InstitucionEducativa'
        db.create_table('territorios_institucioneducativa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('institucion', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_constitucion', self.gf('django.db.models.fields.DateField')()),
            ('enfasis', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('etnoeducacion_en_pei', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('educacion_especial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('educacion_especial_porcentaje', self.gf('django.db.models.fields.IntegerField')()),
            ('educacion_adultos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('educacion_adultos_porcentaje', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_nombrados_total', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_nombrados_indigenas', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_nombrados_afro', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_nombrados_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_nombrados_en_ejercicio', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_temporales_total', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_temporales_indigena', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_temporales_afro', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_temporales_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('maestros_temporales_en_ejercicio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['InstitucionEducativa'])

        # Adding model 'PoblacionEstudiantilPreescolar'
        db.create_table('territorios_poblacionestudiantilpreescolar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['PoblacionEstudiantilPreescolar'])

        # Adding model 'PoblacionEstudiantilBasicaPrimaria'
        db.create_table('territorios_poblacionestudiantilbasicaprimaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['PoblacionEstudiantilBasicaPrimaria'])

        # Adding model 'PoblacionEstudiantilBasicaSecundaria'
        db.create_table('territorios_poblacionestudiantilbasicasecundaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['PoblacionEstudiantilBasicaSecundaria'])

        # Adding model 'PoblacionEstudiantilMediaVocacional'
        db.create_table('territorios_poblacionestudiantilmediavocacional', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['PoblacionEstudiantilMediaVocacional'])

        # Adding model 'CoberturaEstudiantilPreescolar'
        db.create_table('territorios_coberturaestudiantilpreescolar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaEstudiantilPreescolar'])

        # Adding model 'CoberturaEstudiantilBasicaPrimaria'
        db.create_table('territorios_coberturaestudiantilbasicaprimaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaEstudiantilBasicaPrimaria'])

        # Adding model 'CoberturaEstudiantilBasicaSecundaria'
        db.create_table('territorios_coberturaestudiantilbasicasecundaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaEstudiantilBasicaSecundaria'])

        # Adding model 'CoberturaEstudiantilMediaVocacional'
        db.create_table('territorios_coberturaestudiantilmediavocacional', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaEstudiantilMediaVocacional'])

        # Adding model 'CoberturaDesplazadosPreescolar'
        db.create_table('territorios_coberturadesplazadospreescolar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaDesplazadosPreescolar'])

        # Adding model 'CoberturaDesplazadosPrimaria'
        db.create_table('territorios_coberturadesplazadosprimaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaDesplazadosPrimaria'])

        # Adding model 'CoberturaDesplazadosSecundaria'
        db.create_table('territorios_coberturadesplazadossecundaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaDesplazadosSecundaria'])

        # Adding model 'CoberturaDesplazadosMedia'
        db.create_table('territorios_coberturadesplazadosmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['CoberturaDesplazadosMedia'])

        # Adding model 'EstudiantesDesercion'
        db.create_table('territorios_estudiantesdesercion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['EstudiantesDesercion'])

        # Adding model 'EstudiantesPromocion'
        db.create_table('territorios_estudiantespromocion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['EstudiantesPromocion'])

        # Adding model 'EstudiantesRepitencia'
        db.create_table('territorios_estudiantesrepitencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['EstudiantesRepitencia'])

        # Adding model 'EstudiantesAnalfabetismo'
        db.create_table('territorios_estudiantesanalfabetismo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('institucion_educativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.InstitucionEducativa'])),
        ))
        db.send_create_signal('territorios', ['EstudiantesAnalfabetismo'])

        # Adding model 'EntidadContratante'
        db.create_table('territorios_entidadcontratante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('territorios', ['EntidadContratante'])

        # Adding model 'Promotores'
        db.create_table('territorios_promotores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_contrato', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['Promotores'])

        # Adding M2M table for field entidades on 'Promotores'
        db.create_table('territorios_promotores_entidades', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotores', models.ForeignKey(orm['territorios.promotores'], null=False)),
            ('entidadcontratante', models.ForeignKey(orm['territorios.entidadcontratante'], null=False))
        ))
        db.create_unique('territorios_promotores_entidades', ['promotores_id', 'entidadcontratante_id'])

        # Adding model 'Instalaciones'
        db.create_table('territorios_instalaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nivel_de_atencion', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('territorios', ['Instalaciones'])

        # Adding model 'EmpresaPrestadoraRegimenSubsidiario'
        db.create_table('territorios_empresaprestadoraregimensubsidiario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('territorios', ['EmpresaPrestadoraRegimenSubsidiario'])

        # Adding model 'Regimen'
        db.create_table('territorios_regimen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_poblacion', self.gf('django.db.models.fields.IntegerField')()),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['Regimen'])

        # Adding M2M table for field empresas on 'Regimen'
        db.create_table('territorios_regimen_empresas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('regimen', models.ForeignKey(orm['territorios.regimen'], null=False)),
            ('empresaprestadoraregimensubsidiario', models.ForeignKey(orm['territorios.empresaprestadoraregimensubsidiario'], null=False))
        ))
        db.create_unique('territorios_regimen_empresas', ['regimen_id', 'empresaprestadoraregimensubsidiario_id'])

        # Adding model 'SistemaSalud'
        db.create_table('territorios_sistemasalud', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('territorios', ['SistemaSalud'])

        # Adding M2M table for field promotores on 'SistemaSalud'
        db.create_table('territorios_sistemasalud_promotores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sistemasalud', models.ForeignKey(orm['territorios.sistemasalud'], null=False)),
            ('promotores', models.ForeignKey(orm['territorios.promotores'], null=False))
        ))
        db.create_unique('territorios_sistemasalud_promotores', ['sistemasalud_id', 'promotores_id'])

        # Adding M2M table for field instalaciones on 'SistemaSalud'
        db.create_table('territorios_sistemasalud_instalaciones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sistemasalud', models.ForeignKey(orm['territorios.sistemasalud'], null=False)),
            ('instalaciones', models.ForeignKey(orm['territorios.instalaciones'], null=False))
        ))
        db.create_unique('territorios_sistemasalud_instalaciones', ['sistemasalud_id', 'instalaciones_id'])

        # Adding M2M table for field regimenes on 'SistemaSalud'
        db.create_table('territorios_sistemasalud_regimenes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sistemasalud', models.ForeignKey(orm['territorios.sistemasalud'], null=False)),
            ('regimen', models.ForeignKey(orm['territorios.regimen'], null=False))
        ))
        db.create_unique('territorios_sistemasalud_regimenes', ['sistemasalud_id', 'regimen_id'])

        # Adding model 'Desc'
        db.create_table('territorios_desc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingresos_publicos_valor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ingresos_publicos_rango', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('indice_desarrollo_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('indice_desarrollo_rango', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_total', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_rango', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_total_rural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_porcentaje_rural', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_rango_rutal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_total_urbano', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_porcentaje_urbano', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('necesidades_insatisfechas_rango_urbano', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('indice_condiciones_vida_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('indice_condiciones_vida_rango', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('morbilidad_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('morbilidad_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('morbi_mortalidad_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('morbi_mortalidad_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sistema_salud', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.SistemaSalud'])),
        ))
        db.send_create_signal('territorios', ['Desc'])

        # Adding M2M table for field instituciones_educativas_cabecera on 'Desc'
        db.create_table('territorios_desc_instituciones_educativas_cabecera', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('desc', models.ForeignKey(orm['territorios.desc'], null=False)),
            ('institucioneducativa', models.ForeignKey(orm['territorios.institucioneducativa'], null=False))
        ))
        db.create_unique('territorios_desc_instituciones_educativas_cabecera', ['desc_id', 'institucioneducativa_id'])

        # Adding M2M table for field instituciones_educativas_rural on 'Desc'
        db.create_table('territorios_desc_instituciones_educativas_rural', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('desc', models.ForeignKey(orm['territorios.desc'], null=False)),
            ('institucioneducativa', models.ForeignKey(orm['territorios.institucioneducativa'], null=False))
        ))
        db.create_unique('territorios_desc_instituciones_educativas_rural', ['desc_id', 'institucioneducativa_id'])

        # Adding model 'EsperanzaVida'
        db.create_table('territorios_esperanzavida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EsperanzaVida'])

        # Adding model 'MortalidadTotal'
        db.create_table('territorios_mortalidadtotal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['MortalidadTotal'])

        # Adding model 'MortalidadInfantil'
        db.create_table('territorios_mortalidadinfantil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['MortalidadInfantil'])

        # Adding model 'MortalidadMaternoInfantil'
        db.create_table('territorios_mortalidadmaternoinfantil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['MortalidadMaternoInfantil'])

        # Adding model 'TasaAnalfabetizacion'
        db.create_table('territorios_tasaanalfabetizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
            ('rural_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rural_rango', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('urbano_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('urbano_rango', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('todos_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('todos_rango', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('territorios', ['TasaAnalfabetizacion'])

        # Adding model 'Matriculas'
        db.create_table('territorios_matriculas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['Matriculas'])

        # Adding model 'EducacionPreescolar'
        db.create_table('territorios_educacionpreescolar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionPreescolar'])

        # Adding model 'EducacionPrimaria'
        db.create_table('territorios_educacionprimaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionPrimaria'])

        # Adding model 'EducacionSecundaria'
        db.create_table('territorios_educacionsecundaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionSecundaria'])

        # Adding model 'EducacionVocacional'
        db.create_table('territorios_educacionvocacional', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionVocacional'])

        # Adding model 'EducacionTecnica'
        db.create_table('territorios_educaciontecnica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionTecnica'])

        # Adding model 'EducacionNormalista'
        db.create_table('territorios_educacionnormalista', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionNormalista'])

        # Adding model 'EducacionTecnicaTecnologica'
        db.create_table('territorios_educaciontecnicatecnologica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionTecnicaTecnologica'])

        # Adding model 'EducacionSuperior'
        db.create_table('territorios_educacionsuperior', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rango', self.gf('django.db.models.fields.CharField')(default='0-0', max_length=50)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('indigena', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('afro', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
        ))
        db.send_create_signal('territorios', ['EducacionSuperior'])

        # Adding model 'ICBF'
        db.create_table('territorios_icbf', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
            ('poblacion_indigena_infantil_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_infantil_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_infantil_duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_escolar_duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_escolar_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_escolar_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_madres_duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_madres_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_madres_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_discapacitada_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_discapacitada_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_discapacitada_duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_abandono_duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_abandono_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_abandono_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_otro_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_otro_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_indigena_otro_duracion', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_afro_infantil_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_afro_madres_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_afro_otros_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_afro_escolar_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_otro_infantil_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_otro_madres_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_otro_otros_cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('poblacion_otro_escolar_cobertura', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['ICBF'])

        # Adding model 'Economia'
        db.create_table('territorios_economia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
            ('desempleo_informal', self.gf('django.db.models.fields.IntegerField')()),
            ('desempleo_formal', self.gf('django.db.models.fields.IntegerField')()),
            ('empleo_publico', self.gf('django.db.models.fields.IntegerField')()),
            ('empleo_privado', self.gf('django.db.models.fields.IntegerField')()),
            ('contrato_fijo', self.gf('django.db.models.fields.IntegerField')()),
            ('contrato_temporal', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('territorios', ['Economia'])

        # Adding model 'Cultura'
        db.create_table('territorios_cultura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Desc'])),
            ('existe_promocion_y_proteccion_lengua_indigena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcion_promocion_y_proteccion_lengua_indigena', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('territorios', ['Cultura'])

        # Adding model 'ServicioPublico'
        db.create_table('territorios_serviciopublico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.related.ForeignKey')(related_name='servicios_publicos', to=orm['territorios.Desc'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cobertura_rural_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cobertura_rural_rango', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cobertura_urbana_porcentaje', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cobertura_urbana_rango', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('territorios', ['ServicioPublico'])


    def backwards(self, orm):
        
        # Deleting model 'PoblacionGrande'
        db.delete_table('territorios_poblaciongrande')

        # Deleting model 'RecepcionDesplazados'
        db.delete_table('territorios_recepciondesplazados')

        # Deleting model 'ExpulsionDesplazados'
        db.delete_table('territorios_expulsiondesplazados')

        # Deleting model 'PlanDesarrollo'
        db.delete_table('territorios_plandesarrollo')

        # Deleting model 'IngresoDepartamental'
        db.delete_table('territorios_ingresodepartamental')

        # Deleting model 'Departamento'
        db.delete_table('territorios_departamento')

        # Deleting model 'Pueblo'
        db.delete_table('territorios_pueblo')

        # Deleting model 'PoblacionPequena'
        db.delete_table('territorios_poblacionpequena')

        # Deleting model 'IngresoMunicipal'
        db.delete_table('territorios_ingresomunicipal')

        # Deleting model 'PlanOrdenamiento'
        db.delete_table('territorios_planordenamiento')

        # Deleting model 'Asentamiento'
        db.delete_table('territorios_asentamiento')

        # Deleting model 'Municipio'
        db.delete_table('territorios_municipio')

        # Deleting model 'LimiteMunicipio'
        db.delete_table('territorios_limitemunicipio')

        # Deleting model 'LimiteDepartamento'
        db.delete_table('territorios_limitedepartamento')

        # Deleting model 'Titulacion'
        db.delete_table('territorios_titulacion')

        # Deleting model 'Saneamiento'
        db.delete_table('territorios_saneamiento')

        # Deleting model 'TerritorioIndio'
        db.delete_table('territorios_territorioindio')

        # Removing M2M table for field asentamientos on 'TerritorioIndio'
        db.delete_table('territorios_territorioindio_asentamientos')

        # Removing M2M table for field municipios on 'TerritorioIndio'
        db.delete_table('territorios_territorioindio_municipios')

        # Removing M2M table for field pueblos on 'TerritorioIndio'
        db.delete_table('territorios_territorioindio_pueblos')

        # Deleting model 'TerritorioIndioNoTitulado'
        db.delete_table('territorios_territorioindionotitulado')

        # Removing M2M table for field asentamientos on 'TerritorioIndioNoTitulado'
        db.delete_table('territorios_territorioindionotitulado_asentamientos')

        # Removing M2M table for field municipios on 'TerritorioIndioNoTitulado'
        db.delete_table('territorios_territorioindionotitulado_municipios')

        # Removing M2M table for field pueblos on 'TerritorioIndioNoTitulado'
        db.delete_table('territorios_territorioindionotitulado_pueblos')

        # Deleting model 'TerritorioNegro'
        db.delete_table('territorios_territorionegro')

        # Removing M2M table for field asentamientos on 'TerritorioNegro'
        db.delete_table('territorios_territorionegro_asentamientos')

        # Removing M2M table for field municipios on 'TerritorioNegro'
        db.delete_table('territorios_territorionegro_municipios')

        # Deleting model 'TerritorioNegroNoTitulado'
        db.delete_table('territorios_territorionegronotitulado')

        # Removing M2M table for field asentamientos on 'TerritorioNegroNoTitulado'
        db.delete_table('territorios_territorionegronotitulado_asentamientos')

        # Removing M2M table for field municipios on 'TerritorioNegroNoTitulado'
        db.delete_table('territorios_territorionegronotitulado_municipios')

        # Deleting model 'Conflicto'
        db.delete_table('territorios_conflicto')

        # Deleting model 'InstitucionEducativa'
        db.delete_table('territorios_institucioneducativa')

        # Deleting model 'PoblacionEstudiantilPreescolar'
        db.delete_table('territorios_poblacionestudiantilpreescolar')

        # Deleting model 'PoblacionEstudiantilBasicaPrimaria'
        db.delete_table('territorios_poblacionestudiantilbasicaprimaria')

        # Deleting model 'PoblacionEstudiantilBasicaSecundaria'
        db.delete_table('territorios_poblacionestudiantilbasicasecundaria')

        # Deleting model 'PoblacionEstudiantilMediaVocacional'
        db.delete_table('territorios_poblacionestudiantilmediavocacional')

        # Deleting model 'CoberturaEstudiantilPreescolar'
        db.delete_table('territorios_coberturaestudiantilpreescolar')

        # Deleting model 'CoberturaEstudiantilBasicaPrimaria'
        db.delete_table('territorios_coberturaestudiantilbasicaprimaria')

        # Deleting model 'CoberturaEstudiantilBasicaSecundaria'
        db.delete_table('territorios_coberturaestudiantilbasicasecundaria')

        # Deleting model 'CoberturaEstudiantilMediaVocacional'
        db.delete_table('territorios_coberturaestudiantilmediavocacional')

        # Deleting model 'CoberturaDesplazadosPreescolar'
        db.delete_table('territorios_coberturadesplazadospreescolar')

        # Deleting model 'CoberturaDesplazadosPrimaria'
        db.delete_table('territorios_coberturadesplazadosprimaria')

        # Deleting model 'CoberturaDesplazadosSecundaria'
        db.delete_table('territorios_coberturadesplazadossecundaria')

        # Deleting model 'CoberturaDesplazadosMedia'
        db.delete_table('territorios_coberturadesplazadosmedia')

        # Deleting model 'EstudiantesDesercion'
        db.delete_table('territorios_estudiantesdesercion')

        # Deleting model 'EstudiantesPromocion'
        db.delete_table('territorios_estudiantespromocion')

        # Deleting model 'EstudiantesRepitencia'
        db.delete_table('territorios_estudiantesrepitencia')

        # Deleting model 'EstudiantesAnalfabetismo'
        db.delete_table('territorios_estudiantesanalfabetismo')

        # Deleting model 'EntidadContratante'
        db.delete_table('territorios_entidadcontratante')

        # Deleting model 'Promotores'
        db.delete_table('territorios_promotores')

        # Removing M2M table for field entidades on 'Promotores'
        db.delete_table('territorios_promotores_entidades')

        # Deleting model 'Instalaciones'
        db.delete_table('territorios_instalaciones')

        # Deleting model 'EmpresaPrestadoraRegimenSubsidiario'
        db.delete_table('territorios_empresaprestadoraregimensubsidiario')

        # Deleting model 'Regimen'
        db.delete_table('territorios_regimen')

        # Removing M2M table for field empresas on 'Regimen'
        db.delete_table('territorios_regimen_empresas')

        # Deleting model 'SistemaSalud'
        db.delete_table('territorios_sistemasalud')

        # Removing M2M table for field promotores on 'SistemaSalud'
        db.delete_table('territorios_sistemasalud_promotores')

        # Removing M2M table for field instalaciones on 'SistemaSalud'
        db.delete_table('territorios_sistemasalud_instalaciones')

        # Removing M2M table for field regimenes on 'SistemaSalud'
        db.delete_table('territorios_sistemasalud_regimenes')

        # Deleting model 'Desc'
        db.delete_table('territorios_desc')

        # Removing M2M table for field instituciones_educativas_cabecera on 'Desc'
        db.delete_table('territorios_desc_instituciones_educativas_cabecera')

        # Removing M2M table for field instituciones_educativas_rural on 'Desc'
        db.delete_table('territorios_desc_instituciones_educativas_rural')

        # Deleting model 'EsperanzaVida'
        db.delete_table('territorios_esperanzavida')

        # Deleting model 'MortalidadTotal'
        db.delete_table('territorios_mortalidadtotal')

        # Deleting model 'MortalidadInfantil'
        db.delete_table('territorios_mortalidadinfantil')

        # Deleting model 'MortalidadMaternoInfantil'
        db.delete_table('territorios_mortalidadmaternoinfantil')

        # Deleting model 'TasaAnalfabetizacion'
        db.delete_table('territorios_tasaanalfabetizacion')

        # Deleting model 'Matriculas'
        db.delete_table('territorios_matriculas')

        # Deleting model 'EducacionPreescolar'
        db.delete_table('territorios_educacionpreescolar')

        # Deleting model 'EducacionPrimaria'
        db.delete_table('territorios_educacionprimaria')

        # Deleting model 'EducacionSecundaria'
        db.delete_table('territorios_educacionsecundaria')

        # Deleting model 'EducacionVocacional'
        db.delete_table('territorios_educacionvocacional')

        # Deleting model 'EducacionTecnica'
        db.delete_table('territorios_educaciontecnica')

        # Deleting model 'EducacionNormalista'
        db.delete_table('territorios_educacionnormalista')

        # Deleting model 'EducacionTecnicaTecnologica'
        db.delete_table('territorios_educaciontecnicatecnologica')

        # Deleting model 'EducacionSuperior'
        db.delete_table('territorios_educacionsuperior')

        # Deleting model 'ICBF'
        db.delete_table('territorios_icbf')

        # Deleting model 'Economia'
        db.delete_table('territorios_economia')

        # Deleting model 'Cultura'
        db.delete_table('territorios_cultura')

        # Deleting model 'ServicioPublico'
        db.delete_table('territorios_serviciopublico')


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
        'territorios.asentamiento': {
            'Meta': {'object_name': 'Asentamiento'},
            'decha_disolucion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'territorios.coberturadesplazadosmedia': {
            'Meta': {'object_name': 'CoberturaDesplazadosMedia'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.coberturadesplazadospreescolar': {
            'Meta': {'object_name': 'CoberturaDesplazadosPreescolar'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.coberturadesplazadosprimaria': {
            'Meta': {'object_name': 'CoberturaDesplazadosPrimaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.coberturadesplazadossecundaria': {
            'Meta': {'object_name': 'CoberturaDesplazadosSecundaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.coberturaestudiantilbasicaprimaria': {
            'Meta': {'object_name': 'CoberturaEstudiantilBasicaPrimaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.coberturaestudiantilbasicasecundaria': {
            'Meta': {'object_name': 'CoberturaEstudiantilBasicaSecundaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.coberturaestudiantilmediavocacional': {
            'Meta': {'object_name': 'CoberturaEstudiantilMediaVocacional'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.coberturaestudiantilpreescolar': {
            'Meta': {'object_name': 'CoberturaEstudiantilPreescolar'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.conflicto': {
            'Meta': {'object_name': 'Conflicto'},
            'actores': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conflictos_creados'", 'to': "orm['auth.User']"}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fuente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hechos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conflictos_modificados'", 'to': "orm['auth.User']"}),
            'tipo_conflicto': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_etnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'territorios.cultura': {
            'Meta': {'object_name': 'Cultura'},
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'descripcion_promocion_y_proteccion_lengua_indigena': ('django.db.models.fields.TextField', [], {}),
            'existe_promocion_y_proteccion_lengua_indigena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'territorios.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'area_total_rural': ('django.db.models.fields.TextField', [], {}),
            'area_total_urbana': ('django.db.models.fields.TextField', [], {}),
            'cantidad_municipios_pacifico': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_municipios_total': ('django.db.models.fields.IntegerField', [], {}),
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'capital_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'expulsion_desplazados': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.ExpulsionDesplazados']"}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.IngresoDepartamental']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plan_desarrollo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PlanDesarrollo']"}),
            'poblacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PoblacionGrande']"}),
            'presupuesto_anual': ('django.db.models.fields.IntegerField', [], {}),
            'recepcion_desplazados': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.RecepcionDesplazados']"}),
            'rural_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'territorios.desc': {
            'Meta': {'object_name': 'Desc'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indice_condiciones_vida_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'indice_condiciones_vida_rango': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'indice_desarrollo_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'indice_desarrollo_rango': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ingresos_publicos_rango': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ingresos_publicos_valor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'instituciones_educativas_cabecera': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'descs_cabecera'", 'symmetrical': 'False', 'to': "orm['territorios.InstitucionEducativa']"}),
            'instituciones_educativas_rural': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'descs_rural'", 'symmetrical': 'False', 'to': "orm['territorios.InstitucionEducativa']"}),
            'morbi_mortalidad_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'morbi_mortalidad_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'morbilidad_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'morbilidad_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'necesidades_insatisfechas_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_porcentaje_rural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_porcentaje_urbano': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_rango': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_rango_rutal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_rango_urbano': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_total': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_total_rural': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'necesidades_insatisfechas_total_urbano': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sistema_salud': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.SistemaSalud']"})
        },
        'territorios.economia': {
            'Meta': {'object_name': 'Economia'},
            'contrato_fijo': ('django.db.models.fields.IntegerField', [], {}),
            'contrato_temporal': ('django.db.models.fields.IntegerField', [], {}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'desempleo_formal': ('django.db.models.fields.IntegerField', [], {}),
            'desempleo_informal': ('django.db.models.fields.IntegerField', [], {}),
            'empleo_privado': ('django.db.models.fields.IntegerField', [], {}),
            'empleo_publico': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'territorios.educacionnormalista': {
            'Meta': {'object_name': 'EducacionNormalista'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.educacionpreescolar': {
            'Meta': {'object_name': 'EducacionPreescolar'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.educacionprimaria': {
            'Meta': {'object_name': 'EducacionPrimaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.educacionsecundaria': {
            'Meta': {'object_name': 'EducacionSecundaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.educacionsuperior': {
            'Meta': {'object_name': 'EducacionSuperior'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.educaciontecnica': {
            'Meta': {'object_name': 'EducacionTecnica'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.educaciontecnicatecnologica': {
            'Meta': {'object_name': 'EducacionTecnicaTecnologica'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.educacionvocacional': {
            'Meta': {'object_name': 'EducacionVocacional'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.empresaprestadoraregimensubsidiario': {
            'Meta': {'object_name': 'EmpresaPrestadoraRegimenSubsidiario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'territorios.entidadcontratante': {
            'Meta': {'object_name': 'EntidadContratante'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'territorios.esperanzavida': {
            'Meta': {'object_name': 'EsperanzaVida'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.estudiantesanalfabetismo': {
            'Meta': {'object_name': 'EstudiantesAnalfabetismo'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.estudiantesdesercion': {
            'Meta': {'object_name': 'EstudiantesDesercion'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.estudiantespromocion': {
            'Meta': {'object_name': 'EstudiantesPromocion'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.estudiantesrepitencia': {
            'Meta': {'object_name': 'EstudiantesRepitencia'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.expulsiondesplazados': {
            'Meta': {'object_name': 'ExpulsionDesplazados'},
            'cantidad_afro': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_cabecera': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_hombres': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_indigena': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_individual': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_mujeres': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_no_informa': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_otros': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_rural': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_total': ('django.db.models.fields.SmallIntegerField', [], {}),
            'edad_0_5': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_11_15': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_16_20': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_21_25': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_26_30': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_31_35': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_36_40': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_41_45': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_46_50': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_51_55': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_56_60': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_61_65': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_66_70': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_6_10': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_71_75': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_76_80': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_81_85': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_86_90': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_91_95': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'territorios.icbf': {
            'Meta': {'object_name': 'ICBF'},
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poblacion_afro_escolar_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_afro_infantil_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_afro_madres_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_afro_otros_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_abandono_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_abandono_duracion': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_abandono_monto': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_discapacitada_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_discapacitada_duracion': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_discapacitada_monto': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_escolar_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_escolar_duracion': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_escolar_monto': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_infantil_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_infantil_duracion': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_infantil_monto': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_madres_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_madres_duracion': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_madres_monto': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_otro_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_otro_duracion': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_indigena_otro_monto': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_otro_escolar_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_otro_infantil_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_otro_madres_cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'poblacion_otro_otros_cobertura': ('django.db.models.fields.IntegerField', [], {})
        },
        'territorios.ingresodepartamental': {
            'Meta': {'object_name': 'IngresoDepartamental'},
            'credito_externo_amortizaciones': ('django.db.models.fields.IntegerField', [], {}),
            'credito_externo_desembolsos': ('django.db.models.fields.IntegerField', [], {}),
            'credito_interno_amortizaciones': ('django.db.models.fields.IntegerField', [], {}),
            'credito_interno_desembolsos': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_capital_formacion_bruta_capital_fijo': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_capital_inversion_social': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_capital_otros': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_capital_transferencias_capital': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_generales': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_servicios_personales': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_transferencias': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso_no_tributario_nivel_nacional': ('django.db.models.fields.IntegerField', [], {}),
            'ingreso_no_tributario_otras': ('django.db.models.fields.IntegerField', [], {}),
            'ingreso_tributario_cerveza': ('django.db.models.fields.IntegerField', [], {}),
            'ingreso_tributario_cigarillos_Tabaco': ('django.db.models.fields.IntegerField', [], {}),
            'ingreso_tributario_licores': ('django.db.models.fields.IntegerField', [], {}),
            'ingreso_tributario_otros': ('django.db.models.fields.IntegerField', [], {}),
            'ingreso_tributario_registro_anotacion': ('django.db.models.fields.IntegerField', [], {}),
            'ingreso_tributario_vehiculos_automotores': ('django.db.models.fields.IntegerField', [], {}),
            'ingresos_capital_cofinanciacion': ('django.db.models.fields.IntegerField', [], {}),
            'ingresos_capital_otros': ('django.db.models.fields.IntegerField', [], {}),
            'ingresos_capital_regalias': ('django.db.models.fields.IntegerField', [], {}),
            'intereses_deuda_externa': ('django.db.models.fields.IntegerField', [], {}),
            'intereses_deuda_interna': ('django.db.models.fields.IntegerField', [], {}),
            'transferencias_nivel_nacional': ('django.db.models.fields.IntegerField', [], {}),
            'transferencias_otras': ('django.db.models.fields.IntegerField', [], {}),
            'variacion_depositos_y_otros': ('django.db.models.fields.IntegerField', [], {})
        },
        'territorios.ingresomunicipal': {
            'Meta': {'object_name': 'IngresoMunicipal'},
            'amortizaciones': ('django.db.models.fields.IntegerField', [], {}),
            'cofinanciacion': ('django.db.models.fields.IntegerField', [], {}),
            'credito_externo': ('django.db.models.fields.IntegerField', [], {}),
            'credito_interno': ('django.db.models.fields.IntegerField', [], {}),
            'deficit_o_ahorro_corriente': ('django.db.models.fields.IntegerField', [], {}),
            'deficit_o_superavit_total': ('django.db.models.fields.IntegerField', [], {}),
            'del_nivel_nacional': ('django.db.models.fields.IntegerField', [], {}),
            'desembolsos': ('django.db.models.fields.IntegerField', [], {}),
            'formacion_brutal_capital_fijo': ('django.db.models.fields.IntegerField', [], {}),
            'gastos_generales': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industria_comercio': ('django.db.models.fields.IntegerField', [], {}),
            'intereses_deuda_publica': ('django.db.models.fields.IntegerField', [], {}),
            'otras_transferencias': ('django.db.models.fields.IntegerField', [], {}),
            'otros_gastos_corrientes': ('django.db.models.fields.IntegerField', [], {}),
            'otros_ingresos': ('django.db.models.fields.IntegerField', [], {}),
            'otros_ingresos_capital': ('django.db.models.fields.IntegerField', [], {}),
            'predial': ('django.db.models.fields.IntegerField', [], {}),
            'regalias': ('django.db.models.fields.IntegerField', [], {}),
            'resto_inversiones': ('django.db.models.fields.IntegerField', [], {}),
            'servicios_personales': ('django.db.models.fields.IntegerField', [], {}),
            'transferencias_nacionales': ('django.db.models.fields.IntegerField', [], {}),
            'transferencias_pagadas': ('django.db.models.fields.IntegerField', [], {})
        },
        'territorios.instalaciones': {
            'Meta': {'object_name': 'Instalaciones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_de_atencion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'territorios.institucioneducativa': {
            'Meta': {'object_name': 'InstitucionEducativa'},
            'educacion_adultos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'educacion_adultos_porcentaje': ('django.db.models.fields.IntegerField', [], {}),
            'educacion_especial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'educacion_especial_porcentaje': ('django.db.models.fields.IntegerField', [], {}),
            'enfasis': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'etnoeducacion_en_pei': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_constitucion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_nombrados_afro': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_nombrados_en_ejercicio': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_nombrados_indigenas': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_nombrados_otros': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_nombrados_total': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_temporales_afro': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_temporales_en_ejercicio': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_temporales_indigena': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_temporales_otros': ('django.db.models.fields.IntegerField', [], {}),
            'maestros_temporales_total': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'territorios.limitedepartamento': {
            'Meta': {'object_name': 'LimiteDepartamento'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'limites'", 'to': "orm['territorios.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'territorios.limitemunicipio': {
            'Meta': {'object_name': 'LimiteMunicipio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'limites'", 'to': "orm['territorios.Municipio']"}),
            'tipo': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'territorios.matriculas': {
            'Meta': {'object_name': 'Matriculas'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.mortalidadinfantil': {
            'Meta': {'object_name': 'MortalidadInfantil'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.mortalidadmaternoinfantil': {
            'Meta': {'object_name': 'MortalidadMaternoInfantil'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.mortalidadtotal': {
            'Meta': {'object_name': 'MortalidadTotal'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'cabecera_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cabecera_grupo_poblacional': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'cabecera_individuales_cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'expulsion_desplazados': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.ExpulsionDesplazados']"}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.IngresoMunicipal']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plan_desarrollo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PlanDesarrollo']"}),
            'plan_ordenamiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PlanOrdenamiento']"}),
            'poblacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PoblacionGrande']"}),
            'presupuesto_anual': ('django.db.models.fields.IntegerField', [], {}),
            'recepcion_desplazados': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.RecepcionDesplazados']"}),
            'rural_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rural_grupo_poblacional': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'rural_individuales_cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'territorios.plandesarrollo': {
            'Meta': {'object_name': 'PlanDesarrollo'},
            'existe_plan_desarrollo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'territorios.planordenamiento': {
            'Meta': {'object_name': 'PlanOrdenamiento'},
            'area_rutal_suelos_tipos': ('django.db.models.fields.TextField', [], {}),
            'cuencas_hidrograficas_area': ('django.db.models.fields.TextField', [], {}),
            'cuencas_hidrograficas_limite': ('django.db.models.fields.TextField', [], {}),
            'expansion_urbana_area': ('django.db.models.fields.TextField', [], {}),
            'expansion_urbana_limite': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapa_politico_administrativo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'mapa_uso_generales_del_suelo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'prod_agropecuaria_area': ('django.db.models.fields.TextField', [], {}),
            'prod_agropecuaria_limite': ('django.db.models.fields.TextField', [], {}),
            'riesgos_amenazas_descripcion': ('django.db.models.fields.TextField', [], {}),
            'riesgos_amenazas_ubicacion': ('django.db.models.fields.TextField', [], {}),
            'sistema_ambiental_area': ('django.db.models.fields.TextField', [], {}),
            'sistema_ambiental_limites': ('django.db.models.fields.TextField', [], {}),
            'sistema_forestal_area': ('django.db.models.fields.TextField', [], {}),
            'sistema_forestal_limites': ('django.db.models.fields.TextField', [], {}),
            'sistema_silvo_pastorial_area': ('django.db.models.fields.TextField', [], {}),
            'sistema_silvo_pastorial_limites': ('django.db.models.fields.TextField', [], {}),
            'suelo_urbano_area': ('django.db.models.fields.TextField', [], {}),
            'suelo_urbano_limite': ('django.db.models.fields.TextField', [], {}),
            'uso_cobertura_vegetal_area': ('django.db.models.fields.TextField', [], {}),
            'uso_cobertura_vegetal_tipo': ('django.db.models.fields.TextField', [], {}),
            'zonas_vida_area': ('django.db.models.fields.TextField', [], {}),
            'zonas_vida_limites': ('django.db.models.fields.TextField', [], {})
        },
        'territorios.poblacionestudiantilbasicaprimaria': {
            'Meta': {'object_name': 'PoblacionEstudiantilBasicaPrimaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.poblacionestudiantilbasicasecundaria': {
            'Meta': {'object_name': 'PoblacionEstudiantilBasicaSecundaria'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.poblacionestudiantilmediavocacional': {
            'Meta': {'object_name': 'PoblacionEstudiantilMediaVocacional'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.poblacionestudiantilpreescolar': {
            'Meta': {'object_name': 'PoblacionEstudiantilPreescolar'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'institucion_educativa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.InstitucionEducativa']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'territorios.poblaciongrande': {
            'Meta': {'object_name': 'PoblacionGrande'},
            'cantidad_afro': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_cabecera': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_no_informa': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_otros': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_rural': ('django.db.models.fields.IntegerField', [], {}),
            'edad_0_9': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_10_19': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_20_29': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_30_39': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_40_49': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_50_59': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_60_69': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_70_79': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_80_89': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porcentaje_hombres': ('django.db.models.fields.SmallIntegerField', [], {}),
            'porcentaje_indigena': ('django.db.models.fields.SmallIntegerField', [], {}),
            'total': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'territorios.poblacionpequena': {
            'Meta': {'object_name': 'PoblacionPequena'},
            'cantidad_hombres': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_mujeres': ('django.db.models.fields.SmallIntegerField', [], {}),
            'edad_0_5': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_11_15': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_16_20': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_21_25': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_26_30': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_31_35': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_36_40': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_41_45': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_46_50': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_51_55': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_56_60': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_61_65': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_66_70': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_6_10': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_71_75': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_76_80': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_81_85': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_86_90': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_91_95': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porcentaje_pueblos': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'territorios.promotores': {
            'Meta': {'object_name': 'Promotores'},
            'entidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.EntidadContratante']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_contrato': ('django.db.models.fields.IntegerField', [], {})
        },
        'territorios.pueblo': {
            'Meta': {'object_name': 'Pueblo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'territorios.recepciondesplazados': {
            'Meta': {'object_name': 'RecepcionDesplazados'},
            'cantidad_afro': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_cabecera': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_hombres': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_indigena': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_individual': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_mujeres': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_no_informa': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_otros': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_rural': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_total': ('django.db.models.fields.SmallIntegerField', [], {}),
            'edad_0_5': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_11_15': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_16_20': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_21_25': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_26_30': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_31_35': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_36_40': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_41_45': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_46_50': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_51_55': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_56_60': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_61_65': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_66_70': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_6_10': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_71_75': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_76_80': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_81_85': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_86_90': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'edad_91_95': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'territorios.regimen': {
            'Meta': {'object_name': 'Regimen'},
            'empresas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.EmpresaPrestadoraRegimenSubsidiario']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_poblacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'territorios.saneamiento': {
            'Meta': {'object_name': 'Saneamiento'},
            'ampliacion_estado_tramite': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'ampliacion_limites': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ampliacion_resolucion_codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ampliacion_resolucion_fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saneamiento_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'saneamiento_estado_tramite': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'saneamiento_limites': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'saneamiento_poblacion_afro': ('django.db.models.fields.IntegerField', [], {}),
            'saneamiento_poblacion_general': ('django.db.models.fields.IntegerField', [], {}),
            'saneamiento_poblacion_otros': ('django.db.models.fields.IntegerField', [], {}),
            'saneamiento_resolucion_codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'saneamiento_resolucion_fecha': ('django.db.models.fields.DateField', [], {})
        },
        'territorios.serviciopublico': {
            'Meta': {'object_name': 'ServicioPublico'},
            'cobertura_rural_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cobertura_rural_rango': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cobertura_urbana_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cobertura_urbana_rango': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servicios_publicos'", 'to': "orm['territorios.Desc']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'territorios.sistemasalud': {
            'Meta': {'object_name': 'SistemaSalud'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instalaciones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Instalaciones']", 'symmetrical': 'False'}),
            'promotores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Promotores']", 'symmetrical': 'False'}),
            'regimenes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Regimen']", 'symmetrical': 'False'})
        },
        'territorios.tasaanalfabetizacion': {
            'Meta': {'object_name': 'TasaAnalfabetizacion'},
            'afro': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'desc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Desc']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indigena': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rango': ('django.db.models.fields.CharField', [], {'default': "'0-0'", 'max_length': '50'}),
            'rural_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rural_rango': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'todos_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'todos_rango': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'urbano_porcentaje': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'urbano_rango': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'territorios.territorioindio': {
            'Meta': {'object_name': 'TerritorioIndio'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'asentamientos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Asentamiento']", 'symmetrical': 'False'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limites': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'municipios': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'indio_municipio'", 'symmetrical': 'False', 'to': "orm['territorios.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poblacion_total': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PoblacionPequena']"}),
            'pueblos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Pueblo']", 'symmetrical': 'False'}),
            'resolucion_constitucion': ('django.db.models.fields.IntegerField', [], {}),
            'situacion_juridica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Saneamiento']"})
        },
        'territorios.territorioindionotitulado': {
            'Meta': {'object_name': 'TerritorioIndioNoTitulado'},
            'area_solicitada': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'asentamientos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Asentamiento']", 'symmetrical': 'False'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipios': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'indio_not_municipio'", 'symmetrical': 'False', 'to': "orm['territorios.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poblacion_total': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PoblacionPequena']"}),
            'pueblos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Pueblo']", 'symmetrical': 'False'}),
            'situacion_juridica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Titulacion']"})
        },
        'territorios.territorionegro': {
            'Meta': {'object_name': 'TerritorioNegro'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'asentamientos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Asentamiento']", 'symmetrical': 'False'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limites': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'municipios': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'negro_municipio'", 'symmetrical': 'False', 'to': "orm['territorios.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poblacion_total': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PoblacionPequena']"}),
            'resolucion_constitucion': ('django.db.models.fields.IntegerField', [], {})
        },
        'territorios.territorionegronotitulado': {
            'Meta': {'object_name': 'TerritorioNegroNoTitulado'},
            'area_solicitada': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'asentamientos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Asentamiento']", 'symmetrical': 'False'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipios': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'negro_not_municipio'", 'symmetrical': 'False', 'to': "orm['territorios.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poblacion_total': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PoblacionPequena']"}),
            'situacion_juridica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Titulacion']"})
        },
        'territorios.titulacion': {
            'Meta': {'object_name': 'Titulacion'},
            'estado_tramite': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limites': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'resolucion_codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'resolucion_fecha': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['territorios']
