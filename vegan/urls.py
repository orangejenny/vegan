from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import vegan.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vegan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'.*', vegan.views.index),
    url(r'^admin/', include(admin.site.urls)),
)
