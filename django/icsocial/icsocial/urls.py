from django.conf.urls import patterns, include, url
from views import login,place,profile,index,logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login/', login),
    url(r'^logout/', logout),


    url(r'^places/', index),

    url(r'^tours/', index),
    url(r'^tours/my/', index),

    url(r'^at/(?P<nick>\w{1,50})/$', place),
    url(r'^hello/(?P<nick>\w{1,50})/$', profile),

    url(r'^about/us/', index),
    url(r'^about/icsocial/', index),
    url(r'^about/tech/', index),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),    
  	)
