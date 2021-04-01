from django import forms
from django.contrib.auth.models import User
from scishare.models import Category, Study, UserProfile


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

# An inline class to provide additional info on the form.
	class Meta:
		# Provide association between the ModelForm and a model
		model = Category
		fields = ('name', )


class StudyForm(forms.ModelForm):
	title = forms.CharField(max_length=Study.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
	url = forms.URLField(help_text="Please enter the URL of the page.")
	up_votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	down_votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Study
		exclude = ('category', )
	# not to include foreign key or specify the fields to include fields = ('title', 'url', 'views', )


class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)

