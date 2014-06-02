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

from django.shortcuts import redirect, render_to_response as rr
from django.template import RequestContext


def index(request):
    """
    index view of tehpug.ir
    """
    return rr("index.html", {},
              context_instance=RequestContext(request))


def contact(request):
    return rr("contact.html",
              context_instance=RequestContext(request))


# May be a bad idea but right now I don't know much about django views
def facebook(request):
    return redirect('https://facebook.com/tehpug', permanent=True)


def twitter(request):
    return redirect('https://twitter.com/TehPUG', permanent=True)


def github(request):
    return redirect('http://github.com/tehpug', permanent=True)


def trello(request):
    return redirect('https://trello.com/b/B4ZUJzZH/tehpug', permanent=True)


def list(request):
    return redirect('https://mail.python.org/mailman/listinfo/tehpug', permanent=True)


def youtube(request):
    return redirect('https://www.youtube.com/channel/UCvqrqROjFUFccIWh1cKQ8IA', permanent=True)


def irc(request):
    return redirect('http://webchat.freenode.net/?channels=python-ir&uio=d4', permanent=True)
