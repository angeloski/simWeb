from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
from plots import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'plots.views.plots_home', name='plots_home'),
)
