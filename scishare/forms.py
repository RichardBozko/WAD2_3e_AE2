from django import forms
#from django.forms import MoelForm
from django.contrib.auth.models import User

from scishare.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

'''
class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('name', 'email', 'picture',)
'''

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'email', 'picture']

class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']




