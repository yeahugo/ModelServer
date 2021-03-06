from django.conf.urls import patterns, include, url
from django.contrib import admin
#from mongonaut import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ModelServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^models/',include('toys.urls')),
    url(r'^models/.*$',include('toys.urls')),
    url(r'^api/',include('files.urls')),
    url(r'^catalog/',include('catalog.urls')),
#    url(r'mongonaut',include('mongonaut.urls'))
)
