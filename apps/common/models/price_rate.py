# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime


#汇率
class PriceRate(models.Model):
    PRICE_TYPE = ((1,u'人民币'),(2,u'美元'),(3,u'欧元'),(4,u'英镑'))
    price_type = models.IntegerField(u'币种', max_length=2, choices=PRICE_TYPE, help_text=u'币种')
    rate = models.FloatField(u'汇率', max_length=64, help_text=u'汇率')

    class Meta:
        app_label = 'common'
        unique_together = (('price_type'),('rate'))
