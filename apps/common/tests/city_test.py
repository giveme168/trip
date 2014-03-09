# -*- coding:utf8 -*-
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client

from apps.common.models.city import City

import simplejson as json


class CityTest(TestCase):
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

    def test_city_index(self):
        response = self.c.get('/common/city/index')
        self.assertEqual(response.status_code,200)

    def test_city_create(self):
        params = {}
        params['continent'] = 1
        params['city_zh'] = '海南'
        params['city_en'] = 'HaiNan'

        response = self.c.post('/common/city/create',params)
        self.assertEqual(response.status_code,302)

    def test_city_update(self):
        self.test_city_create()

        params = {}
        params['continent'] = 1
        params['city_zh'] = '海南1'
        params['city_en'] = 'HaiNan2'

        response = self.c.post('/common/city/1/update',params)
        self.assertEqual(response.status_code,302)

    def test_city_delete(self):
        response = self.c.get('/common/city/1/delete')
        self.assertEqual(response.status_code,200)