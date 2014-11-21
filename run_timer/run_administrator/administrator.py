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
        'username':'admin@huohuatrip.com',
        'email':'admin@huohuatrip.com',
        'password':'admin',
        'name':'admin',
        'cellphone':'18601111111',
        'description':'普通管理员',
        'body':''
    }
]

def run():

    for supplier in SUPPLIERS:
        user = User()
        user.username = supplier['email']
        user.email = supplier['email']
        user.set_password(supplier['password'])
        try:
            user.save()
        except:
            print supplier['email'],u'添加失败'
            return
        
        user_info = Info()
        user_info.user = user
        user_info.name = supplier['name']
        user_info.ID_type = 3
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