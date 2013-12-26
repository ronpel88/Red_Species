from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redSpecies.views.home', name='home'),
    url(r'^(home|index)?/?$', include('index.urls', namespace="index"), name='home'),

     url(r'^accounts/login/$', 'django.contrib.auth.views.login',
         {'template_name': 'login.html'}, name='login'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),

    url(r'^admin/', include(admin.site.urls)),
)
