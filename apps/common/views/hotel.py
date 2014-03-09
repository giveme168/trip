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
from apps.common.models.hotel import Hotels


@render_to('common/hotel/index.html')
def index(request):
    name = request.REQUEST.get('name','')
    page = int(request.REQUEST.get('page',1))
    if name:
        hotels = Hotels.objects.filter(city_zh__contains = name)
    else:
        hotels = Hotels.objects.all()

    paginator=Paginator(hotels,10)
    page_count= paginator.count
    try:
        hotels=paginator.page(page)
    except (EmptyPage,InvalidPage):
        hotels=paginator.page(paginator.num_pages)
    return {'page_count':page_count,'hotels':hotels}

@render_to('common/hotel/create.html')
def create(request):
    if request.method=='POST':
        city = int(request.REQUEST.get('city',0))
        name = request.REQUEST.get('name','')
        star = request.REQUEST.get('star','')
        desc = request.REQUEST.get('desc','')

        hotel = Hotels()
        hotel.city = City.objects.get(id=city)
        hotel.name = name
        hotel.star = star
        hotel.desc = desc

        try:
            hotel.save()
            return HttpResponseRedirect('/common/hotel/index')
        except:
            return {}
    return {}

@render_to('common/hotel/update.html')
def update(request,hid):
    hotel = Hotels.objects.get(id=hid)
    if request.method=='POST':
        city = int(request.REQUEST.get('city',0))
        name = request.REQUEST.get('name','')
        star = request.REQUEST.get('star','')
        desc = request.REQUEST.get('desc','')

        
        hotel.city = City.objects.get(id=city)
        hotel.name = name
        hotel.star = star
        hotel.desc = desc
        try:
            hotel.save()
            return HttpResponseRedirect('/common/hotel/index')
        except Exception as e:
            print e
            return {}

    return {'product':product}

def delete(request,hid):
    try :
        hotel = Hotels.objects.get(id=hid)
        hotel.delete()
    except:
        return json_response({'ret':False,'message':u'删除出错'})
    return json_response({'ret':True,'message':u'删除成功'})