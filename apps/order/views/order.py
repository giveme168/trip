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
from apps.order.models.order import Orders
from util.alipay import pay_req


def alipay(request,pid):
    #if not request.user.id:
    #    return HttpResponseRedirect('/login/?path=/product/%s/show/'%(pid))
    product = Products.objects.get(id=pid)
    notify_url_default = 'http://www.gettrip.com/alipay/notify'
    return_url_default = 'http://www.gettrip.com/alipay/redirect'
    ret_url = pay_req(product.id, product.name, product.name, product.price, notify_url = notify_url_default, return_url = return_url_default)
    return HttpResponseRedirect(ret_url)

@render_to('ink/product/index.html')
def index(request):
    name = request.REQUEST.get('name','')
    page = int(request.REQUEST.get('page',1))
    if name:
        orders = Orders.objects.filter(name__contains = name, user=request.user)
    else:
        orders = Orders.objects.filter(user=request.user)

    paginator=Paginator(orders,10)
    page_count= paginator.count
    try:
        orders=paginator.page(page)
    except (EmptyPage,InvalidPage):
        orders=paginator.page(paginator.num_pages)
    return {'page_count':page_count,'orders':orders}

@render_to('ink/product/create.html')
def create(request):
    if request.method=='POST':
        pid = request.REQUEST.get('product','')
        trip_date = datetime.datetime.strptime(request.REQUEST.get('trip_date',datetime.datetime.now().strftime('%Y-%m-%d')),'%Y-%m-%d')
        
        product = Products.objects.get(id=pid)
        if product.trip_start_time <= trip_date <= product.trip_end_time:
            order = Orders()
            order.user = request.user
            order.name = product.name
            order.product = product.id
            order.price = product.total_price
            order.product_info = ''
            order.trip_date = trip_date
            order.save()
            try:
                order.save()
                return HttpResponseRedirect('/order/index')
            except:
                print '异常'
                #异常
                return {}
        else:
            #订单无效
            print '日期超出'
            return {}
    return {}

@render_to('ink/product/update.html')
def update(request,oid):
    order = Orders.objects.get(oid=oid)
    if request.method=='POST':
        trip_date = datetime.datetime.strptime(request.REQUEST.get('trip_date',datetime.datetime.now().strftime('%Y-%m-%d')),'%Y-%m-%d')
        try:
            product = Products.objects.get(id=order.product)
        except:
            #找不到产品信息
            return {}

        if product.trip_start_time <= trip_date <= product.trip_end_time:
            order.trip_date = trip_date
            try:
                order.save()
                return HttpResponseRedirect('/order/index')
            except:
                return {}
        else:
            #选择日期超过产品日期
            return {}
    return {'order':order}

def delete(request,oid):
    try :
        order = Orders.objects.get(oid=int(oid))
        order.status=3
        order.save()
    except:
        return json_response({'ret':False,'message':u'删除出错'})
    return json_response({'ret':True,'message':u'删除成功'})