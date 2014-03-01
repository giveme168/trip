# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime


#特殊标签
class SpecialTags(models.Model):
    name = models.CharField(u'名称',max_length=128,help_text="名称")
    name_en = models.CharField(u'英文名称',max_length=128,help_text="英文名称")
    create_time = models.DateTimeField('创建时间',auto_now_add=True,default=datetime.datetime.now(),help_text='创建时间')

    class Meta:
        app_label = 'product' 
        ordering = ['-create_time']
        unique_together = (('name'),)

        