from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
#    url(r'^home/', 'entries.views.home'),
#    url(r'^', 'entries.views.home'),
    url(r'^create_profile/', 'entries.views.create_profile'),
    url(r'^settings/', 'entries.views.administration'),
    url(r'^write/', 'entries.views.write'),
    url(r'^entries/', 'entries.views.list'),                       
    url(r'^flag/', 'entries.views.flag'),
    url(r'^(?P<entry_id>\d+)/', 'entries.views.view'),                       
    url(r'^google/', direct_to_template, {'template': 'google.html'}),                        
)
