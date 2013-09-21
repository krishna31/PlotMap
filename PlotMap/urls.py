from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'plotmap.views.home', name='home'),
    # url(r'^PlotMap/', include('PlotMap.foo.urls')),
     url(r'ajax', 'plotmap.views.getLocation', name='getLocation'),
     url(r'path/(\d+)/$', 'plotmap.views.getPath', name='getPath'),
     url(r'getAllPath', 'plotmap.views.getAllPath', name='getAllPath'),	
     url(r'^login/$',login),
     url(r'^logout/$',logout,{'template_name':'registration/logout.html'}),  
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^accounts/', include('registration.urls')),	

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
