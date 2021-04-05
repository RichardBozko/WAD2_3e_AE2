from django.test import TestCase, Client
import os
from django.urls import reverse, resolve
from scishare.views import *
from scishare.models import *
from scishare.forms import UserUpdateForm, UserCreateForm
import json


class TestViews(TestCase):

	def setUp(self):
		'''
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
		'''
		self.login_url_GET = reverse('scishare:login')
		#self.login_url_POST = ""
		self.register_url_GET = reverse('scishare:register')
		self.home_url = reverse('scishare:home')
		#self.register_url_POST = ""

	# Test whether GET works for register page
	def test_register_GET(self):
		clinet = Client()
		response = clinet.get(self.register_url_GET)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/register.html')

	# Test whether GET works for login page
	def test_login_GET(self):
		clinet = Client()
		response = clinet.get(self.login_url_GET)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/login.html')

	# Check whether POST to register results in a functional user
	# *IF* a viable form is supplied
	def test_register_POST_good(self):
		u_data = {'username': 'Ford_Prefect', 
		 'password1': 'beetlejuice42',
		 'password2': 'beetlejuice42',
		  'email': 'FP@gmail.com'}
		u_form = UserCreateForm(data = u_data)
		self.assertTrue(u_form.is_valid())
		actual_user = u_form.save()
		self.assertTrue(self.client.login(username='Ford_Prefect', password='beetlejuice42'))
		
	# Check whether errors happen if empty form is supplied
	def test_register_POST_bad(self):
		request = self.client.post(reverse('scishare:register'))
		content = request.content.decode('utf-8')
		self.assertTrue('<ul class="errorlist">' in content)


'''
	#clinet = Client()


		#response = clinet.get(self.register_url_GET)
		#self.assertEquals(response.status_code, 200)
		#self.assertTemplateUsed(response, 'registration/register.html')

	def test_login_POST(self):
		clinet = Client()
		response = clinet.get(self.login_url_GET)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/login.html')




class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

	def test_register_GET(self):
		clinet = Client()
		response = clinet.get(reverse('scishare:register'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/register.html')
'''