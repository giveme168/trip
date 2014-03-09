# -*- coding:utf8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from annoying.decorators import render_to,ajax_request
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import simplejson as json 
import datetime

from contrib.shortcuts import json_response
from apps.common.models.price_rate import PriceRate


@render_to('common/price_rate/index.html')
def index(request):
    type = request.REQUEST.get('type','')
    page = int(request.REQUEST.get('page',1))
    if type:
        rates = PriceRate.objects.filter(price_type = type)
    else:
        rates = PriceRate.objects.all()

    paginator=Paginator(rates,10)
    page_count= paginator.count
    try:
        rates=paginator.page(page)
    except (EmptyPage,InvalidPage):
        rates=paginator.page(paginator.num_pages)
    return {'page_count':page_count,'rates':rates}

@render_to('common/price_rate/create.html')
def create(request):
    if request.method=='POST':
        price_type = int(request.REQUEST.get('price_type',1))
        rate = float(request.REQUEST.get('rate',1))
        price = PriceRate()
        price.price_type = price_type
        price.rate = rate

        try:
            price.save()
            return HttpResponseRedirect('/common/price_rate/index')
        except Exception as e:
            print e
            return {}
    return {}

@render_to('common/price_rate/update.html')
def update(request,pid):
    price = PriceRate.objects.get(id=pid)
    if request.method=='POST':
        price_type = int(request.REQUEST.get('type',1))
        rate = float(request.REQUEST.get('rate',1))
        
        price.price_type = price_type
        price.rate = rate
        try:
            price.save()
            return HttpResponseRedirect('/common/price_rate/index')
        except Exception as e:
            print e
            return {}

    return {'product':product}

def delete(request,pid):
    try :
        price = PriceRate.objects.get(id=pid)
        price.delete()
    except:
        return json_response({'ret':False,'message':u'删除出错'})
    return json_response({'ret':True,'message':u'删除成功'})