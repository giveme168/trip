# -*- coding:utf8 -*-

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


def current_user(request):
    user = request.user
    '''power = {}
    try:
        is_super = user.is_superuser
        if is_super:
            powers = [
                'http_source_add','http_source_edit','http_source_delete',
                'http_task_add','http_task_edit','http_task_delete','http_task_down',
                'dns_source_add','dns_source_edit','dns_source_delete',
                'dns_task_add','dns_task_edit','dns_task_delete','dns_task_down',
                'monitor_http_add','monitor_http_edit','monitor_http_delete',
                'monitor_person_add','monitor_person_edit','monitor_person_delete',
                'monitor_control_delete','http_show','dns_show','monitor_show'
            ]
            for k in powers:
                power[k] = True
        else:
            userpower = UserPower.objects.get(user=user)
            for k in userpower.power.power.split('|')[:-1]:
                power[k] = True
    except Exception as e:
        print e
        is_super = False
    return {'current_user': request.user,'is_super':is_super,'user_id':user.id,'power':power}'''
    if not user.username:
        user = None
    return {'current_user':user}

def is_super_permission(redirect_url='error.html', login_url='/'):
    def wrapper(f):
        def decorate(*arg):
            request = arg[0]
            if not request.user.is_superuser:
                return render_to_response(redirect_url,{'message':u'对不起您权限不够'})
            else:
                return f(arg[0])
        return decorate
    return wrapper

def authority_required(redirect_url='/', login_url='/'):
    """
    Decorator for views that checks whether a user has a service permission
    enabled, redirecting to the redirect page if necessary.
    """
    def wrapper(f):
        def decorate(*arg):
            request = arg[0]
            if not request.user.id:
            	return HttpResponseRedirect(redirect_url)
            else:
            	return f(arg[0])
        return decorate
    return wrapper