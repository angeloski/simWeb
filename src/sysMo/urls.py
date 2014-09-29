from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # Password URL workarounds for Django 1.6: 
    #   http://stackoverflow.com/questions/19985103/
    url(r'^password/change/$',
                    auth_views.password_change,
                    name='password_change'),
    url(r'^password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
    url(r'^password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
    url(r'^accounts/password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
    url(r'^password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),
    # ------------------------------------------------------
    url(r'^$', 'sysMo.views.home', name='home'),
    url(r'^profile/$', 'sysMo.views.profile', name='profile'),
    url(r'^about-us/$', 'sysMo.views.aboutus', name='aboutus'),
    url(r'^contact/$', 'sysMo.views.contact', name='contact'),
    url(r'^platform/', 'sysMo.views.platform', name='platform'),
    #url(r'^smoFluidProps/', include('smoFluidProps.urls', namespace='smoFluidProps')),
    #url(r'^dataManagement/', include('dataManagement.urls', namespace='dataManagement')),    
)
