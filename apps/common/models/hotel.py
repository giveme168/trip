# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

from apps.common.models.city import City


#酒店
class Hotels(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(u'名称', max_length=128, help_text=u"名称")
    star = models.IntegerField(u'星级', max_length=2, help_text=u'星级')
    desc = models.TextField('详情')
    create_time = models.DateTimeField('创建时间', auto_now_add=True, default=datetime.datetime.now(), help_text='创建时间')

    class Meta:
        app_label = 'common' 
        ordering = ['-create_time']
        unique_together = (('city','name'),)

        