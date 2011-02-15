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

    complete_apps = ['fichas']
