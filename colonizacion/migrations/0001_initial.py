# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Colonizacion'
        db.create_table('colonizacion_colonizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Municipio'], null=True, blank=True)),
            ('procedencia', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('cantidad_personas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('causa', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('actor', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('megaproyecto', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('colonizacion', ['Colonizacion'])

        # Adding model 'UsoTerritorio'
        db.create_table('colonizacion_usoterritorio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('colonizacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='usos_de_territorio', to=orm['colonizacion.Colonizacion'])),
            ('tipo_uso_area', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('colonizacion', ['UsoTerritorio'])


    def backwards(self, orm):
        
        # Deleting model 'Colonizacion'
        db.delete_table('colonizacion_colonizacion')

        # Deleting model 'UsoTerritorio'
        db.delete_table('colonizacion_usoterritorio')


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
        'colonizacion.colonizacion': {
            'Meta': {'object_name': 'Colonizacion'},
            'actor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cantidad_personas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'causa': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'megaproyecto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Municipio']", 'null': 'True', 'blank': 'True'}),
            'procedencia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'colonizacion.usoterritorio': {
            'Meta': {'object_name': 'UsoTerritorio'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'colonizacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usos_de_territorio'", 'to': "orm['colonizacion.Colonizacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_uso_area': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['colonizacion']
