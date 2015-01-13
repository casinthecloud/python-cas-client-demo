from django.conf.urls import patterns, include, url
from django.contrib import admin

import webapp.views

urlpatterns = patterns('',
    url(r'^$', webapp.views.index, name='index'),
    url(r'^index$', webapp.views.index, name='index'),
    url(r'^protected/index$', webapp.views.protected, name='protected'),
    url(r'^logout$', webapp.views.logout, name='logout'),
    url(r'^accounts/login/$', 'cas.views.login'),
    url(r'^accounts/logout/$', 'cas.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
)

