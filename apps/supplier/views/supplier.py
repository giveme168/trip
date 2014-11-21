# -*- coding:utf8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from annoying.decorators import render_to,ajax_request
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import simplejson as json 
import datetime

from contrib.shortcuts import json_response
from apps.product.models.product import Products
from apps.account.models.auth_info import Info

@render_to('supplier/index.html')
def index(request,sid):
    page = int(request.REQUEST.get('page',1))
    order = request.REQUEST.get('order','def')
    if order == 'pop':
        order_type = '-sales'
    elif order == 'sales':
        order_type = '-sales'
    elif order == 'honor':
        order_type = '-star'
    elif order == 'new':
        order_type = '-create_time'
    elif order == 'price':
        order_type = '-price_by_one'
    else:
        order_type = '-create_time'
    
    products = Products.objects.filter(status=2,user__id = sid).order_by(order_type)

    paginator = Paginator(products, 10)
    try:
        products = paginator.page(page)
    except Exception,e:
        products = paginator.page(paginator.num_pages)
    for product in products.object_list:
        product.tags = product.tags.replace('|',', ')
        pics = product.pics.split('|')
        product.pics = pics[0]
        product.pics_coutn = len(pics)

    try:
        supplier = Info.objects.get(user__id = sid)
        supplier.body = json.loads(supplier.body)
    except:
        pass

    return {
        'products':products,
        'page':page,
        'order':order,
        'supplier':supplier,
        'param':'&order='+order
    }

