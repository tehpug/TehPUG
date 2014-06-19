# -----------------------------------------------------------------------------
#    karajlug.org
#    Copyright (C) 2010  karajlug community
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# -----------------------------------------------------------------------------

import os

from django.conf.urls import *
from django.contrib import admin
from django.conf import settings

from sitemap import sitemaps

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^admin/', include(admin.site.urls)),
    (r'^faq/$', "faq.views.index"),
    (r'^news/', include('news.urls')),
    (r'^page/', include('page.urls')),
    (r'^contact/$', 'tehpug.views.contact'),
    (r'^$', 'tehpug.views.index'),
    (r'^facebook/$', 'tehpug.views.facebook'),
    (r'^twitter/$', 'tehpug.views.twitter'),
    (r'^github/$', 'tehpug.views.github'),
    (r'^trello/$', 'tehpug.views.trello'),
    (r'^list/$', 'tehpug.views.list'),
    (r'^youtube/$', 'tehpug.views.youtube'),
    (r'^irc/$', 'tehpug.views.irc'),
)

# Local media serving.
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__),
         '../statics').replace('\\', '/')}),
    )
