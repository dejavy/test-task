from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('root.views',
    url(r'^$', 'home', name='home'),
    url(r'^settings/$',  'settings'),
    url(r'^edit/$',  'edit'),
    url(r'^edit/password/$',  'password'),
    url(r'^accounts/login/$',  'login'),
    url(r'^accounts/logout/$', 'logout'),
    url(r'^registration/', 'registration', name='registration'),
    url(r'^admin/', include(admin.site.urls)),

)

#static & media data
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT}),

        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}),
    )