# -*- coding: utf-8 -*-
from fuentes.models import FuenteDato
from territorios.models import Departamento, Municipio
from django.db import models

TIPO_COOPERACION = (
    ("internacional-bilateral","Internacional / Bilateral"),
    ("internacional-multilateral","Internacional / Multilateral"),
    ("internacional-ong","Internacional / ONG"),
    ("nacional-empresa-privada","Nacional / Empresa privada"),
    ("nacional-ong","Nacional / ONG"),
)

TIPO_PROYECTOS = (
    ("des-productivo","Desarrollo / Productivo"),
    ("des-genero","Desarrollo / Genero"),
    ("des-ninez","Desarrollo / Niñes"),
    ("des-educativo","Desarrollo / Educativo"),
    ("des-salud","Desarrollo / Salud"),
    ("des-otro","Desarrollo / Otro"),
    ("derechos-humanos","Derechos humanos"),
    ("ayuda-humanitaria","Ayuda humanitaria"),
    ("ambientales","Ambientales"),
)

OPERADORES = (
    ("publico","Público"),
    ("privado-ong","Privado / ONG"),
    ("privado-iglesias","Privado / Iglesias"),
    ("privado-org-sociales","Privado / Organizaciones sociales"),
    ("otros","Otros"),
)

class Cooperacion(models.Model):
    departamento = models.ForeignKey(Departamento, related_name='cooperaciones')

    cooperacion = models.CharField(max_length=200, choices=TIPO_COOPERACION)
    tipo_proyecto = models.CharField(max_length=200, choices=TIPO_PROYECTOS)
    periodo_convenio = models.CharField(max_length=200, null=True, blank=True)
    monto_inversion = models.IntegerField(help_text='millones de pesos')
    cobertura = models.ManyToManyField(Municipio)
    operadores = models.CharField(max_length=200, choices=OPERADORES)

    fuente = models.ForeignKey(FuenteDato, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cooperaciones'

    def __unicode__(self):
        return '%s: Cooperacion %s' % (self.departamento, self.cooperacion)