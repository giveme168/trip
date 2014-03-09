# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.common.views.city',
    url(r'^city/index$','index',name='common_city_index'),
    url(r'^city/create$','create',name='common_city_create'),
    url(r'^city/(?P<cid>\d+)/update$','update',name='common_city_update'),
    url(r'^city/(?P<cid>\d+)/delete$','delete',name='common_city_delete'),
)

urlpatterns += patterns('apps.common.views.hotel',
    url(r'^hotel/index$','index',name='common_hotel_index'),
    url(r'^hotel/create$','create',name='common_hotel_create'),
    url(r'^hotel/(?P<hid>\d+)/update$','update',name='common_hotel_update'),
    url(r'^hotel/(?P<hid>\d+)/delete$','delete',name='common_hotel_delete'),
)

urlpatterns += patterns('apps.common.views.price_rate',
    url(r'^price_rate/index$','index',name='common_price_rate_index'),
    url(r'^price_rate/create$','create',name='common_price_rate_create'),
    url(r'^price_rate/(?P<pid>\d+)/update$','update',name='common_price_rate_update'),
    url(r'^price_rate/(?P<pid>\d+)/delete$','delete',name='common_price_rate_delete'),
)