# -*- coding:utf8 -*-
import datetime

from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from annoying.decorators import render_to,ajax_request

import simplejson as json 

from contrib.shortcuts import json_response
from apps.common.models.city import City
from settings import LOGIN_REDIRECT_URL

@render_to('index.html')
def index(request):
    return {}

@render_to('account/auth/login.html')
def login(request):
    path = request.REQUEST.get('path','')
    message = ''
    if path:
        message = u'请您登录'   
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None :
            auth.login(request, user)
            print '1111'
            print path
            if path:
            	return HttpResponseRedirect(path)
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        else:
            return {'message':u'用户名或密码不正确'}
    return {'path':path,'message':message}