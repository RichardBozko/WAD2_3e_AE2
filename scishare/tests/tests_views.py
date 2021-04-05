from django.test import TestCase, Client
import os
from django.urls import reverse, resolve
from scishare.views import *
from scishare.models import *
import json


class TestViews(TestCase):

	def setUp(self):
		self.login_url_GET = reverse('scishare:login')
		self.login_url_POST = ""
		self.register_url_GET = reverse('scishare:register')
		self.register_url_POST = ""


	def test_register_GET(self):
		clinet = Client()
		response = clinet.get(self.register_url_GET)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/register.html')

	def test_login_GET(self):
		clinet = Client()
		response = clinet.get(self.login_url_GET)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/login.html')


'''
class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

	def test_register_GET(self):
		clinet = Client()
		response = clinet.get(reverse('scishare:register'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/register.html')
'''