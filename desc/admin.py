# -*- coding: utf-8 -*-
from desc.models import *
from django.contrib.gis import admin

class InstitucionEducativaInline(admin.StackedInline):
    model = InstitucionEducativa
    extra = 1

class PromotoresSaludInline(admin.StackedInline):
    model = PromotoresSalud
    extra = 1
  
class InstalacionesSaludInline(admin.StackedInline):
    model = InstalacionesSalud
    extra = 1

class ProgramaSeguridadAlimentariaInline(admin.StackedInline):
    model = ProgramaSeguridadAlimentaria
    extra = 1

class ProyectoEducativoInline(admin.StackedInline):
    model = ProyectoEducativo
    extra = 1

class EducacionAdmin(admin.ModelAdmin):
    inlines = (InstitucionEducativaInline,)
    list_display = ('municipio', 'total_instituciones')
    fieldsets = (
          ('Nivel Educativo', {
              'fields':
                 (
                 'content_type',
                 'object_id',

                 ('nivel_educativo_preescolar', 'nivel_educativo_primaria', 'nivel_educativo_secundaria'),
                 ('nivel_educativo_mediatec','nivel_educativo_normalista'),
                 'nivel_educativo_media_total',
                 ('nivel_educativo_sup_tecnica','nivel_educativo_sup_tecnologica','nivel_educativo_sup_profesional'),
                 'nivel_educativo_sup_total',
                  #'instituciones_total',
                  'fuente_nivel_educativo',
                 )

          }),
          ('Maestros vinculados', {
              'fields':
                 (
                 'maestros_vinculados_total',
                 ('maestros_vinculados_indigenas', 'maestros_vinculados_afro'),
                 ('maestros_vinculados_otros','maestros_vinculados_ejerciendo'),
                 )

          }),
          ('Maestros contratados', {
              'fields':
                 (
                 'maestros_contratados_total',
                 ('maestros_contratados_indigenas', 'maestros_contratados_afro'),
                 ('maestros_contratados_otros','maestros_contratados_ejerciendo'),
                 )

          }),
          (None, {
                'fields':
                    (
                    'fuente_maestros',
                    )
          }),
          ('Poblacion estudiantil', {
              'fields':
                 (
                 'total_poblacion_estudiantil',
                 ('cobertura_preescolar', 'cobertura_primaria'),
                 ('cobertura_secundaria','cobertura_mediavocacional'),
                 )

          }),
          ('Poblacion estudiantil (desplazados)', {
              'fields':
                 (
                 'total_poblacion_estudiantil_desplazada',
                 ('cobertura_preescolar_desplazados', 'cobertura_primaria_desplazados'),
                 ('cobertura_secundaria_desplazados','cobertura_mediavocacional_desplazados'),
                 )

          }),
          (None, {
              'fields':
                 (
                 ('desercion', 'promocion'),
                 ('repitencia','analfabetismo'),
                 )
          }),
          (None, {
                'fields':
                    (
                    'fuente_poblacion_estudiantil',
                    )
           }),
          
      )

class SistemaSaludAdmin(admin.ModelAdmin):
    inlines = (PromotoresSaludInline, InstalacionesSaludInline)
    list_display = ('municipio', 'entidades_contratantes', 'total_promotores_de_salud', 'contratos_temporales','contratos_fijos', 'puestos_de_salud', 'centros_de_salud', 'total_hospitales')
    fieldsets = (
          (None, {
              'fields':
                  (
                    'content_type',
                    'object_id',
                  )
          }),
          ('Régimen subsidiado carnetizado', {
              'fields':
                 (
                 ('reg_sub_carnetizado_indigena_porcentaje', 'reg_sub_carnetizado_indigena_empresas'),
                 ('reg_sub_carnetizado_afro_porcentaje','reg_sub_carnetizado_afro_empresas'),
                 ('reg_sub_carnetizado_otra_porcentaje','reg_sub_carnetizado_otra_empresas'),
                 )

          }),
          ('Régimen subsidiado vinculado', {
              'fields':
                 (
                 ('reg_sub_vinculado_indigena_porcentaje', 'reg_sub_vinculado_indigena_empresas'),
                 ('reg_sub_vinculado_afro_porcentaje','reg_sub_vinculado_afro_empresas'),
                 ('reg_sub_vinculado_otra_porcentaje','reg_sub_vinculado_otra_empresas'),
                 )

          }),
          ('Régimen contributivo', {
              'fields':
                 (
                 ('reg_contributivo_indigena_porcentaje', 'reg_contributivo_indigena_empresas'),
                 ('reg_contributivo_afro_porcentaje','reg_contributivo_afro_empresas'),
                 ('reg_contributivo_otra_porcentaje','reg_contributivo_otra_empresas'),
                 )

          }),
          (None, {'fields':('fuente_regimenes',)}),
      )

class DerechoPrimeraInfanciaAdmin(admin.ModelAdmin):
    inlines = (ProgramaSeguridadAlimentariaInline,)
    fieldsets = (
          (None, {
              'fields':
                  (
                    'content_type',
                    'object_id'
                  )
          }),
          ('Registro civil', {
              'fields':
                 (
                 ('registro_civil'),
                 ('registro_civil_indigena','registro_civil_afro', 'registro_civil_otros'),
                 'fuente_registro_civil',
                 )

          }),
         ('Vacunación', {
              'fields':
                 (
                 ('vacunacion_cobertura_indigena','vacunacion_cobertura_afro', 'vacunacion_cobertura_otros'),
                 'vacunacion_covertura_total',
                 'fuente_vacunacion',
                 )

          }),
          ('Programa Crecimiento y Desarrollo', {
              'fields':
                 (
                 ('pcd_cobertura_indigena','pcd_cobertura_afro', 'pcd_cobertura_otros'),
                 'pcd_cobertura_total',
                 'fuente_crecimiento_y_desarrollo',
                 )

          }),
          ('Afiliacion a salud', {
              'fields':
                 (
                 ('reg_sub_carnetizado_indigena','reg_sub_carnetizado_afro', 'reg_sub_carnetizado_otros'),
                 'reg_sub_carnetizado_total',
                 ('reg_contrib_vinculado_indigena','reg_contrib_vinculado_afro', 'reg_contrib_vinculado_otros'),
                 'reg_contrib_vinculado_total',
                 ('reg_contributivo_indigena','reg_contributivo_afro', 'reg_contributivo_otros'),
                 'reg_contributivo_total',
                 'fuente_afiliacion_salud',
                 )

          }),

      )

class DerechoAlTrabajoAdmin(admin.ModelAdmin):
    fieldsets = (
          (None, {
              'fields':
                  (
                    'content_type',
                    'object_id'
                  )
          }),
          (None, {
              'fields':
                  (
                    'desempleo',
                    'trabajo_informal',
                    'trabajo_formal',
                  )
          }),
         ('Empleo', {
              'fields':
                 (
                 ('empleo_formal_publico','empleo_formal_privado'),
                 ('empleo_formal_por_contrado_fijo','empleo_formal_por_contrado_temporal'),
                 )

          }),
          (None, {'fields':('fuente',)}),
      )

class DerechoCulturaAdmin(admin.ModelAdmin):
    inlines = (ProyectoEducativoInline, )
    fieldsets = (
          (None, {
              'fields':
                  (
                    'content_type',
                    'object_id'
                  )
          }),
          ('Programas de Protección y Promoción del patrimonio cultural', {
              'fields':
                 (
                 'pc_indigenas','pc_indigenas_descripcion',
                 'pc_afro','pc_afro_descripcion',
                 'fuente_pc',
                 )

          }),
          ('Programas de acceso a los medios de comunicacion', {
              'fields':
                 (
                 'pamc_indigenas','pamc_indigenas_descripcion',
                 'pamc_afro','pamc_afro_descripcion',
                 'fuente_pamc',
                 )

          }),
          ('Programas de protección y promoción de lenguas indígenas', {
              'fields':
                 (
                 'pl_indigenas','pl_indigenas_descripcion',
                 'fuente_pl',
                 )

          }),
          (None, {'fields':(
                ('existen_tr_indigenas_juzgado','total_tr_indigenas_juzgado'),
                ('existen_tr_indigenas_hospitales','total_tr_indigenas_hospitales'),
                'fuente_tr',
                )
           }),
      )
    

admin.site.register([IndicadorBasico, ])
admin.site.register(Educacion, EducacionAdmin)
admin.site.register(SistemaSalud, SistemaSaludAdmin)
admin.site.register(DerechoPrimeraInfancia, DerechoPrimeraInfanciaAdmin)
admin.site.register(DerechoAlTrabajo, DerechoAlTrabajoAdmin)
admin.site.register(DerechoCultura, DerechoCulturaAdmin)
