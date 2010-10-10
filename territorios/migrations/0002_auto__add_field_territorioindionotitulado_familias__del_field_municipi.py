# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'TerritorioIndioNoTitulado.familias'
        db.add_column('territorios_territorioindionotitulado', 'familias', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Municipio.cabecera_area'
        db.delete_column('territorios_municipio', 'cabecera_area')

        # Adding field 'Municipio.cabecera_area_total_titulos'
        db.add_column('territorios_municipio', 'cabecera_area_total_titulos', self.gf('django.db.models.fields.CharField')(default=None, max_length=255), keep_default=False)

        # Adding field 'Municipio.masivo'
        db.add_column('territorios_municipio', 'masivo', self.gf('django.db.models.fields.TextField')(default=None), keep_default=False)

        # Deleting field 'Economia.desempleo_formal'
        db.delete_column('territorios_economia', 'desempleo_formal')

        # Deleting field 'Economia.desempleo_informal'
        db.delete_column('territorios_economia', 'desempleo_informal')

        # Adding field 'Economia.desempleo'
        db.add_column('territorios_economia', 'desempleo', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)

        # Adding field 'Economia.trabajo_informal'
        db.add_column('territorios_economia', 'trabajo_informal', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)

        # Adding field 'Economia.trabajo_formal'
        db.add_column('territorios_economia', 'trabajo_formal', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)

        # Adding field 'TerritorioIndio.familias'
        db.add_column('territorios_territorioindio', 'familias', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Departamento.area_total'
        db.add_column('territorios_departamento', 'area_total', self.gf('django.db.models.fields.TextField')(default=None), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'TerritorioIndioNoTitulado.familias'
        db.delete_column('territorios_territorioindionotitulado', 'familias')

        # Adding field 'Municipio.cabecera_area'
        db.add_column('territorios_municipio', 'cabecera_area', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Deleting field 'Municipio.cabecera_area_total_titulos'
        db.delete_column('territorios_municipio', 'cabecera_area_total_titulos')

        # Deleting field 'Municipio.masivo'
        db.delete_column('territorios_municipio', 'masivo')

        # Adding field 'Economia.desempleo_formal'
        db.add_column('territorios_economia', 'desempleo_formal', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)

        # Adding field 'Economia.desempleo_informal'
        db.add_column('territorios_economia', 'desempleo_informal', self.gf('django.db.models.fields.IntegerField')(default=None), keep_default=False)

        # Deleting field 'Economia.desempleo'
        db.delete_column('territorios_economia', 'desempleo')

        # Deleting field 'Economia.trabajo_informal'
        db.delete_column('territorios_economia', 'trabajo_informal')

        # Deleting field 'Economia.trabajo_formal'
        db.delete_column('territorios_economia', 'trabajo_formal')

        # Deleting field 'TerritorioIndio.familias'
        db.delete_column('territorios_territorioindio', 'familias')

        # Deleting field 'Departamento.area_total'
        db.delete_column('territorios_departamento', 'area_total')


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
            'desempleo': ('django.db.models.fields.IntegerField', [], {}),
            'empleo_privado': ('django.db.models.fields.IntegerField', [], {}),
            'empleo_publico': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trabajo_formal': ('django.db.models.fields.IntegerField', [], {}),
            'trabajo_informal': ('django.db.models.fields.IntegerField', [], {})
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
            'cabecera_area_total_titulos': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'familias': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'familias': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
