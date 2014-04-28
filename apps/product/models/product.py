# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

#产品
class Products(models.Model):
    PTYPE_CHOICES = ((1,u'人民币'),(2,u'美元'),(3,u'欧元'),(4,u'英镑'))
    STATUS = ((1,u'未审核'),(2,u'上架'),(3,u'已到期或下架'),(4,u'已删除'))
    id = models.AutoField(u'产品编号', primary_key=True, help_text=u'产品编号')
    name = models.CharField(u'名称', max_length=254, help_text=u"名称", db_index=True)
    price_type = models.IntegerField(u'货币类型', max_length=2, choices=PTYPE_CHOICES, default=1 ,help_text=u'货币类型')

    price_by_one = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_one = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)
    
    price_by_two = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_two = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)

    price_by_three = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_three = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)

    price_by_four = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_four = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)

    price_by_five = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_five = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)

    price_by_six = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_six = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)

    price_by_serven = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_serven = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)

    price_by_eight = models.FloatField(u'原始价钱', max_length=64, help_text=u'原始价钱')
    total_price_by_eight = models.FloatField('人民币总价', max_length=64, help_text=u'人民币总价', default=1, db_index=True)

    order_time = models.DateTimeField(u'订单截至时间', help_text=u'订单截至时间', db_index=True)
    trip_start_time = models.DateTimeField(u'旅行开始时间', help_text=u'旅行开始时间', db_index=True)
    trip_end_time = models.DateTimeField(u'旅行结束时间', help_text=u'旅行结束时间', db_index=True)
    key_desc = models.TextField(u'关键销售点', help_text=u"关键销售点")
    start_city = models.CharField(u'出发城市', max_length=64, help_text=u"出发城市", db_index=True)
    end_country = models.CharField(u'目的国家', max_length=64, help_text=u"目的国家", db_index=True)
    end_city = models.CharField(u'目的城市', max_length=254,help_text=u'目的城市', db_index=True)
    language = models.CharField(u'服务语言',max_length=254,help_text=u'服务语言',db_index=True)
    pics = models.CharField(u'首图片', max_length=254, help_text=u"首图片")
    trips = models.TextField(u'旅途安排')
    date_count = models.IntegerField(u'旅程天数', max_length=2, help_text=u'旅程天数',db_index=True)
    user = models.ForeignKey(User)
    status = models.IntegerField(u'状态', choices=STATUS, help_text=u'状态', default=1,db_index=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间',db_index=True)
    body = models.TextField(u'其他说明')

    class Meta:
        app_label = 'product' 
        ordering = ['-create_time']

#升级套餐
class Product_Add_Service(models.Model):
    PTYPE_CHOICES = ((1,u'人民币'),(2,u'美元'),(3,u'欧元'),(4,u'英镑'))
    prodect = models.ForeignKey(Products)
    content = models.TextField(u'升级内容')
    price_type = models.IntegerField(u'货币类型', max_length=2, choices=PTYPE_CHOICES, default=1 ,help_text=u'货币类型')
    price_by_one = models.FloatField(u'原始价钱', max_length=64, default=1, help_text=u'原始价钱')
    total_price_by_one = models.FloatField('人民币总价', max_length=64, default=1, help_text=u'人民币总价', db_index=True)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间',db_index=True)
    body = models.TextField(u'其他说明')
    
    class Meta:
        app_label = 'product' 
        ordering = ['-create_time']

#特殊标签
class Special_Tags(models.Model):
    name = models.CharField(u'名称',max_length=128,help_text="名称",db_index=True)
    name_en = models.CharField(u'英文名称',max_length=128,help_text="英文名称",db_index=True)
    create_time = models.DateTimeField('创建时间',auto_now_add=True,default=datetime.datetime.now(),help_text='创建时间',db_index=True)

    class Meta:
        app_label = 'product' 
        ordering = ['-create_time']
        unique_together = (('name'),)

#产品特殊分类
class Product_Tags(models.Model):
    prodect = models.ForeignKey(Products)
    tag = models.ForeignKey(Special_Tags)

    class Meta:
        app_label = 'product'
        unique_together = (('prodect','tag'),)

#产品评价
class Product_Reviews(models.Model):
    TYPE_CHOICES = ((1,'购买前评价'),(2,'购买后评价'))
    product = models.ForeignKey(Products)
    user = models.ForeignKey(User)
    type = models.IntegerField(u'评价类型',max_length=2, choices=TYPE_CHOICES, help_text=u'评价类型',db_index=True)
    content = models.CharField(u'内容',max_length=254,help_text=u'内容')
    star = models.IntegerField(u'星评',max_length=1,help_text=u'星评',db_index=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间',db_index=True)

    class Meta:
        app_label = 'product'
        ordering = ['-create_time']
