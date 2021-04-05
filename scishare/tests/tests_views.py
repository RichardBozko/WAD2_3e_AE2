from django.test import TestCase, Client
import os
from django.urls import reverse, resolve
from scishare.views import *
from scishare.models import *
import json


class TestViews(TestCase):

	def setUp(self):

		self.user_1 = User.objects.create(
			username = "u1", 
			email = "u1@gmail.com",
			password = "fourtytwo42",
			)
		self.user_42 = User.objects.create(
			username = "u42", 
			email = "u42@gmail.com",
			password = "fourtytwo42",
			)

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

	def test_register_POST(self):
		clinet = Client()
		response = clinet.get(self.register_url_GET)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/register.html')

	def test_login_POST(self):
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