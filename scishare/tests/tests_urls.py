# -*- coding: utf-8 -*-
from django.test import TestCase
import os
from django.urls import reverse, resolve
from scishare.views import *

class TestUrls(TestCase):
	# Simple check whether a URL leads where it should 
	# (used for learning, kept it here)

	# The whole url.func is derived from printing url (that one took me a while hehe)
	def test_home_resolves(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)

	def test_groups_resolves(self):
		url = reverse('scishare:groups')
		self.assertEquals(resolve(url).func, groups)

	# Test whether works with slugs
	def test_category_w_slug(self):
		url = reverse('scishare:show_category', args = ['my_favorite_slug'])
		self.assertEquals(resolve(url).func, show_category)

	