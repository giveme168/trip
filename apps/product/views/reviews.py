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

@render_to('product/reviews/index.html')
def index(request,pid):
    page = int(request.REQUEST.get('page',1))
    reviews = Product_Reviews.objects.filter(product__id = pid)
    paginator=Paginator(reviews,10)
    page_count= paginator.count
    try:
        reviews=paginator.page(page)
    except (EmptyPage,InvalidPage):
        reviews=paginator.page(paginator.num_pages)
    return {'page_count':page_count,'reviews':reviews}

@render_to('product/reviews/create.html')
def create(request,pid):
    if request.method=='POST':
        content = request.REQUEST.get('content','')
        star = int(request.REQUEST.get('star',5))
        type = int(request.REQUEST.get('type',1))
        
        rev = Product_Reviews()
        rev.product = Products.objects.get(id=pid)
        rev.user = request.user
        rev.type = type
        rev.content = content
        rev.star = star
        try:
            rev.save()
            return HttpResponseRedirect('/common/city/index')
        except Exception as e:
            print e
            return {}
    return {}

@render_to('product/reviews/update.html')
def update(request,rid):
    rev = Product_Reviews.objects.get(id=rid)
    if request.method=='POST':
        content = request.REQUEST.get('content','')
        star = int(request.REQUEST.get('star',5))
        
        rev.user = request.user
        rev.content = content
        rev.star = star
        try:
            rev.save()
            return HttpResponseRedirect('/common/city/index')
        except Exception as e:
            print e
            return {}

    return {'product':product}

def delete(request,rid):
    try :
        rev = Product_Reviews.objects.get(id=rid)
        rev.delete()
    except:
        return json_response({'ret':False,'message':u'删除出错'})
    return json_response({'ret':True,'message':u'删除成功'})