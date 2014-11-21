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
from apps.account.models.auth_info import Info


@render_to('product/list.html')
def index(request):
    page = int(request.REQUEST.get('page',1))
    order = request.REQUEST.get('order','def')
    filter = request.REQUEST.get('filter','')
    days = int(request.REQUEST.get('days',0))
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
    
    days_filter = {}
    if days == 3:
        days_filter['date_count__gte'] = 1
        days_filter['date_count__lte'] = 3
    elif days == 7:
        days_filter['date_count__gt'] = 3
        days_filter['date_count__lte'] = 7
    elif days == 8:
        days_filter['date_count__gte'] = 8
    else:
        days_filter['date_count__gte'] = 1

    products = Products.objects.filter(status=2,tags__contains=filter,**days_filter).order_by(order_type)

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
    return {
        'products':products,
        'page':page,
        'order':order,
        'param':'&order='+order+'&filter='+filter+'&days='+str(days)
    }

@render_to('product/show.html')
def show(request,pid):
    product = Products.objects.get(id=pid)
    product.pics = product.pics.split('|')
    product.trips = json.loads(product.trips)
    reviews = Product_Reviews.objects.filter(product__id = pid)
    try:
        supplier = Info.objects.get(user = product.user)
        supplier.body = json.loads(supplier.body)
    except:
        pass
    return {'product':product,'reviews':reviews,'reviews_count':reviews.count(),'supplier':supplier}