from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'entries.views.home'),
    url(r'^', include('entries.urls')),                       
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/password_reset/', 'django.contrib.auth.views.password_reset', {'template_name': 'registration/pw_reset_form.html', 'email_template_name':'registration/pw_reset_email.html'}),   
    url(r'^accounts/reset/done/', 'django.contrib.auth.views.password_reset_done', {'template_name': 'registration/pw_email_sent.html'}),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name' : 'registration/password_reset.html',  'post_reset_redirect': '/entries/'}, name='auth_password_reset_confirm' ),
)


urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
