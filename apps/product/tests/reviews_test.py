# -*- coding:utf8 -*-
import datetime

from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
import simplejson as json

from apps.product.models.product import Products


class ReviewsTest(TestCase):
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

        product = Products()
        product.name = '123123'
        product.price = 123
        product.price_type = 1
        product.total_price = 1*2
        product.order_time = datetime.datetime.strptime('2014-03-20','%Y-%m-%d')
        product.trip_start_time = datetime.datetime.strptime('2014-06-20','%Y-%m-%d')
        product.trip_end_time = datetime.datetime.strptime('2014-09-09','%Y-%m-%d')
        product.key_desc = '123'
        product.start_city = '123'
        product.end_city = '123'
        product.pics = ''
        product.trips = ''
        product.date_count = 4
        product.user = self.user
        product.save()

        self.product = product

    def test_reviews_index(self):
        response = self.c.get('/product/reviews/1000/index')
        self.assertEqual(response.status_code,200)

    def test_reviews_create(self):
        params = {}
        params['product'] = self.product.id
        params['type'] = 2
        params['content'] = ''
        params['star'] = 5

        response = self.c.post('/product/reviews/1000/create',params)
        self.assertEqual(response.status_code,302)

    def test_reviews_update(self):
        self.test_reviews_create()

        params = {}
        params['type'] = 2
        params['content'] = '123'
        params['star'] = 5

        response = self.c.post('/product/reviews/1/update',params)
        self.assertEqual(response.status_code,302)

    def test_reviews_delete(self):
        response = self.c.get('/product/reviews/1/delete')
        self.assertEqual(response.status_code,200)