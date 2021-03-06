# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'DerechoPrimeraInfancia.pcd_cobertura_total'
        db.alter_column('desc_derechoprimerainfancia', 'pcd_cobertura_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'DerechoPrimeraInfancia.reg_contributivo_total'
        db.alter_column('desc_derechoprimerainfancia', 'reg_contributivo_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'DerechoPrimeraInfancia.reg_contrib_vinculado_total'
        db.alter_column('desc_derechoprimerainfancia', 'reg_contrib_vinculado_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'DerechoPrimeraInfancia.reg_sub_carnetizado_total'
        db.alter_column('desc_derechoprimerainfancia', 'reg_sub_carnetizado_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'DerechoPrimeraInfancia.vacunacion_covertura_total'
        db.alter_column('desc_derechoprimerainfancia', 'vacunacion_covertura_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))


    def backwards(self, orm):
        
        # Changing field 'DerechoPrimeraInfancia.pcd_cobertura_total'
        db.alter_column('desc_derechoprimerainfancia', 'pcd_cobertura_total', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DerechoPrimeraInfancia.reg_contributivo_total'
        db.alter_column('desc_derechoprimerainfancia', 'reg_contributivo_total', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DerechoPrimeraInfancia.reg_contrib_vinculado_total'
        db.alter_column('desc_derechoprimerainfancia', 'reg_contrib_vinculado_total', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DerechoPrimeraInfancia.reg_sub_carnetizado_total'
        db.alter_column('desc_derechoprimerainfancia', 'reg_sub_carnetizado_total', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DerechoPrimeraInfancia.vacunacion_covertura_total'
        db.alter_column('desc_derechoprimerainfancia', 'vacunacion_covertura_total', self.gf('django.db.models.fields.IntegerField')(null=True))


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
        'desc.derechoaltrabajo': {
            'Meta': {'object_name': 'DerechoAlTrabajo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_4'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'desempleo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'empleo_formal_por_contrado_fijo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'empleo_formal_por_contrado_temporal': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'empleo_formal_privado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'empleo_formal_publico': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trabajo_formal': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'trabajo_informal': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        },
        'desc.derechocultura': {
            'Meta': {'object_name': 'DerechoCultura'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_5'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'existen_tr_indigenas_hospitales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'existen_tr_indigenas_juzgado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fuente_pamc': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuentes_pamc'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_pc': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuentes_pc'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_pl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuentes_pl'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_tr': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuentes_tl'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pamc_afro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pamc_afro_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pamc_indigenas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pamc_indigenas_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pc_afro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pc_afro_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pc_indigenas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pc_indigenas_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pl_indigenas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pl_indigenas_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'total_tr_indigenas_hospitales': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'total_tr_indigenas_juzgado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'desc.derechoprimerainfancia': {
            'Meta': {'object_name': 'DerechoPrimeraInfancia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_3'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'fuente_afiliacion_salud': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuentes_regimen'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_crecimiento_y_desarrollo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuentes_coberturas'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_registro_civil': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_registro_civil'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_vacunacion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_vacunacion'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pcd_cobertura_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'pcd_cobertura_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'pcd_cobertura_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'pcd_cobertura_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contrib_vinculado_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contrib_vinculado_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contrib_vinculado_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contrib_vinculado_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contributivo_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contributivo_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contributivo_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contributivo_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'registro_civil': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'registro_civil_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'registro_civil_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'registro_civil_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'vacunacion_cobertura_afro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'vacunacion_cobertura_indigena': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'vacunacion_cobertura_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'vacunacion_covertura_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        },
        'desc.educacion': {
            'Meta': {'object_name': 'Educacion'},
            'analfabetismo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_mediavocacional': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_mediavocacional_desplazados': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_preescolar': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_preescolar_desplazados': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_primaria': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_primaria_desplazados': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_secundaria': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_secundaria_desplazados': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_1'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'desercion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'fuente_maestros': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_maestros'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_nivel_educativo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'niveles_educativos'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_poblacion_estudiantil': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_pobestudiantil'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_poblacion_estudiantil_desplazados': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_pobestudiantildes'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_poblacion_estudiantil_otros': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fuente_pobestudiantiliotro'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_contratados_afro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_contratados_ejerciendo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_contratados_indigenas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_contratados_otros': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_contratados_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_nombrados_afro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_nombrados_ejerciendo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_nombrados_indigenas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_nombrados_otros': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_nombrados_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_vinculados_afro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_vinculados_ejerciendo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_vinculados_indigenas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_vinculados_otros': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maestros_vinculados_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nivel_educativo_media_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_mediatec': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_normalista': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_preescolar': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_primaria': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_secundaria': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_sup_profesional': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_sup_tecnica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_sup_tecnologica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'nivel_educativo_sup_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'promocion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'repitencia': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'total_poblacion_estudiantil': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'total_poblacion_estudiantil_desplazada': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        },
        'desc.indicadorbasico': {
            'Meta': {'object_name': 'IndicadorBasico'},
            'alfabetizacion_rural': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'alfabetizacion_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'alfabetizacion_urbano': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_acueducto_rural': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_acueducto_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_acueducto_urbano': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_alcantarillado_rural': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_alcantarillado_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_alcantarillado_urbano': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_energia_rural': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_energia_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'cobertura_energia_urbano': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'esperanza_vida_hombres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'esperanza_vida_mujeres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'esperanza_vida_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'fuente_alfabetizacion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bbbbb'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_esperanza_vida': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bb'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_indice_condiciones_de_vida': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'condic'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_indice_desarrollo_humano': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'desa'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_ingreso_per_capita': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'per'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_matricula': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bbbbbb'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_morbilidad': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bbbb'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_mortalidad': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bbb'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_necesidades_basicas_insatisfechas': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'insat'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'fuente_servicios_publicos': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'servicios_publicos'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indice_condiciones_de_vida': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'indice_desarrollo_humano': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'ingresos_publicos_per_capita': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'matricula_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'morbilidad_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'morbilidad_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'morbimortalidad_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'morbimortalidad_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'mortalidad_infantil': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mortalidad_maternoinfantil': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mortalidad_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'necesidades_basicas_insatisfechas_rural': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'necesidades_basicas_insatisfechas_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'necesidades_basicas_insatisfechas_urbano': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'desc.instalacionessalud': {
            'Meta': {'object_name': 'InstalacionesSalud'},
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_de_atencion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sistema_salud': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instalaciones_salud'", 'to': "orm['desc.SistemaSalud']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'desc.institucioneducativa': {
            'Meta': {'object_name': 'InstitucionEducativa'},
            'adultos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'educa_adultos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enfasis': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'es_publica': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'etnoeducacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_constitucion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'instituciones'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador_educacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instituciones'", 'to': "orm['desc.Educacion']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tiene_pec': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tiene_pei': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'desc.programaseguridadalimentaria': {
            'Meta': {'object_name': 'ProgramaSeguridadAlimentaria'},
            'cobertura_afro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cobertura_indigena': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cobertura_otros': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cobertura_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'derecho': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'programas'", 'to': "orm['desc.DerechoPrimeraInfancia']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'desc.promotoressalud': {
            'Meta': {'object_name': 'PromotoresSalud'},
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'numero_contrato': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'promotores': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'sistema_salud': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promotores_salud'", 'to': "orm['desc.SistemaSalud']"}),
            'tipo_contrato': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'desc.proyectoeducativo': {
            'Meta': {'object_name': 'ProyectoEducativo'},
            'derecho': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyectos_educativos'", 'to': "orm['desc.DerechoCultura']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tiene': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'bi'", 'max_length': '100'})
        },
        'desc.sistemasalud': {
            'Meta': {'object_name': 'SistemaSalud'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'content_type_2'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'fuente_regimenes': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fregs'", 'null': 'True', 'to': "orm['fuentes.FuenteDato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reg_contributivo_afro_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_contributivo_afro_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contributivo_indigena_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_contributivo_indigena_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contributivo_otra_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_contributivo_otra_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_contributivo_total_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_afro_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_sub_carnetizado_afro_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_indigena_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_sub_carnetizado_indigena_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_otra_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_sub_carnetizado_otra_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_carnetizado_total_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_vinculado_afro_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_sub_vinculado_afro_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_vinculado_indigena_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_sub_vinculado_indigena_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_vinculado_otra_empresas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reg_sub_vinculado_otra_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reg_sub_vinculado_total_porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
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
        }
    }

    complete_apps = ['desc']
