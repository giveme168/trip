# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.order.views.order',
	url(r'^index$','index',name='order_index'),
    url(r'^create$','create',name='order_create'),
    url(r'^(?P<oid>\d+)/update$','update',name='order_update'),
    url(r'^(?P<oid>\d+)/delete$','delete',name='order_delete'),
)