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


@render_to('ink/product/index.html')
def rend_data(request):
    product = Products()
    product.name = u'海南七日游' 
    product.price = 1
    product.price_type = 1
    product.total_price = 1
    product.order_time = datetime.datetime.strptime('2014-03-31','%Y-%m-%d')
    product.trip_start_time = datetime.datetime.strptime('2014-06-15','%Y-%m-%d')
    product.trip_end_time = datetime.datetime.strptime('2014-09-15','%Y-%m-%d')
    product.key_desc = u'海南七日游'
    product.start_city = u'北京'
    product.end_city = u'海南'
    product.pics = ''
    product.trips = '游艇'
    product.date_count = len(json.loads(json.dumps([{'name':u'第一天'},{'name':u'第二天'}])))
    product.user = request.user
    try:
        product.save()
        return HttpResponseRedirect('/ink/product/index')
    except:
        return {}
    return {}

@render_to('ink/product/index.html')
def index(request):
    name = request.REQUEST.get('name','')
    page = int(request.REQUEST.get('page',1))
    if name:
        products = Products.objects.filter(name__contains = name,status=2, user=request.user)
    else:
        products = Products.objects.filter(status=2, user=request.user)

    paginator=Paginator(products,10)
    page_count= paginator.count
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return {'page_count':page_count,'products':products}

@render_to('ink/product/create.html')
def create(request):
    if request.method=='POST':
        name = request.REQUEST.get('name','')
        price = float(request.REQUEST.get('price',1))
        price_type = float(request.REQUEST.get('price_type',1))
        order_time = request.REQUEST.get('order_time',datetime.datetime.now().strftime('%Y-%m-%d'))
        trip_start_time = request.REQUEST.get('trip_start_time',datetime.datetime.now().strftime('%Y-%m-%d'))
        trip_end_time = request.REQUEST.get('trip_end_time',datetime.datetime.now().strftime('%Y-%m-%d'))
        key_desc = request.REQUEST.get('key_desc','')
        start_city = request.REQUEST.get('start_city','')
        end_city = request.REQUEST.get('end_city','')
        pics = request.REQUEST.get('pics','')
        trips = request.REQUEST.get('trips',json.dumps([]))
        
        product = Products()
        product.name = name
        product.price = price
        product.price_type = price_type
        product.total_price = price*price_type
        product.order_time = datetime.datetime.strptime(order_time,'%Y-%m-%d')
        product.trip_start_time = datetime.datetime.strptime(trip_start_time,'%Y-%m-%d')
        product.trip_end_time = datetime.datetime.strptime(trip_end_time,'%Y-%m-%d')
        product.key_desc = key_desc
        product.start_city = start_city
        product.end_city = end_city
        product.pics = pics
        product.trips = trips
        product.date_count = len(json.loads(trips))
        product.user = request.user
        try:
            product.save()
            return HttpResponseRedirect('/ink/product/index')
        except:
            return {}
    return {}

@render_to('ink/product/update.html')
def update(request,pid):
    product = Products.objects.get(id=pid)
    if request.method=='POST':
        name = request.REQUEST.get('name','')
        price = float(request.REQUEST.get('price',1))
        price_type = float(request.REQUEST.get('price_type',1))
        order_time = request.REQUEST.get('order_time',datetime.datetime.now().strftime('%Y-%m-%d'))
        trip_start_time = request.REQUEST.get('trip_start_time',datetime.datetime.now().strftime('%Y-%m-%d'))
        trip_end_time = request.REQUEST.get('trip_end_time',datetime.datetime.now().strftime('%Y-%m-%d'))
        key_desc = request.REQUEST.get('key_desc','')
        start_city = request.REQUEST.get('start_city','')
        end_city = request.REQUEST.get('end_city','')
        pics = request.REQUEST.get('pics','')
        trips = request.REQUEST.get('trips',json.dumps([]))
        
        product.name = name
        product.price = price
        product.price_type = price_type
        product.total_price = price*price_type
        product.order_time = datetime.datetime.strptime(order_time,'%Y-%m-%d')
        product.trip_start_time = datetime.datetime.strptime(trip_start_time,'%Y-%m-%d')
        product.trip_end_time = datetime.datetime.strptime(trip_end_time,'%Y-%m-%d')
        product.key_desc = key_desc
        product.start_city = start_city
        product.end_city = end_city
        product.pics = pics
        product.trips = trips
        product.date_count = len(json.loads(trips))
        product.user = request.user
        try:
            product.save()
            return HttpResponseRedirect('/ink/product/index')
        except:
            return {}

    return {'product':product}

def delete(request,pid):
    try :
        product = Products.objects.get(id=cid)
        product.delete()
    except:
        return json_response({'ret':False,'message':u'删除出错'})
    return json_response({'ret':True,'message':u'删除成功'})