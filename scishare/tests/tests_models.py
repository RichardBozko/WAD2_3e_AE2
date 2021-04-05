# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
import os
from django.urls import reverse
from django.conf import settings
from scishare.models import Category, Study, UserProfile
from django.contrib.auth.models import User



class TestScishareModels(TestCase):
	def test_category_str(self):
		name = Category.objects.create(name = "Biology")
		self.assertEqual(str(name), "Biology")

	def test_study_str(self):
		daddy = Category.objects.create(name = "Biology")
		title = Study.objects.create(title = "The Powerhouse of the Cell", category = daddy)
		self.assertEqual(str(title), "The Powerhouse of the Cell")

'''
	def test_study_upvotes(self):
		testuser1 = User.objects.create(
			username = "testuser1", email = "testu1@gmail.com", password1 = "1testing23", password2 = "1testing23"
			)
		testuser2 = User.objects.create(
			username = "testuser2", email = "testu2@gmail.com", password1 = "1testing23", password2 = "1testing23"
			)
		study1 = Study.objects.create(title = "TAI42")

	def test_study_downvotes(self):
		#testuser1 = User




class URLTests(TestCase):
	def test_homepage(self):
		response = self.client.get('scishare:home')
		self.assertEqual(response.status_code, 200)

'''

# Create your tests here.
