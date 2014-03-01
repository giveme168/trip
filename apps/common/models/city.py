# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime


#城市
class City(models.Model):
    TYPE_CONTIENT = ((1,'亚洲-Asia'),(2,'北美洲-North America'),(3,'南美洲-South America'),(4,'欧洲-Europe'),(5,'非洲-Africa'),(6,'大洋洲-Oceania'),(7,'南极洲-Antarctica'))
    continent = models.IntegerField(u'洲',choices=TYPE_CONTIENT,help_text=u'中文大洲',db_index=True)
    city_zh = models.CharField(u'中文城市',max_length=64,help_text=u'中文城市',db_index=True)
    city_en = models.CharField(u'英文城市',max_length=64,help_text=u'英文城市',db_index=True)

    class Meta:
        app_label = 'common'
        unique_together = (('city_zh'),('city_en'))
