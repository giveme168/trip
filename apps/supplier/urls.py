# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.supplier.views.supplier',
    url(r'^(?P<sid>\d+)/index/$','index',name='supplier_index'),
)