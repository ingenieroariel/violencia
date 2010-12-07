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
    #list_filter = ('object_id', )
    fieldsets = (
          ('Nivel Educativo', {
              'fields':
                 (
                 'content_type',
                 'object_id',

                 ('nivel_educativo_preescolar', 'nivel_educativo_primaria', 'nivel_educativo_secundaria'),
                 ('nivel_educativo_mediatec','nivel_educativo_normalista'),
                 ('nivel_educativo_sup_tecnica','nivel_educativo_sup_tecnologica','nivel_educativo_sup_profesional'),
                  'instituciones_total',
                  'fuente_nivel_educativo',
                 )

          }),
      )

class SistemaSaludAdmin(admin.ModelAdmin):
    inlines = (PromotoresSaludInline, InstalacionesSaludInline)
    fieldsets = (
          (None, {
              'fields':
                  (
                    'content_type',
                    'object_id'
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
          ('Proteccion', {
              'fields':
                 (
                 ('registro_civil'),
                 ('registro_civil_indigena','registro_civil_afro', 'registro_civil_otros'),
                 )

          }),
         ('Salud', {
              'fields':
                 (
                 ('vacunacion_cobertura_indigena','vacunacion_cobertura_afro', 'vacunacion_cobertura_otros'),
                 )

          }),
          ('Programa Crecimiento y Desarrollo', {
              'fields':
                 (
                 ('pcd_cobertura_indigena','pcd_cobertura_afro', 'pcd_cobertura_otros'),
                 )

          }),
          ('Afiliacion a salud', {
              'fields':
                 (
                 ('reg_sub_carnetizado_indigena','reg_sub_carnetizado_afro', 'reg_sub_carnetizado_otros'),
                 ('reg_contrib_vinculado_indigena','reg_contrib_vinculado_afro', 'reg_contrib_vinculado_otros'),
                 ('reg_contributivo_indigena','reg_contributivo_afro', 'reg_contributivo_otros'),
                 )

          }),
          (None, {'fields':('fuente',)}),
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
          ('Desempleo', {
              'fields':
                 (
                 ('desempleo'),
                 )

          }),
         ('Empleo', {
              'fields':
                 (
                 ('empleo_informal'),
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
                 )

          }),
          ('Programas de acceso a los medios de comunicacion', {
              'fields':
                 (
                 'pamc_indigenas','pamc_indigenas_descripcion',
                 'pamc_afro','pamc_afro_descripcion',
                 )

          }),
          ('Programas de protección y promoción de lenguas indígenas', {
              'fields':
                 (
                 'pl_indigenas','pl_indigenas_descripcion',
                 ('existencia_tr_indigenas_juzgado','existencia_tr_indigenas_hospitales'),
                 )

          }),
          (None, {'fields':('fuente',)}),
      )
    

admin.site.register([IndicadorBasico, ])
admin.site.register(Educacion, EducacionAdmin)
admin.site.register(SistemaSalud, SistemaSaludAdmin)
admin.site.register(DerechoPrimeraInfancia, DerechoPrimeraInfanciaAdmin)
admin.site.register(DerechoAlTrabajo, DerechoAlTrabajoAdmin)
admin.site.register(DerechoCultura, DerechoCulturaAdmin)
