# -*- coding:utf8 -*-
import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from annoying.decorators import render_to,ajax_request

import simplejson as json 

from contrib.shortcuts import json_response

@render_to('index.html')
def index(request):
    return {}


@render_to('common/about/safe.html')
def about_safe(request):
    return {}