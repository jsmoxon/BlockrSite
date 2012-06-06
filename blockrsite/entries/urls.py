from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
#    url(r'^home/', 'entries.views.home'),
#    url(r'^', 'entries.views.home'),
    url(r'^create_profile/', 'entries.views.create_profile'),
    url(r'^settings/', 'entries.views.administration'),
    url(r'^write/$', 'entries.views.write'),
    url(r'^write/nocommits', 'entries.views.no_commits'),
    url(r'^entries/', 'entries.views.list'),                       
    url(r'^flag/', 'entries.views.flag'),
    url(r'^(?P<entry_id>\d+)/', 'entries.views.view'),                       
    url(r'^google62e008c19d363d60.html/', direct_to_template, {'template': 'google2.html'}),
    url(r'^about/', direct_to_template, {'template': 'about.html'}),
    url(r'^github/', 'entries.views.check_github'),
    url(r'^preview/', 'entries.views.write_preview'),                       
)
