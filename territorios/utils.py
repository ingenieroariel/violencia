# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType

"""
Get content types ids from names of the lists, used to limit ubicacion choices
"""
def get_content_types_ids():
    types = ["departamento", "municipio", "Territorio Colectivo Comunidades Negras", "Territorio Colectivo Indígena"]
    items = []
    for t in types:
        try:
            content_type = ContentType.objects.get(name=t)
            items.append(content_type.id)
        except ContentType.DoesNotExist:
            pass
    return items

"""
Generates tuple
"""
def gen_rangos_cantidad():
    tupla = '('
    i = 0
    for c in range(5, 305, 5):
        tupla = tupla + "('%i-%i', '%i-%i')," % (i, c, i, c)
        i = c + 1
    tupla = tupla + ')'
    return eval(tupla)
