from django.db import models

"""
MODULO 1. LINEA BASE ORDENAMIENTO DEL TERRITORIO Y POBLACION

1.  Territorio Colectivo Indigena titulado
2.  Territorio Colectivo Indigena no titulado
3.  Territorio Colectivo Comunidades Negras titulado
4.  Territorio Colectivo Comunidades Negras no titulado
5.  Municipio
6.  Departamento

"""


# Create your models here.
class Territorio(models.Model):
    nombre = models.CharField(max_length=100)
    geom = models.TextField() #models.MultiPolygonField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return nombre

class TerritorioPolitico(Territorio):

    class Meta:
        abstract = True

class Departamento(TerritorioPolitico):
    pass

class Municipio(TerritorioPolitico):
    departamento = models.ForeignKey(Departamento)

class TerritorioComunidad(Territorio): 
    departamento = models.ForeignKey(Departamento)

    class Meta:
        abstract = True

class TerritorioIndio(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='indio_municipio')

class TerritorioIndioNoTitulado(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='indio_not_municipio')

class TerritorioNegro(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='negro_municipio')

class TerritorioNegroNoTitulado(TerritorioComunidad):
    municipios = models.ManyToManyField(Municipio, related_name='negro_not_municipio')
