# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ActividadProductiva'
        db.create_table('gestion_actividadproductiva', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('gestion', ['ActividadProductiva'])

        # Adding model 'Afectacion'
        db.create_table('gestion_afectacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_impacto_ambiental', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion_impacto_ambiental', self.gf('django.db.models.fields.TextField')()),
            ('tipo_impacto_cultural', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion_impacto_cultural', self.gf('django.db.models.fields.TextField')()),
            ('tipo_impacto_economico', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion_impacto_economico', self.gf('django.db.models.fields.TextField')()),
            ('tipo_impacto_social', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion_impacto_social', self.gf('django.db.models.fields.TextField')()),
            ('tipo_impacto_organizacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion_impacto_organizacion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('gestion', ['Afectacion'])

        # Adding model 'ModeloAdministracion'
        db.create_table('gestion_modeloadministracion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('externo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('compartido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('administrador', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('autonomo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('gestion', ['ModeloAdministracion'])

        # Adding model 'GestionRecursos'
        db.create_table('gestion_gestionrecursos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monto_total', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_cooperacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('entidades_cooperacion', self.gf('django.db.models.fields.TextField')()),
            ('monto_cooperacion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gestion', ['GestionRecursos'])

        # Adding model 'GestionEconomica'
        db.create_table('gestion_gestioneconomica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iniciativa_empresarial', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
            ('cobertura_poblacional', self.gf('django.db.models.fields.IntegerField')()),
            ('actividad_productiva', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.ActividadProductiva'])),
            ('gestion_recursos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.GestionRecursos'])),
            ('modelo_administracion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.ModeloAdministracion'])),
            ('afectacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.Afectacion'])),
        ))
        db.send_create_signal('gestion', ['GestionEconomica'])

        # Adding model 'PlanEtnodesarrollo'
        db.create_table('gestion_planetnodesarrollo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cobertura', self.gf('django.db.models.fields.TextField')()),
            ('sectores_que_aplican', self.gf('django.db.models.fields.TextField')()),
            ('evaluacion_implementacion', self.gf('django.db.models.fields.TextField')()),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('gestion', ['PlanEtnodesarrollo'])

        # Adding model 'ConsejoComunitarioMayor'
        db.create_table('gestion_consejocomunitariomayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('permanencia', self.gf('django.db.models.fields.IntegerField')()),
            ('asamblea', self.gf('django.db.models.fields.TextField')()),
            ('comites', self.gf('django.db.models.fields.TextField')()),
            ('junta_directiva', self.gf('django.db.models.fields.TextField')()),
            ('asociacion_consejo_comunitario', self.gf('django.db.models.fields.TextField')()),
            ('reglamento_interno_debil', self.gf('django.db.models.fields.TextField')()),
            ('reglamento_interno_fuerte', self.gf('django.db.models.fields.TextField')()),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('gestion', ['ConsejoComunitarioMayor'])

        # Adding model 'ConsejoComunitario'
        db.create_table('gestion_consejocomunitario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('permanencia', self.gf('django.db.models.fields.IntegerField')()),
            ('asamblea', self.gf('django.db.models.fields.TextField')()),
            ('comites', self.gf('django.db.models.fields.TextField')()),
            ('junta_directiva', self.gf('django.db.models.fields.TextField')()),
            ('asociacion_consejo_comunitario', self.gf('django.db.models.fields.TextField')()),
            ('consejo_comunitario_mayor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.ConsejoComunitarioMayor'])),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('gestion', ['ConsejoComunitario'])

        # Adding model 'CabildoMayor'
        db.create_table('gestion_cabildomayor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cantidad_resguardos', self.gf('django.db.models.fields.IntegerField')()),
            ('pertenece_asociacion_cabildos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombre_asiciacion_cabildos', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('gestion', ['CabildoMayor'])

        # Adding model 'CabildoLocal'
        db.create_table('gestion_cabildolocal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estructura_organizativa', self.gf('django.db.models.fields.TextField')()),
            ('autoridades_tradicionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo_autoridad', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cantidad_autoridades', self.gf('django.db.models.fields.IntegerField')()),
            ('agentes_salud_tradicional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo_agente_salud', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cantidad_agentes_salud', self.gf('django.db.models.fields.IntegerField')()),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidadIndigena'])),
            ('cabildo_mayor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.CabildoMayor'])),
        ))
        db.send_create_signal('gestion', ['CabildoLocal'])

        # Adding model 'PlanVida'
        db.create_table('gestion_planvida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cobertura', self.gf('django.db.models.fields.TextField')()),
            ('sectores_que_aplican', self.gf('django.db.models.fields.TextField')()),
            ('ordenamiento_territorial_area', self.gf('django.db.models.fields.IntegerField')()),
            ('ordenamiento_territorial_descripcion', self.gf('django.db.models.fields.TextField')()),
            ('evaluacion_implementacion', self.gf('django.db.models.fields.TextField')()),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('gestion', ['PlanVida'])

        # Adding model 'JurisdiccionEspecialIndigena'
        db.create_table('gestion_jurisdiccionespecialindigena', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reglamento_justicia_indigena', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo_nivel_aplicacion', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('descripcion_nivel_aplicacion', self.gf('django.db.models.fields.TextField')()),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('gestion', ['JurisdiccionEspecialIndigena'])

        # Adding model 'TransferenciasPresupuestales'
        db.create_table('gestion_transferenciaspresupuestales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plan_inversion_anual', self.gf('django.db.models.fields.IntegerField')()),
            ('monto_educacion', self.gf('django.db.models.fields.IntegerField')()),
            ('monto_salud', self.gf('django.db.models.fields.IntegerField')()),
            ('monto_saneamieno', self.gf('django.db.models.fields.IntegerField')()),
            ('monto_produccion', self.gf('django.db.models.fields.IntegerField')()),
            ('monto_otros', self.gf('django.db.models.fields.IntegerField')()),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('gestion', ['TransferenciasPresupuestales'])

        # Adding model 'AccionesExigibilidadDerechos'
        db.create_table('gestion_accionesexigibilidadderechos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movilizacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_movilizacion', self.gf('django.db.models.fields.DateField')()),
            ('lugar_movilizacion', self.gf('django.db.models.fields.TextField')()),
            ('causa_movilizacion', self.gf('django.db.models.fields.TextField')()),
            ('participantes_movilizacion', self.gf('django.db.models.fields.IntegerField')()),
            ('instancia_movilizacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion_movilizacion', self.gf('django.db.models.fields.TextField')()),
            ('resultado_movilizacion', self.gf('django.db.models.fields.TextField')()),
            ('accion_juridica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_accion_juridica', self.gf('django.db.models.fields.DateField')()),
            ('lugar_accion_juridica', self.gf('django.db.models.fields.TextField')()),
            ('causa_accion_juridica', self.gf('django.db.models.fields.TextField')()),
            ('participantes_accion_juridica', self.gf('django.db.models.fields.TextField')()),
            ('instancia_accion_juridica', self.gf('django.db.models.fields.TextField')()),
            ('descripcion_accion_juridica', self.gf('django.db.models.fields.TextField')()),
            ('resultado_accion_juridica', self.gf('django.db.models.fields.TextField')()),
            ('estrategia_comunicacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_estrategia_comunicacion', self.gf('django.db.models.fields.DateField')()),
            ('lugar_estrategia_comunicacion', self.gf('django.db.models.fields.TextField')()),
            ('causa_estrategia_comunicacion', self.gf('django.db.models.fields.TextField')()),
            ('participantes_estrategia_comunicacion', self.gf('django.db.models.fields.IntegerField')()),
            ('instancia_estrategia_comunicacion', self.gf('django.db.models.fields.TextField')()),
            ('descripcion_estrategia_comunicacion', self.gf('django.db.models.fields.TextField')()),
            ('resultado_estrategia_comunicacion', self.gf('django.db.models.fields.TextField')()),
            ('otro', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_otro', self.gf('django.db.models.fields.DateField')()),
            ('causa_otro', self.gf('django.db.models.fields.TextField')()),
            ('descripcion_otro', self.gf('django.db.models.fields.TextField')()),
            ('resultado_otro', self.gf('django.db.models.fields.TextField')()),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
        ))
        db.send_create_signal('gestion', ['AccionesExigibilidadDerechos'])


    def backwards(self, orm):
        
        # Deleting model 'ActividadProductiva'
        db.delete_table('gestion_actividadproductiva')

        # Deleting model 'Afectacion'
        db.delete_table('gestion_afectacion')

        # Deleting model 'ModeloAdministracion'
        db.delete_table('gestion_modeloadministracion')

        # Deleting model 'GestionRecursos'
        db.delete_table('gestion_gestionrecursos')

        # Deleting model 'GestionEconomica'
        db.delete_table('gestion_gestioneconomica')

        # Deleting model 'PlanEtnodesarrollo'
        db.delete_table('gestion_planetnodesarrollo')

        # Deleting model 'ConsejoComunitarioMayor'
        db.delete_table('gestion_consejocomunitariomayor')

        # Deleting model 'ConsejoComunitario'
        db.delete_table('gestion_consejocomunitario')

        # Deleting model 'CabildoMayor'
        db.delete_table('gestion_cabildomayor')

        # Deleting model 'CabildoLocal'
        db.delete_table('gestion_cabildolocal')

        # Deleting model 'PlanVida'
        db.delete_table('gestion_planvida')

        # Deleting model 'JurisdiccionEspecialIndigena'
        db.delete_table('gestion_jurisdiccionespecialindigena')

        # Deleting model 'TransferenciasPresupuestales'
        db.delete_table('gestion_transferenciaspresupuestales')

        # Deleting model 'AccionesExigibilidadDerechos'
        db.delete_table('gestion_accionesexigibilidadderechos')


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
        'gestion.accionesexigibilidadderechos': {
            'Meta': {'object_name': 'AccionesExigibilidadDerechos'},
            'accion_juridica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'causa_accion_juridica': ('django.db.models.fields.TextField', [], {}),
            'causa_estrategia_comunicacion': ('django.db.models.fields.TextField', [], {}),
            'causa_movilizacion': ('django.db.models.fields.TextField', [], {}),
            'causa_otro': ('django.db.models.fields.TextField', [], {}),
            'descripcion_accion_juridica': ('django.db.models.fields.TextField', [], {}),
            'descripcion_estrategia_comunicacion': ('django.db.models.fields.TextField', [], {}),
            'descripcion_movilizacion': ('django.db.models.fields.TextField', [], {}),
            'descripcion_otro': ('django.db.models.fields.TextField', [], {}),
            'estrategia_comunicacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_accion_juridica': ('django.db.models.fields.DateField', [], {}),
            'fecha_estrategia_comunicacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_movilizacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_otro': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instancia_accion_juridica': ('django.db.models.fields.TextField', [], {}),
            'instancia_estrategia_comunicacion': ('django.db.models.fields.TextField', [], {}),
            'instancia_movilizacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lugar_accion_juridica': ('django.db.models.fields.TextField', [], {}),
            'lugar_estrategia_comunicacion': ('django.db.models.fields.TextField', [], {}),
            'lugar_movilizacion': ('django.db.models.fields.TextField', [], {}),
            'movilizacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'otro': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'participantes_accion_juridica': ('django.db.models.fields.TextField', [], {}),
            'participantes_estrategia_comunicacion': ('django.db.models.fields.IntegerField', [], {}),
            'participantes_movilizacion': ('django.db.models.fields.IntegerField', [], {}),
            'resultado_accion_juridica': ('django.db.models.fields.TextField', [], {}),
            'resultado_estrategia_comunicacion': ('django.db.models.fields.TextField', [], {}),
            'resultado_movilizacion': ('django.db.models.fields.TextField', [], {}),
            'resultado_otro': ('django.db.models.fields.TextField', [], {}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'gestion.actividadproductiva': {
            'Meta': {'object_name': 'ActividadProductiva'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gestion.afectacion': {
            'Meta': {'object_name': 'Afectacion'},
            'descripcion_impacto_ambiental': ('django.db.models.fields.TextField', [], {}),
            'descripcion_impacto_cultural': ('django.db.models.fields.TextField', [], {}),
            'descripcion_impacto_economico': ('django.db.models.fields.TextField', [], {}),
            'descripcion_impacto_organizacion': ('django.db.models.fields.TextField', [], {}),
            'descripcion_impacto_social': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_impacto_ambiental': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_impacto_cultural': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_impacto_economico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_impacto_organizacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_impacto_social': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gestion.cabildolocal': {
            'Meta': {'object_name': 'CabildoLocal'},
            'agentes_salud_tradicional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autoridades_tradicionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cabildo_mayor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gestion.CabildoMayor']"}),
            'cantidad_agentes_salud': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_autoridades': ('django.db.models.fields.IntegerField', [], {}),
            'estructura_organizativa': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidadIndigena']"}),
            'tipo_agente_salud': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_autoridad': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'gestion.cabildomayor': {
            'Meta': {'object_name': 'CabildoMayor'},
            'cantidad_resguardos': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre_asiciacion_cabildos': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pertenece_asociacion_cabildos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'territorios': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.TerritorioComunidadIndigena']", 'through': "orm['gestion.CabildoLocal']", 'symmetrical': 'False'})
        },
        'gestion.consejocomunitario': {
            'Meta': {'object_name': 'ConsejoComunitario'},
            'asamblea': ('django.db.models.fields.TextField', [], {}),
            'asociacion_consejo_comunitario': ('django.db.models.fields.TextField', [], {}),
            'comites': ('django.db.models.fields.TextField', [], {}),
            'consejo_comunitario_mayor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gestion.ConsejoComunitarioMayor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'junta_directiva': ('django.db.models.fields.TextField', [], {}),
            'permanencia': ('django.db.models.fields.IntegerField', [], {}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'gestion.consejocomunitariomayor': {
            'Meta': {'object_name': 'ConsejoComunitarioMayor'},
            'asamblea': ('django.db.models.fields.TextField', [], {}),
            'asociacion_consejo_comunitario': ('django.db.models.fields.TextField', [], {}),
            'comites': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'junta_directiva': ('django.db.models.fields.TextField', [], {}),
            'permanencia': ('django.db.models.fields.IntegerField', [], {}),
            'reglamento_interno_debil': ('django.db.models.fields.TextField', [], {}),
            'reglamento_interno_fuerte': ('django.db.models.fields.TextField', [], {}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'gestion.gestioneconomica': {
            'Meta': {'object_name': 'GestionEconomica'},
            'actividad_productiva': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gestion.ActividadProductiva']"}),
            'afectacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gestion.Afectacion']"}),
            'cobertura_poblacional': ('django.db.models.fields.IntegerField', [], {}),
            'gestion_recursos': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gestion.GestionRecursos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iniciativa_empresarial': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modelo_administracion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gestion.ModeloAdministracion']"}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'gestion.gestionrecursos': {
            'Meta': {'object_name': 'GestionRecursos'},
            'entidades_cooperacion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto_cooperacion': ('django.db.models.fields.IntegerField', [], {}),
            'monto_total': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_cooperacion': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gestion.jurisdiccionespecialindigena': {
            'Meta': {'object_name': 'JurisdiccionEspecialIndigena'},
            'descripcion_nivel_aplicacion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reglamento_justicia_indigena': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"}),
            'tipo_nivel_aplicacion': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'gestion.modeloadministracion': {
            'Meta': {'object_name': 'ModeloAdministracion'},
            'administrador': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'autonomo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'compartido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'externo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'gestion.planetnodesarrollo': {
            'Meta': {'object_name': 'PlanEtnodesarrollo'},
            'cobertura': ('django.db.models.fields.TextField', [], {}),
            'evaluacion_implementacion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sectores_que_aplican': ('django.db.models.fields.TextField', [], {}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'gestion.planvida': {
            'Meta': {'object_name': 'PlanVida'},
            'cobertura': ('django.db.models.fields.TextField', [], {}),
            'evaluacion_implementacion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordenamiento_territorial_area': ('django.db.models.fields.IntegerField', [], {}),
            'ordenamiento_territorial_descripcion': ('django.db.models.fields.TextField', [], {}),
            'sectores_que_aplican': ('django.db.models.fields.TextField', [], {}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'gestion.transferenciaspresupuestales': {
            'Meta': {'object_name': 'TransferenciasPresupuestales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto_educacion': ('django.db.models.fields.IntegerField', [], {}),
            'monto_otros': ('django.db.models.fields.IntegerField', [], {}),
            'monto_produccion': ('django.db.models.fields.IntegerField', [], {}),
            'monto_salud': ('django.db.models.fields.IntegerField', [], {}),
            'monto_saneamieno': ('django.db.models.fields.IntegerField', [], {}),
            'plan_inversion_anual': ('django.db.models.fields.IntegerField', [], {}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
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
        },
        'territorios.territoriocomunidadindigena': {
            'Meta': {'object_name': 'TerritorioComunidadIndigena', '_ormbases': ['territorios.TerritorioComunidad']},
            'territoriocomunidad_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['territorios.TerritorioComunidad']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['gestion']
