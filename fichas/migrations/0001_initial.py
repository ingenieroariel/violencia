# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Relato'
        db.create_table('fichas_relato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Departamento'])),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Municipio'])),
            ('corregimiento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ins_deptal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ins_munic', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('caserio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('vereda', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sitio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('antecedentes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contexto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ocurrido_en', self.gf('django.db.models.fields.DateTimeField')()),
            ('duracion_hecho', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('fichas', ['Relato'])

        # Adding model 'Fuente'
        db.create_table('fichas_fuente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relato', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fuentes', null=True, to=orm['fichas.Relato'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='d', max_length=1)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(default='Fuente directa', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('fichas', ['Fuente'])

        # Adding model 'TipoViolencia'
        db.create_table('fichas_tipoviolencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('fichas', ['TipoViolencia'])

        # Adding model 'GrupoViolencia'
        db.create_table('fichas_grupoviolencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='grupos', to=orm['fichas.TipoViolencia'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('fichas', ['GrupoViolencia'])

        # Adding model 'ItemGrupoViolencia'
        db.create_table('fichas_itemgrupoviolencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='grupo_items', to=orm['fichas.GrupoViolencia'])),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre_tipo', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('fichas', ['ItemGrupoViolencia'])

        # Adding model 'Victima'
        db.create_table('fichas_victima', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relato', self.gf('django.db.models.fields.related.ForeignKey')(related_name='victimas', to=orm['fichas.Relato'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('por_cantidad', self.gf('django.db.models.fields.CharField')(default='i', max_length=1)),
        ))
        db.send_create_signal('fichas', ['Victima'])

        # Adding model 'RelacionVictima'
        db.create_table('fichas_relacionvictima', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('victima', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipos_violencia', to=orm['fichas.Victima'])),
            ('tipo_violencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fichas.ItemGrupoViolencia'])),
        ))
        db.send_create_signal('fichas', ['RelacionVictima'])


    def backwards(self, orm):
        
        # Deleting model 'Relato'
        db.delete_table('fichas_relato')

        # Deleting model 'Fuente'
        db.delete_table('fichas_fuente')

        # Deleting model 'TipoViolencia'
        db.delete_table('fichas_tipoviolencia')

        # Deleting model 'GrupoViolencia'
        db.delete_table('fichas_grupoviolencia')

        # Deleting model 'ItemGrupoViolencia'
        db.delete_table('fichas_itemgrupoviolencia')

        # Deleting model 'Victima'
        db.delete_table('fichas_victima')

        # Deleting model 'RelacionVictima'
        db.delete_table('fichas_relacionvictima')


    models = {
        'fichas.fuente': {
            'Meta': {'object_name': 'Fuente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'relato': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuentes'", 'null': 'True', 'to': "orm['fichas.Relato']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'default': "'Fuente directa'", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'fichas.grupoviolencia': {
            'Meta': {'object_name': 'GrupoViolencia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grupos'", 'to': "orm['fichas.TipoViolencia']"})
        },
        'fichas.itemgrupoviolencia': {
            'Meta': {'object_name': 'ItemGrupoViolencia'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grupo_items'", 'to': "orm['fichas.GrupoViolencia']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tipo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'fichas.relacionvictima': {
            'Meta': {'object_name': 'RelacionVictima'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_violencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fichas.ItemGrupoViolencia']"}),
            'victima': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipos_violencia'", 'to': "orm['fichas.Victima']"})
        },
        'fichas.relato': {
            'Meta': {'object_name': 'Relato'},
            'antecedentes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'caserio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contexto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'corregimiento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'duracion_hecho': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ins_deptal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ins_munic': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Municipio']"}),
            'ocurrido_en': ('django.db.models.fields.DateTimeField', [], {}),
            'sitio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vereda': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'fichas.tipoviolencia': {
            'Meta': {'object_name': 'TipoViolencia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'fichas.victima': {
            'Meta': {'object_name': 'Victima'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'por_cantidad': ('django.db.models.fields.CharField', [], {'default': "'i'", 'max_length': '1'}),
            'relato': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'victimas'", 'to': "orm['fichas.Relato']"}),
            'tipo_violencia': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fichas.ItemGrupoViolencia']", 'through': "orm['fichas.RelacionVictima']", 'symmetrical': 'False'})
        },
        'territorios.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'area_total': ('django.db.models.fields.TextField', [], {}),
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
        'territorios.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'cabecera_area_total_titulos': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255'}),
            'cabecera_grupo_poblacional': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'cabecera_individuales_cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'expulsion_desplazados': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.ExpulsionDesplazados']"}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.IngresoMunicipal']"}),
            'masivo': ('django.db.models.fields.TextField', [], {}),
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
        }
    }

    complete_apps = ['fichas']
