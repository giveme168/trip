# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.ink.views.product',
	url(r'^product/rend_data$','rend_data',name='ink_product_rend_data'),
    url(r'^product/index$','index',name='ink_product_index'),
    url(r'^product/create$','create',name='ink_product_create'),
    url(r'^product/(?P<pid>\d+)/update$','update',name='ink_product_update'),
    url(r'^product/(?P<pid>\d+)/delete$','delete',name='ink_product_delete'),
)