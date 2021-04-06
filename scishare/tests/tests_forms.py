from scishare.forms import *
from django.test import TestCase, Client

class TestForms(TestCase):

	def setUp(self):

		self.useru = {
			'email':'test@gmail.com',
			'username':'Spongebob',
			}

		self.userc = {
			'email':'test@gmail.com',
			'username':'Spongebob',
			'password':'ineedtosleep42',
			'password2':'ineedtosleep42',
        }

		self.user_1 = User.objects.create(
			username = "u1", 
			email = "u1@gmail.com",
			password = "fourtytwo42",
			)
		
		self.study1 = {
			'title':'S1',
			'url':'https://fbaum.unc.edu/teaching/articles/JPSP-2009-Moral-Foundations.pdf',
        	'up_votes': 1,
        	'down_votes': 2,
        	'study_slug': 'sslugg',

        }

		self.category1 = {
			'name':'Ctest',
			'views': 0,
			'likes': 1,
			'slug': 'helpful_slug',

        }




	def test_category_form(self):
		form = CategoryForm(data = self.category1)
		self.assertTrue(form.is_valid())

	def test_study_form(self):
		form = StudyForm(data = self.study1)
		self.assertTrue(form.is_valid())


	def test_group_form(self):
		data = {

			'group_name': 'People',
        	'group_slug': 'some_slug',
        	'members' : [self.user_1]

		}
		form = GroupForm(data = data)
		self.assertTrue(form.is_valid())


	def UserCreateForm(self):
		form = CategoryForm(data = self.userc)
		self.assertTrue(form.is_valid())


	def test_user_u_form(self):
		form = UserUpdateForm(data = self.useru)
		self.assertTrue(form.is_valid())


