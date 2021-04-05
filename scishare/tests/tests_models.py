# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
from scishare.models import Category, Study, UserProfile, Group
from django.contrib.auth.models import User



class TestScishareModels(TestCase):

	# Setup -> makes objects to be used/tested below
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


		self.category42 = Category.objects.create(name = "Biology")

		self.study42 = Study.objects.create(title = "The Powerhouse of the Cell", 
			category = self.category42)

		self.user_p_42 = UserProfile.objects.create(
			user = self.user_1,
			username = self.user_1.username,
			email = self.user_1.email
			
			)


	



	# All test whether an object is created correctly 
	def test_category_str(self):
		self.assertEqual(str(self.category42), "Biology")

	# in cases like this that included checking for parrent (category to which a study belongs)
	def test_study_str(self):
		#daddy = Category.objects.create(name = "Biology")
		#title = Study.objects.create(title = "The Powerhouse of the Cell", category = daddy)
		self.assertEqual(str(self.study42), "The Powerhouse of the Cell")

	# Object made correcly + user&study numbers correct
	def test_group(self):
		group_t = Group.objects.create(
			group_name = "Slartibartfasts",
			group_slug = "my_slug",
			
			)	
		group_t.group_studies.set([self.study42])
		group_t.members.set([self.user_1, self.user_42])
		self.assertEqual(str(group_t), "Slartibartfasts")
		self.assertEqual(group_t.members.all().count(), 2)
		self.assertEqual(group_t.group_studies.all().count(), 1)


	
	# Test whether there is only 1 user and whether it's object was made correctly
	# Also that the object has a picture
	# (Since none was set this menas the default pic works)
	def test_profiles(self):
		self.assertEqual(str(self.user_p_42), "u1")
		self.assertEqual(UserProfile.objects.all().count(), 1)
		self.assertTrue(UserProfile.picture)




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
