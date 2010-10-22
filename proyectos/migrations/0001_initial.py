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
        'territorios.asentamiento': {
            'Meta': {'object_name': 'Asentamiento'},
            'decha_disolucion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        'territorios.territoriocomunidad': {
            'Meta': {'object_name': 'TerritorioComunidad'},
            'asentamientos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['territorios.Asentamiento']", 'symmetrical': 'False'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.Departamento']"}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poblacion_total': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['territorios.PoblacionPequena']"})
        }
    }

    complete_apps = ['proyectos']
