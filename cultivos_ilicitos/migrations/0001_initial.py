# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CultivosIlicitos'
        db.create_table('cultivos_ilicitos_cultivosilicitos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Municipio'], null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('promotores', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('participacion_comunidad', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('participacion_comunidad_tipo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('participacion_otros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('participacion_otros_tipo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
        ))
        db.send_create_signal('cultivos_ilicitos', ['CultivosIlicitos'])

        # Adding model 'ErradicacionCultivosIlicitos'
        db.create_table('cultivos_ilicitos_erradicacioncultivosilicitos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos_ilicitos', self.gf('django.db.models.fields.related.ForeignKey')(related_name='erradicaciones', to=orm['cultivos_ilicitos.CultivosIlicitos'])),
            ('erradicacion_tipo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('referencia_cartografica', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('afectacion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('afectacion_nombre', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('impactos_salud_humana', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('impactos_salud_humana_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('impactos_ambientales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('impactos_ambientales_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('impactos_seguridad_alimentaria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('impactos_seguridad_alimentaria_descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('modalidad_ejecucion_directa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modalidad_ejecucion_contratada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modalidad_ejecucion_contratada_quienes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('consulta_previa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
        ))
        db.send_create_signal('cultivos_ilicitos', ['ErradicacionCultivosIlicitos'])

        # Adding M2M table for field territorios on 'ErradicacionCultivosIlicitos'
        db.create_table('cultivos_ilicitos_erradicacioncultivosilicitos_territorios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('erradicacioncultivosilicitos', models.ForeignKey(orm['cultivos_ilicitos.erradicacioncultivosilicitos'], null=False)),
            ('territoriocomunidad', models.ForeignKey(orm['territorios.territoriocomunidad'], null=False))
        ))
        db.create_unique('cultivos_ilicitos_erradicacioncultivosilicitos_territorios', ['erradicacioncultivosilicitos_id', 'territoriocomunidad_id'])

        # Adding model 'InversionSocialCultivosIlicitos'
        db.create_table('cultivos_ilicitos_inversionsocialcultivosilicitos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivos_ilicitos', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inversiones', to=orm['cultivos_ilicitos.CultivosIlicitos'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('catidad_familias', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('monto_por_municipio', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuentes.FuenteDato'], null=True, blank=True)),
        ))
        db.send_create_signal('cultivos_ilicitos', ['InversionSocialCultivosIlicitos'])


    def backwards(self, orm):
        
        # Deleting model 'CultivosIlicitos'
        db.delete_table('cultivos_ilicitos_cultivosilicitos')

        # Deleting model 'ErradicacionCultivosIlicitos'
        db.delete_table('cultivos_ilicitos_erradicacioncultivosilicitos')

        # Removing M2M table for field territorios on 'ErradicacionCultivosIlicitos'
        db.delete_table('cultivos_ilicitos_erradicacioncultivosilicitos_territorios')

        # Deleting model 'InversionSocialCultivosIlicitos'
        db.delete_table('cultivos_ilicitos_inversionsocialcultivosilicitos')


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
        'cultivos_ilicitos.cultivosilicitos': {
            'Meta': {'object_name': 'CultivosIlicitos'},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Municipio']", 'null': 'True', 'blank': 'True'}),
            'participacion_comunidad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'participacion_comunidad_tipo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'participacion_otros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'participacion_otros_tipo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promotores': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'cultivos_ilicitos.erradicacioncultivosilicitos': {
            'Meta': {'object_name': 'ErradicacionCultivosIlicitos'},
            'afectacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'afectacion_nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'consulta_previa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cultivos_ilicitos': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'erradicaciones'", 'to': "orm['cultivos_ilicitos.CultivosIlicitos']"}),
            'erradicacion_tipo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impactos_ambientales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'impactos_ambientales_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'impactos_salud_humana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'impactos_salud_humana_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'impactos_seguridad_alimentaria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'impactos_seguridad_alimentaria_descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modalidad_ejecucion_contratada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modalidad_ejecucion_contratada_quienes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modalidad_ejecucion_directa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referencia_cartografica': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'territorios': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.TerritorioComunidad']", 'symmetrical': 'False'})
        },
        'cultivos_ilicitos.inversionsocialcultivosilicitos': {
            'Meta': {'object_name': 'InversionSocialCultivosIlicitos'},
            'catidad_familias': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cultivos_ilicitos': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inversiones'", 'to': "orm['cultivos_ilicitos.CultivosIlicitos']"}),
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fuentes.FuenteDato']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto_por_municipio': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['cultivos_ilicitos']
