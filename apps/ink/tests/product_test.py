# -*- coding:utf8 -*-
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client

from apps.product.models.product import Products

import simplejson as json

class OrderTest(TestCase):
    def setUp(self):
        user = User()
        user.is_superuser = 1
        user.username = 'admin'
        user.set_password('password2')
        user.email = 'admin@cc.com'
        user.first_name = 'aa'
        user.is_active = 1
        user.save()
        self.user = user

        c = Client()
        self.c = c
        self.c.login( username='admin', password='password2')
    
    def test_product_create(self):
        params = {}
        params['name'] = u'海南七日游' 
        params['price'] = 14
        params['price_type'] = 1
        params['order_time'] = '2014-03-15'
        params['trip_start_time'] = '2014-06-15'
        params['trip_end_time'] = '2014-09-15'
        params['key_desc'] = u'无'
        params['start_city'] = u'北京'
        params['end_city'] = u'海南'
        params['pics'] = ''
        params['tags'] = '极地游|极光游|'
        params['trips'] = json.dumps([{'name':u'第一天'},{'name':u'第二天'}])

        response = self.c.post('/ink/product/create',params)
        self.assertEqual(response.status_code,302)

    def test_product_update(self):
        params = {}
        params['name'] = u'海南七日游' 
        params['price'] = 14
        params['price_type'] = 1
        params['order_time'] = '2014-03-15'
        params['trip_start_time'] = '2014-06-15'
        params['trip_end_time'] = '2014-09-15'
        params['key_desc'] = u'无'
        params['start_city'] = u'北京'
        params['end_city'] = u'海南'
        params['pics'] = ''
        params['tags'] = '极地游|极光游|'
        params['trips'] = json.dumps([{'name':u'第一天'},{'name':u'第二天'}])

        response = self.c.post('/ink/product/create',params)

        params = {}
        params['name'] = u'海南七日游2' 
        params['price'] = 14
        params['price_type'] = 1
        params['order_time'] = '2014-03-15'
        params['trip_start_time'] = '2014-06-15'
        params['trip_end_time'] = '2014-09-15'
        params['key_desc'] = u'无'
        params['start_city'] = u'北京'
        params['end_city'] = u'海南'
        params['pics'] = ''
        params['tags'] = '极地游|极光游|'
        params['trips'] = json.dumps([{'name':u'第一天'},{'name':u'第二天'}])

        response = self.c.post('/ink/product/1000/update',params)

        self.assertEqual(response.status_code,302)

    def test_product_delete(self):
        response = self.c.post('/ink/product/1000/delete')
        self.assertEqual(response.status_code,200)

    def test_product_index(self):
        response = self.c.get('/ink/product/index')
        self.assertEqual(response.status_code,200)
