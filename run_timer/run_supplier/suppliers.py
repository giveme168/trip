#coding:utf-8

import logging
import datetime
import simplejson as json

import sys
from config import APP_PATH
from config import LOG_FILE
sys.path.append(APP_PATH) 

from django.core.management import setup_environ

import settings
setup_environ(settings)

from django.contrib.auth.models import User
from apps.account.models.auth_info import Info

SUPPLIERS = [
    {
        'username':'admin@compass.com',
        'email':'admin@compass.com',
        'password':'compass',
        'name':'compass',
        'cellphone':'18601111111',
        'description':'',
        'body':{
            'company_name':'compass',
            'authentication':True,                       #认证
            'qualification':'',                          #资质
            'country':u'中国',
            'city':u'北京',
            'address':u'北京市西城区德胜门内大街103号',
            'security_deposit':100*10000,                    #保证金
            'nick_name':'Rex',
            'key_tags':u'私人飞机|极光',
            'pics':'7477a3d7096d4ba2b8f5bfaee68b713b.jpg',
            'language':u'中文|英文',
            'weixin':'',
            'weibo':'',
            'QQ':'',
        }
    }
]

def run():

    for supplier in SUPPLIERS:
        user = User()
        user.email = supplier['email']
        user.username = supplier['email']
        user.set_password(supplier['password'])
        try:
            user.save()
        except:
            print supplier['email'],u'添加失败'
            return
        
        user_info = Info()
        user_info.user = user
        user_info.name = supplier['name']
        user_info.ID_type = 2
        user_info.cellphone = supplier['cellphone']
        user_info.description = supplier['description']
        user_info.body = json.dumps(supplier['body'])
        try:
            user_info.save()
        except:
            User.objects.get(id=user.id).delete()
            print supplier['email'],u'添加失败'
    return

if __name__ == '__main__':
    run()