from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('root.views',
    url(r'^$', 'home', name='home'),
#    url(r'^add_person/', 'add_person', name='add_person'),
#    url(r'^upload_file/', 'file_uploading', name='upload_file'),

#    (r'^admin/rosetta/', include('rosetta.urls')),
    (r'^admin/', include(admin.site.urls)),
)