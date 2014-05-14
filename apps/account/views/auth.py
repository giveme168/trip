# -*- coding:utf8 -*-
import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from annoying.decorators import render_to,ajax_request

import simplejson as json 

from contrib.shortcuts import json_response
from apps.common.models.city import City
from settings import LOGIN_REDIRECT_URL

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
            if path:
            	return HttpResponseRedirect(path)
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        else:
            return {'message':u'用户名或密码不正确'}
    return {'path':path,'message':message}

@render_to('account/auth/register.html')
def register(request):
    if request.method == 'POST':
        username = request.REQUEST.get('username','')
        password = request.REQUEST.get('password','')
        check_password = request.REQUEST.get('check_password','')
        if not username :
            return {'message':u'邮箱不能为空'}
        if not password :
            return {'message':u'密码不能为空'}
        if not check_password :
            return {'message':u'确认密码不能为空'}
        if password != check_password:
            return {'message':u'密码与确认密码不相同'}
        user = User()
        user.username = username
        user.set_password(check_password)
        try:
            user.save()
        except:
            return {'message':u'用户名已被使用'}
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        auth.login(request, user)
        return HttpResponseRedirect(LOGIN_REDIRECT_URL)
    return {}