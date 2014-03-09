# -*- coding:utf8 -*-
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client

import simplejson as json


class PriceRateTest(TestCase):
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

    def test_price_index(self):
        response = self.c.get('/common/price_rate/index')
        self.assertEqual(response.status_code,200)

    def test_price_create(self):
        params = {}
        params['price_type'] = 1
        params['rate'] = 1.0

        response = self.c.post('/common/price_rate/create',params)
        self.assertEqual(response.status_code,302)

    def test_price_update(self):
        self.test_price_create()

        params = {}
        params['price_type'] = 1
        params['rate'] = 1.0

        response = self.c.post('/common/price_rate/1/update',params)
        self.assertEqual(response.status_code,302)

    def test_price_delete(self):
        response = self.c.get('/common/price_rate/1/delete')
        self.assertEqual(response.status_code,200)