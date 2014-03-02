# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime


#城市
class Orders(models.Model):
    STATUS = ((0,u'未付款'),(1,'已付款'),(2,'订单完成'),(3,'标记删除'))
    oid = models.AutoField('订单号', primary_key=True, help_text='订单号', default=1000)
    user = models.ForeignKey(User)
    name = models.CharField(u'名称', max_length=254, help_text="名称", db_index=True)
    status = models.IntegerField(u'订单状态', max_length=2, help_text=u'订单状态', default=0, db_index=True)
    product = models.IntegerField(u'所属产品', max_length=10, help_text=u'所属产品')
    price = models.FloatField(u'价钱', max_length=64, help_text=u'价钱')
    product_info = models.TextField()
    trip_date = models.DateTimeField('旅游时间', default=datetime.datetime.now(), help_text='旅游时间')
    create_time = models.DateTimeField('创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间')

    class Meta:
        app_label = 'order'
        ordering = ['-create_time']
