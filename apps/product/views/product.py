# -*- coding:utf8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from annoying.decorators import render_to,ajax_request
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import simplejson as json 
import datetime

from contrib.shortcuts import json_response
from apps.product.models.product import Products
from apps.product.models.product import Product_Reviews

@render_to('product/list.html')
def index(request):
    return {}

@render_to('product/show.html')
def show(request,pid):
    return {}