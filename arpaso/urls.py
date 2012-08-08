from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('root.views',
    url(r'^$', 'home', name='home'),
    url(r'^accounts/login/$',  'login'),
    url(r'^accounts/logout/$', 'logout'),
    url(r'^registration/', 'registration', name='registration'),
    
    url(r'^admin/', include(admin.site.urls)),

)