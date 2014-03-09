# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.product.views.reviews',
    url(r'^reviews/(?P<pid>\d+)/index$','index',name='product_reviews_index'),
    url(r'^reviews/(?P<pid>\d+)/create$','create',name='product_reviews_create'),
    url(r'^reviews/(?P<rid>\d+)/update$','update',name='product_reviews_update'),
    url(r'^reviews/(?P<rid>\d+)/delete$','delete',name='product_reviews_delete'),
)