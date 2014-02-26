from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from functools import wraps
from django.http import HttpResponse
from django.utils import simplejson as json
from coffin import shortcuts
from anyjson import serialize

import datetime

def render_to_string(template, context, request=None):
    if request:
        context_instance = RequestContext(request)
    else:
        context_instance = None

    return shortcuts.render_to_string(template, context, context_instance)

def render(request, template, context={}, mimetype='text/html'):
    response = render_to_string(template, context, request)

    return HttpResponse(response, mimetype=mimetype)

def json_response(response):
    return HttpResponse(serialize(response), mimetype='application/json')

def json_response_404(response):
    return HttpResponseNotFound(serialize(response), mimetype='application/json')

def to_dict(obj):
    fields = []
    for field in obj._meta.fields:
        fields.append(field.name)
    d = {}
    for attr in fields:
        if type(getattr(obj, attr)) == type(datetime.datetime.now()):
            d[attr] = getattr(obj, attr).strftime('%Y-%m-%d')
        else:
            d[attr] = getattr(obj, attr)
    return d