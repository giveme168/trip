# -*- coding:utf8 -*-
from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client

from apps.common.models.city import City
from apps.common.models.hotel import Hotels

import simplejson as json


class HotelTest(TestCase):
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

    def test_hotel_index(self):
        response = self.c.get('/common/hotel/index')
        self.assertEqual(response.status_code,200)

    def test_hotel_create(self):
        city = City()
        city.continent = 1
        city.city_zh = '海南'
        city.city_en = 'HaiNan'
        city.save()

        params = {}
        params['city'] = 1
        params['name'] = '北京饭店'
        params['star'] = 5
        params['desc'] = '五星级饭店'
        response = self.c.post('/common/hotel/create',params)
        self.assertEqual(response.status_code,302)

    def test_hotel_update(self):
        self.test_hotel_create()

        params = {}
        params['city'] = 1
        params['name'] = '北京饭店1'
        params['star'] = 5
        params['desc'] = '五星级饭店1'

        response = self.c.post('/common/hotel/1/update',params)
        self.assertEqual(response.status_code,302)

    def test_hotel_delete(self):
        response = self.c.get('/common/hotel/1/delete')
        self.assertEqual(response.status_code,200)