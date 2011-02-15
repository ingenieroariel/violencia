# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Empresa'
        db.create_table('proyectos_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('representante_legal', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sede_principal', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('accionistas_nacionales', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('accionistas_extranjeros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('opera_en_colombia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('opera_en_extranjero', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('otras_actividades', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('proyectos', ['Empresa'])

        # Adding model 'InstitucionFinanciera'
        db.create_table('proyectos_institucionfinanciera', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('proyectos', ['InstitucionFinanciera'])

        # Adding model 'Financiacion'
        db.create_table('proyectos_financiacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monto', self.gf('django.db.models.fields.IntegerField')()),
            ('institucion_financiera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.InstitucionFinanciera'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Empresa'])),
        ))
        db.send_create_signal('proyectos', ['Financiacion'])

        # Adding model 'Proyecto'
        db.create_table('proyectos_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.Municipio'])),
            ('territorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorios.TerritorioComunidad'])),
            ('area_proyecto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('inicio', self.gf('django.db.models.fields.DateField')()),
            ('final', self.gf('django.db.models.fields.DateField')()),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Empresa'])),
            ('fecha_convocatoria', self.gf('django.db.models.fields.DateField')()),
            ('fecha_adjudicacion', self.gf('django.db.models.fields.DateField')()),
            ('subcontratista', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombre_subcontratista', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cesion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('nuevo_titular', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('suspension', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('motivo_suspension', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('revocatoria', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('motivo_revocatoria', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('requisitos_legales', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('proyectos', ['Proyecto'])

        # Adding model 'ConsultaPrevia'
        db.create_table('proyectos_consultaprevia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_acuerdo', self.gf('django.db.models.fields.DateField')()),
            ('suscriptores', self.gf('django.db.models.fields.TextField')()),
            ('acuerdos', self.gf('django.db.models.fields.TextField')()),
            ('metodologia', self.gf('django.db.models.fields.TextField')()),
            ('participacion', self.gf('django.db.models.fields.TextField')()),
            ('cumplimiento_acuerdos', self.gf('django.db.models.fields.TextField')()),
            ('conflictos', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('proyectos', ['ConsultaPrevia'])

        # Adding model 'LicenciaAmbiental'
        db.create_table('proyectos_licenciaambiental', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('impacto_ambiental', self.gf('django.db.models.fields.TextField')()),
            ('impacto_cultural', self.gf('django.db.models.fields.TextField')()),
            ('impacto_socioeconomico', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('proyectos', ['LicenciaAmbiental'])

        # Adding model 'PlanManejo'
        db.create_table('proyectos_planmanejo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('medidas_prevencion', self.gf('django.db.models.fields.TextField')()),
            ('medidas_mitigacion', self.gf('django.db.models.fields.TextField')()),
            ('medidas_correccion', self.gf('django.db.models.fields.TextField')()),
            ('medidas_compensacion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('proyectos', ['PlanManejo'])

        # Adding model 'RequisitoLegal'
        db.create_table('proyectos_requisitolegal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consulta_previa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.ConsultaPrevia'])),
            ('licencia_ambiental', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.LicenciaAmbiental'])),
            ('plan_manejo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.PlanManejo'])),
        ))
        db.send_create_signal('proyectos', ['RequisitoLegal'])

        # Adding model 'Empleo'
        db.create_table('proyectos_empleo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compromiso_consulta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empleo_local', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('salario_medio', self.gf('django.db.models.fields.IntegerField')()),
            ('empleo_otra_region', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_actividades', self.gf('django.db.models.fields.TextField')()),
            ('forma_pago', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('proyectos', ['Empleo'])

        # Adding model 'ProgramaSocial'
        db.create_table('proyectos_programasocial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compromiso_consulta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('educacion', self.gf('django.db.models.fields.TextField')()),
            ('educacion_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('infraestructura', self.gf('django.db.models.fields.TextField')()),
            ('infraestructura_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('salud', self.gf('django.db.models.fields.TextField')()),
            ('salud_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('produccion', self.gf('django.db.models.fields.TextField')()),
            ('produccion_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('otros', self.gf('django.db.models.fields.TextField')()),
            ('otros_monto', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('proyectos', ['ProgramaSocial'])

        # Adding model 'Subsidio'
        db.create_table('proyectos_subsidio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compromiso_consulta', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('individuales', self.gf('django.db.models.fields.TextField')()),
            ('individuales_monto', self.gf('django.db.models.fields.IntegerField')()),
            ('colectivos', self.gf('django.db.models.fields.TextField')()),
            ('colectivos_monto', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('proyectos', ['Subsidio'])

        # Adding model 'VinculaionPoblacion'
        db.create_table('proyectos_vinculaionpoblacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empleo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Empleo'])),
            ('programa_social', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.ProgramaSocial'])),
            ('subsidio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Subsidio'])),
        ))
        db.send_create_signal('proyectos', ['VinculaionPoblacion'])

        # Adding model 'Megaproyecto'
        db.create_table('proyectos_megaproyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Proyecto'])),
            ('tipo_proyecto', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('requisitos_legales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.RequisitoLegal'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('proyectos', ['Megaproyecto'])

        # Adding model 'DesarrolloLegislativo'
        db.create_table('proyectos_desarrollolegislativo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('megaproyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Megaproyecto'])),
            ('documento', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('decreto', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('resolucion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ordenanza', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('jurisprudencia', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('proyectos', ['DesarrolloLegislativo'])


    def backwards(self, orm):
        
        # Deleting model 'Empresa'
        db.delete_table('proyectos_empresa')

        # Deleting model 'InstitucionFinanciera'
        db.delete_table('proyectos_institucionfinanciera')

        # Deleting model 'Financiacion'
        db.delete_table('proyectos_financiacion')

        # Deleting model 'Proyecto'
        db.delete_table('proyectos_proyecto')

        # Deleting model 'ConsultaPrevia'
        db.delete_table('proyectos_consultaprevia')

        # Deleting model 'LicenciaAmbiental'
        db.delete_table('proyectos_licenciaambiental')

        # Deleting model 'PlanManejo'
        db.delete_table('proyectos_planmanejo')

        # Deleting model 'RequisitoLegal'
        db.delete_table('proyectos_requisitolegal')

        # Deleting model 'Empleo'
        db.delete_table('proyectos_empleo')

        # Deleting model 'ProgramaSocial'
        db.delete_table('proyectos_programasocial')

        # Deleting model 'Subsidio'
        db.delete_table('proyectos_subsidio')

        # Deleting model 'VinculaionPoblacion'
        db.delete_table('proyectos_vinculaionpoblacion')

        # Deleting model 'Megaproyecto'
        db.delete_table('proyectos_megaproyecto')

        # Deleting model 'DesarrolloLegislativo'
        db.delete_table('proyectos_desarrollolegislativo')


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
        'proyectos.consultaprevia': {
            'Meta': {'object_name': 'ConsultaPrevia'},
            'acuerdos': ('django.db.models.fields.TextField', [], {}),
            'conflictos': ('django.db.models.fields.TextField', [], {}),
            'cumplimiento_acuerdos': ('django.db.models.fields.TextField', [], {}),
            'fecha_acuerdo': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodologia': ('django.db.models.fields.TextField', [], {}),
            'participacion': ('django.db.models.fields.TextField', [], {}),
            'suscriptores': ('django.db.models.fields.TextField', [], {})
        },
        'proyectos.desarrollolegislativo': {
            'Meta': {'object_name': 'DesarrolloLegislativo'},
            'decreto': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'documento': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisprudencia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'megaproyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.Megaproyecto']"}),
            'ordenanza': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resolucion': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'proyectos.empleo': {
            'Meta': {'object_name': 'Empleo'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'compromiso_consulta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empleo_local': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'empleo_otra_region': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'forma_pago': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salario_medio': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_actividades': ('django.db.models.fields.TextField', [], {})
        },
        'proyectos.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'accionistas_extranjeros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'accionistas_nacionales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opera_en_colombia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'opera_en_extranjero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'otras_actividades': ('django.db.models.fields.TextField', [], {}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sede_principal': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'proyectos.financiacion': {
            'Meta': {'object_name': 'Financiacion'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.Empresa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion_financiera': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.InstitucionFinanciera']"}),
            'monto': ('django.db.models.fields.IntegerField', [], {})
        },
        'proyectos.institucionfinanciera': {
            'Meta': {'object_name': 'InstitucionFinanciera'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'proyectos.licenciaambiental': {
            'Meta': {'object_name': 'LicenciaAmbiental'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacto_ambiental': ('django.db.models.fields.TextField', [], {}),
            'impacto_cultural': ('django.db.models.fields.TextField', [], {}),
            'impacto_socioeconomico': ('django.db.models.fields.TextField', [], {})
        },
        'proyectos.megaproyecto': {
            'Meta': {'object_name': 'Megaproyecto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.Proyecto']"}),
            'requisitos_legales': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.RequisitoLegal']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'proyectos.planmanejo': {
            'Meta': {'object_name': 'PlanManejo'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medidas_compensacion': ('django.db.models.fields.TextField', [], {}),
            'medidas_correccion': ('django.db.models.fields.TextField', [], {}),
            'medidas_mitigacion': ('django.db.models.fields.TextField', [], {}),
            'medidas_prevencion': ('django.db.models.fields.TextField', [], {})
        },
        'proyectos.programasocial': {
            'Meta': {'object_name': 'ProgramaSocial'},
            'compromiso_consulta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'educacion': ('django.db.models.fields.TextField', [], {}),
            'educacion_monto': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.TextField', [], {}),
            'infraestructura_monto': ('django.db.models.fields.IntegerField', [], {}),
            'otros': ('django.db.models.fields.TextField', [], {}),
            'otros_monto': ('django.db.models.fields.IntegerField', [], {}),
            'produccion': ('django.db.models.fields.TextField', [], {}),
            'produccion_monto': ('django.db.models.fields.IntegerField', [], {}),
            'salud': ('django.db.models.fields.TextField', [], {}),
            'salud_monto': ('django.db.models.fields.IntegerField', [], {})
        },
        'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'area_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cesion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.Empresa']"}),
            'fecha_adjudicacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_convocatoria': ('django.db.models.fields.DateField', [], {}),
            'final': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {}),
            'motivo_revocatoria': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'motivo_suspension': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre_subcontratista': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nuevo_titular': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'requisitos_legales': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'revocatoria': ('django.db.models.fields.SmallIntegerField', [], {}),
            'subcontratista': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suspension': ('django.db.models.fields.SmallIntegerField', [], {}),
            'territorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.TerritorioComunidad']"})
        },
        'proyectos.requisitolegal': {
            'Meta': {'object_name': 'RequisitoLegal'},
            'consulta_previa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.ConsultaPrevia']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licencia_ambiental': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.LicenciaAmbiental']"}),
            'plan_manejo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.PlanManejo']"})
        },
        'proyectos.subsidio': {
            'Meta': {'object_name': 'Subsidio'},
            'colectivos': ('django.db.models.fields.TextField', [], {}),
            'colectivos_monto': ('django.db.models.fields.IntegerField', [], {}),
            'compromiso_consulta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individuales': ('django.db.models.fields.TextField', [], {}),
            'individuales_monto': ('django.db.models.fields.IntegerField', [], {})
        },
        'proyectos.vinculaionpoblacion': {
            'Meta': {'object_name': 'VinculaionPoblacion'},
            'empleo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.Empleo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programa_social': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.ProgramaSocial']"}),
            'subsidio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos.Subsidio']"})
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

    complete_apps = ['proyectos']
