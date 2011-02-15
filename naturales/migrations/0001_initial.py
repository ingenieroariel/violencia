# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DesastreNatural'
        db.create_table('naturales_desastrenatural', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('descripcion_desastre', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('poblacion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('territorios_afectados', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('causas_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('afectacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('descripcion_afectacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('intervencion_fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('intervencion_clase', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('intervencion_institucion_organizacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('intervencion_tipo', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('naturales', ['DesastreNatural'])

        # Adding model 'AreaNaturalProtegida'
        db.create_table('naturales_areanaturalprotegida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_natural', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('resolucion_creacion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('traslape', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('descripcion_conflictos_uso', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('naturales', ['AreaNaturalProtegida'])

        # Adding M2M table for field municipios on 'AreaNaturalProtegida'
        db.create_table('naturales_areanaturalprotegida_municipios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('areanaturalprotegida', models.ForeignKey(orm['naturales.areanaturalprotegida'], null=False)),
            ('municipio', models.ForeignKey(orm['territorios.municipio'], null=False))
        ))
        db.create_unique('naturales_areanaturalprotegida_municipios', ['areanaturalprotegida_id', 'municipio_id'])

        # Adding model 'ParqueNacionalMAVDT'
        db.create_table('naturales_parquenacionalmavdt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_natural', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parques', to=orm['naturales.AreaNaturalProtegida'])),
            ('plan_de_manejo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('participantes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('participantes_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acuerdos_uso_manejo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('regimen_especial_manejo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('concesion_turistica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('concesion_turistica_entidad', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('concesion_turistica_representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('representante_opera_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('representante_opera_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('representante_actividades_economicas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('naturales', ['ParqueNacionalMAVDT'])

        # Adding model 'AfectacionAreaProtegida'
        db.create_table('naturales_afectacionareaprotegida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_natural', self.gf('django.db.models.fields.related.ForeignKey')(related_name='afectaciones', to=orm['naturales.AreaNaturalProtegida'])),
            ('afectacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('naturales', ['AfectacionAreaProtegida'])


    def backwards(self, orm):
        
        # Deleting model 'DesastreNatural'
        db.delete_table('naturales_desastrenatural')

        # Deleting model 'AreaNaturalProtegida'
        db.delete_table('naturales_areanaturalprotegida')

        # Removing M2M table for field municipios on 'AreaNaturalProtegida'
        db.delete_table('naturales_areanaturalprotegida_municipios')

        # Deleting model 'ParqueNacionalMAVDT'
        db.delete_table('naturales_parquenacionalmavdt')

        # Deleting model 'AfectacionAreaProtegida'
        db.delete_table('naturales_afectacionareaprotegida')


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
        'naturales.afectacionareaprotegida': {
            'Meta': {'object_name': 'AfectacionAreaProtegida'},
            'afectacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'area_natural': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'afectaciones'", 'to': "orm['naturales.AreaNaturalProtegida']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'naturales.areanaturalprotegida': {
            'Meta': {'object_name': 'AreaNaturalProtegida'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_natural': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'descripcion_conflictos_uso': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipios': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Municipio']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'resolucion_creacion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'traslape': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'naturales.desastrenatural': {
            'Meta': {'object_name': 'DesastreNatural'},
            'afectacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'causas_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_afectacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_desastre': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervencion_clase': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'intervencion_fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'intervencion_institucion_organizacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'intervencion_tipo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'poblacion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'territorios_afectados': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'naturales.parquenacionalmavdt': {
            'Meta': {'object_name': 'ParqueNacionalMAVDT'},
            'acuerdos_uso_manejo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'area_natural': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parques'", 'to': "orm['naturales.AreaNaturalProtegida']"}),
            'concesion_turistica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concesion_turistica_entidad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'concesion_turistica_representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'participantes_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plan_de_manejo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'regimen_especial_manejo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'representante_actividades_economicas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'representante_opera_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'representante_opera_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        }
    }

    complete_apps = ['naturales']
