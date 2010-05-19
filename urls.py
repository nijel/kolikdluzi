from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'dluhy.views.index'),
    (r'^ministri/$', 'dluhy.views.ministri'),
    (r'^info/$', 'dluhy.views.info'),
    (r'^chart.js$', 'dluhy.views.chart'),
    (r'^ministri/(?P<slug>[^/]+)/$', 'dluhy.views.ministr'),
    (r'^strana/(?P<slug>[^/]+)/$', 'dluhy.views.strana'),

    # Example:
    # (r'^kolikdluzi/', include('kolikdluzi.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Static media for development
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media'}),
)
