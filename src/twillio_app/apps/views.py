from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def twillio(request):
    return render_to_response('base.xml', {},
        mimetype="application/xml")
