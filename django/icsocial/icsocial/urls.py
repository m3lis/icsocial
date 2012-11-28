from django.conf.urls import patterns, include, url
from views import login,place,profile,index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login/', login),
	url(r'^at/(?P<nick>\w{1,50})/$', place),
	url(r'^hello/(?P<nick>\w{1,50})/$', profile),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	)
