# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime


#用户资料
class Info(models.Model):
    ID_TYPE = ((0,u'both'),(1,u'普通用户'),(2,u'供应商'))
    user = models.ForeignKey(User)
    name = models.CharField('昵称',max_length=254,help_text=u'昵称', db_index=True)
    ID_type = models.IntegerField(u'用户身份', max_length=2, help_text=u'用户身份', default=1, choices=ID_TYPE, db_index=True)
    cellphone = models.CharField(u'联系方式', max_length=254, help_text="联系方式", db_index=True)
    description = models.TextField(u'描述信息')
    body = models.TextField(u'其他内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间')
    
    class Meta:
        app_label = 'auth'
        ordering = ['-create_time']