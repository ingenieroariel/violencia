from django.contrib.contenttypes.models import ContentType
from piston.handler import AnonymousBaseHandler, BaseHandler
from fichas.models import Departamento, Municipio, Relato, Fuente, Victima, RelacionVictima, TipoViolencia, GrupoViolencia, ItemGrupoViolencia

ALL = ('GET', 'POST', 'PUT', 'DELETE')
 

class AnonymousRelatoHandler(AnonymousBaseHandler):
   allowed_methods = ('GET',)
   model = Relato

class AnonymousFuenteHandler(AnonymousBaseHandler):
   allowed_methods = ('GET',)
   model = Fuente

class AnonymousVictimaHandler(AnonymousBaseHandler):
   allowed_methods = ('GET',)
   model = Victima

class RelatoHandler(BaseHandler):
   anonymous = AnonymousRelatoHandler
   allowed_methods = ALL
   model = Relato

class FuenteHandler(BaseHandler):
   anonymous = AnonymousFuenteHandler
   allowed_methods = ALL
   model = Fuente

class VictimaHandler(BaseHandler):
   anonymous = AnonymousVictimaHandler
   allowed_methods = ALL
   model = Victima

class ContentTypeHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, model_name=None, id=None):
        base = ContentType.objects
        if model_name:
            try:
                return base.get(model=model_name)
            except ContentType.DoesNotExist:
                return {}
        elif id:
            ct = base.get(id=id)
            object = ct.model_class()
            list = []
            objects = object.objects.all()
            for o in objects:
                dict = {"id":o.id, "unicode":o.__unicode__()}
                list.append(dict)
            return list
        else:
            return base.all()

class TerritorioHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, content_type_id=None, territorio_id=None):
        base = ContentType.objects
        content_type = base.get(id=content_type_id)
        object = content_type.model_class().objects.get(id=territorio_id)
        return object.__unicode__()
