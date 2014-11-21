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
from apps.account.models.auth_info import Info
from settings import LOGIN_REDIRECT_URL

@render_to('administrator/login.html')
def login(request):
    message = ''
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None :
            info = Info.objects.get(user=user)
            if info.ID_type != 3:
                return {'message':u'对不起，您不能登录该系统'}
            auth.login(request, user)
            return HttpResponseRedirect('/administrator/index')
        else:
            return {'message':u'用户名或密码不正确'}
    if request.user.username:
        auth.logout(request)
    return {}

@render_to('administrator/index.html')
def index(request):

    return {}

@render_to('account/auth/register.html')
def register(request):
    if request.method == 'POST':
        username = request.REQUEST.get('username','')
        cellphone = request.REQUEST.get('cellphone','')
        email = request.REQUEST.get('email','')
        password = request.REQUEST.get('password','')
        check_password = request.REQUEST.get('check_password','')
        if not username:
            return {'message':u'昵称不能为空'}
        if not cellphone:
            return {'message':u'手机号码不能为空'}
        if not email :
            return {'message':u'邮箱不能为空'}
        if not password :
            return {'message':u'密码不能为空'}
        if not check_password :
            return {'message':u'确认密码不能为空'}
        if password != check_password:
            return {'message':u'密码与确认密码不相同'}

        user = User()
        user.username = email
        user.email = email
        user.set_password(check_password)
        try:
            user.save()
        except:
            return {'message':u'用户名已被使用'}
        user_info = Info()
        user_info.user = user
        user_info.name = username
        user_info.ID_type = 1
        user_info.cellphone = cellphone
        user_info.description = ''
        user_info.body = ''
        try:
            user_info.save()
        except:
            User.objects.get(id=user.id).delete()
            return {'message':u'出错，请稍后再试'}

        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        auth.login(request, user)
        return HttpResponseRedirect(LOGIN_REDIRECT_URL)
    return {}