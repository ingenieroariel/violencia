from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('violencia.api.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
                     (r'^site_media/(?P<path>.*)$', 
                     'django.views.static.serve',
                     {'document_root': settings.MEDIA_ROOT}))
