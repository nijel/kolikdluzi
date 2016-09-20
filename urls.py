from django.conf.urls import include, url
import django.views.static
from django.contrib.sitemaps import GenericSitemap, Sitemap
import django.contrib.sitemaps.views

from dluhy.models import Ministr
import dluhy.views

from django.conf import settings

import os
import datetime

from django.contrib import admin



admin.autodiscover()

ministr_dict = {
    'queryset': Ministr.objects.all(),
}

class PagesSitemap(Sitemap):
    changefreq = 'weekly'
    def items(self):
        return [
            ('/', '%s/index.html' % settings.HTML_ROOT, 1),
            ('/ministri/', '%s/top.html' % settings.HTML_ROOT, 1),
            ('/info/', '%s/info.html' % settings.HTML_ROOT, 0.5),
            ]
    def location(self, item):
        return item[0]

    def lastmod(self, item):
        if item[1] is None:
            return None
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(item[1])
        return datetime.datetime.fromtimestamp(mtime)

    def priority(self, item):
        return item[2]

sitemaps = {
    'ministri': GenericSitemap(ministr_dict, priority=0.8, changefreq='monthly'),
    'pages': PagesSitemap(),
}

urlpatterns = [
    url(r'^$', dluhy.views.index),
    url(r'^ministri/$', dluhy.views.ministri),
    url(r'^info/$', dluhy.views.info),
    url(r'^chart.js$', dluhy.views.chart),
    url(r'^ministri/(?P<slug>[^/]+)/$', dluhy.views.ministr),

    # Sitemap
    url(r'^sitemap.xml$', django.contrib.sitemaps.views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', django.contrib.sitemaps.views.sitemap, {'sitemaps': sitemaps}),

    # Example:
    # (r'^kolikdluzi/', include('kolikdluzi.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Static media for development
    url(r'^media/(?P<path>.*)$', django.views.static.serve,
        {'document_root': './media'}),
]
