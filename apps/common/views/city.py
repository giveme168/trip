# -*- coding:utf8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from annoying.decorators import render_to,ajax_request
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import simplejson as json 
import datetime

from contrib.shortcuts import json_response
from apps.common.models.city import City


@render_to('common/city/index.html')
def index(request):
    name = request.REQUEST.get('name','')
    page = int(request.REQUEST.get('page',1))
    if name:
        citys = City.objects.filter(city_zh__contains = name, user=request.user)
    else:
        citys = City.objects.all()

    paginator=Paginator(citys,10)
    page_count= paginator.count
    try:
        citys=paginator.page(page)
    except (EmptyPage,InvalidPage):
        citys=paginator.page(paginator.num_pages)
    return {'page_count':page_count,'citys':citys}

@render_to('common/city/create.html')
def create(request):
    if request.method=='POST':
        continent = int(request.REQUEST.get('continent',1))
        city_zh = request.REQUEST.get('city_zh','')
        city_en = request.REQUEST.get('city_en','')

        city = City()
        city.continent = continent
        city.city_zh = city_zh
        city.city_en = city_en
        try:
            city.save()
            return HttpResponseRedirect('/common/city/index')
        except:
            return {}
    return {}

@render_to('common/city/update.html')
def update(request,cid):
    city = City.objects.get(id=cid)
    if request.method=='POST':
        continent = int(request.REQUEST.get('continent',1))
        city_zh = request.REQUEST.get('city_zh','')
        city_en = request.REQUEST.get('city_en','')
        
        city.continent = continent
        city.city_zh = city_zh
        city.city_en = city_en
        try:
            city.save()
            return HttpResponseRedirect('/common/city/index')
        except Exception as e:
            print e
            return {}

    return {'product':product}

def delete(request,cid):
    try :
        city = City.objects.get(id=cid)
        city.delete()
    except:
        return json_response({'ret':False,'message':u'删除出错'})
    return json_response({'ret':True,'message':u'删除成功'})