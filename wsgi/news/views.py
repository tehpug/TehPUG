# -----------------------------------------------------------------------------
#    Karajlug.org
#    Copyright (C) 2010  Karajlug community
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

from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
from django.utils import translation

from news.models import News


def news_entry(request, id_=None):
    """
    Show a single news entry.
    """
    if not id_:
        raise Http404()

    try:
        news_ent = News.objects.get(id=id_)

    except News.DoesNotExist:
        raise Http404()

    return rr('news_view.html',
              {'news': news_ent},
              context_instance=RequestContext(request))


def index(request):
    """
    show all the news with pagination.
    """
    return rr('news_list.html',
              context_instance=RequestContext(request))


def ajax(request):
    """
    load news with ajax
    """
    lang = translation.get_language()
    news = News.objects.filter(lang=lang).order_by('-date')

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        count = int(request.GET.get('count', '10'))
    except ValueError:
        count = 10

    if not 1 < count < 20:
        count = 10

    p = Paginator(news, count)

    try:
        return rr('ajax.html',
                  {'news_list': p.page(page)},
                  context_instance=RequestContext(request))
    except (EmptyPage, InvalidPage):
        return HttpResponse('')
