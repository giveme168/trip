# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.account.views.order',
    url(r'^order/$','index',name='chart_index'),
    url(r'^order/(?P<oid>\d+)/delete$','delete',name='chart_delete'),
    url(r'^order/(?P<oid>\d+)/show$','show',name='chart_show'),
    url(r'^order/pay$','pay',name='chart_pay'),
)
urlpatterns += patterns('apps.account.views.chart',
    url(r'^chart/$','index',name='order_index'),
    url(r'^chart/(?P<oid>\d+)/delete$','delete',name='order_delete'),
)