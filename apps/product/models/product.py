# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

from apps.product.models.special_tag import SpecialTags


#产品
class Products(models.Model):
    PTYPE_CHOICES = ((1,u'人民币'),(2,u'美元'),(3,u'欧元'),(4,u'英镑'))
    STATUS = ((1,u'未审核'),(2,u'上架'),(3,u'已到期或下架'),(4,u'已删除'))
    id = models.AutoField('产品编号', primary_key=True, help_text='产品编号', default=1000)
    name = models.CharField(u'名称', max_length=254, help_text="名称", db_index=True)
    price = models.FloatField(u'价钱', max_length=64, help_text=u'价钱')
    price_type = models.IntegerField(u'货币类型', max_length=2, choices=PTYPE_CHOICES, default=1 ,help_text=u'货币类型')
    total_price = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', db_index=True)
    order_time = models.DateTimeField(u'订单截至时间', help_text=u'订单截至时间', db_index=True)
    trip_start_time = models.DateTimeField(u'旅行开始时间', help_text=u'旅行开始时间', db_index=True)
    trip_end_time = models.DateTimeField(u'旅行结束时间', help_text=u'旅行结束时间', db_index=True)
    key_desc = models.CharField(u'关键销售点', max_length=254, help_text=u"关键销售点")
    start_city = models.CharField(u'出发城市', max_length=64, help_text=u"出发城市", db_index=True)
    end_city = models.CharField(u'目的城市', max_length=64, help_text=u"目的城市", db_index=True)
    pics = models.CharField(u'首图片', max_length=254, help_text=u"首图片")
    trips = models.TextField(u'旅途安排')
    date_count = models.IntegerField(u'旅程天数', max_length=2, help_text=u'旅程天数',db_index=True)
    user = models.ForeignKey(User)
    status = models.IntegerField(u'状态', choices=STATUS, help_text=u'状态', default=1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间')
    
    class Meta:
        app_label = 'product' 
        ordering = ['-create_time']

#产品特殊分类
class Products_Tags(models.Model):
    prodect = models.ForeignKey(Products)
    tag = models.ForeignKey(SpecialTags)

    class Meta:
        app_label = 'product'
        unique_together = (('prodect','tag'),)

#产品评价
class Product_Reviews(models.Model):
    TYPE_CHOICES = ((1,'购买前评价'),(2,'购买后评价'))
    prodect = models.ForeignKey(Products)
    user = models.ForeignKey(User)
    type = models.IntegerField(u'评价类型',max_length=2, choices=TYPE_CHOICES, help_text=u'评价类型')
    content = models.CharField(u'内容',max_length=254,help_text=u'内容')
    star = models.IntegerField(u'星评',max_length=1,help_text=u'星评',db_index=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间')

    class Meta:
        app_label = 'product'
        ordering = ['-create_time']
