from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from territorios.views import departamentos
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^departamentos.json$', departamentos),
    url(r'^world.json$', direct_to_template, {'template': 'world.json'}),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
                     (r'^site_media/(?P<path>.*)$', 
                     'django.views.static.serve',
                     {'document_root': settings.MEDIA_ROOT}))
