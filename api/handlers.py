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
