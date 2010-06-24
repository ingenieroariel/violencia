from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from violencia.api.handlers import RelatoHandler, FuenteHandler, VictimaHandler

auth = HttpBasicAuthentication(realm='My sample API')

relatos = Resource(handler=RelatoHandler, authentication=auth)
fuentes = Resource(handler=FuenteHandler, authentication=auth)
victimas = Resource(handler=VictimaHandler, authentication=auth)

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

    # automated documentation
    url(r'^$', documentation_view),
)
