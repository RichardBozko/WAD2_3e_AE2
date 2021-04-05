# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
import os
from django.urls import reverse
from django.conf import settings
from scishare.models import Category


class TestScishareModels(TestCase):
	def test_category_str(self):
		name = Category.objects.create(name = "Biology")
		self.assertEqual(str(name), "Biology")





'''
class URLTests(TestCase):
	def test_homepage(self):
		response = self.client.get('scishare:home')
		self.assertEqual(response.status_code, 200)

'''

# Create your tests here.
