# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.administrator.views.auth',
	url(r'^$','login',name='administrator_login'),
    url(r'^index/$','index',name='administrator_index'),
)
