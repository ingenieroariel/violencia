from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from violencia.api.handlers import RelatoHandler, FuenteHandler, VictimaHandler, ContentTypeHandler, TerritorioHandler

auth = HttpBasicAuthentication(realm='My sample API')

relatos = Resource(handler=RelatoHandler, authentication=auth)
fuentes = Resource(handler=FuenteHandler, authentication=auth)
victimas = Resource(handler=VictimaHandler, authentication=auth)
content_types = Resource(handler=ContentTypeHandler)
territorios = Resource(handler=TerritorioHandler)

urlpatterns = patterns('',
    url(r'^relatos/$', relatos),
    url(r'^relatos/(?P<emitter_format>.+)/$', relatos),
    url(r'^relatos\.(?P<emitter_format>.+)', relatos, name='relatos'),

    url(r'^fuentes/$', fuentes),
    url(r'^fuentes/(?P<emitter_format>.+)/$', fuentes),
    url(r'^fuentes\.(?P<emitter_format>.+)', fuentes, name='fuentes'),

    url(r'^victimas/$', victimas),
    url(r'^victimas/(?P<emitter_format>.+)/$', victimas),
    url(r'^victimas\.(?P<emitter_format>.+)', victimas, name='victimas'),

    url(r'^content_types/$', content_types),
    url(r'^content_types/(?P<id>\d+)/$', content_types, name='contenttype_modelobjects_by_id'),
    url(r'^content_types/(?P<model_name>[^/]+)/$', content_types, name='contenttype_by_model_name'),
    url(r'^content_types\.(?P<emitter_format>.+)', content_types, name='content_types'),

    url(r'^territorios/(?P<content_type_id>\d+)/(?P<territorio_id>\d+)/$', territorios, name='territorios_resolver'),

    # automated documentation
    url(r'^$', documentation_view),
)
