# -*- coding:utf8 -*-
from django.conf.urls.defaults  import *

urlpatterns = patterns('apps.company.views.company',
    url(r'^(?P<cid>\d+)/index/$','index',name='company_index'),
)