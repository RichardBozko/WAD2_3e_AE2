from django import forms
from django.contrib.auth.models import User
from scishare.models import Category, Study, UserProfile, Group
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name:")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

# An inline class to provide additional info on the form.
	class Meta:
		# Provide association between the ModelForm and a model
		model = Category
		fields = ('name', )


class StudyForm(forms.ModelForm):
	title = forms.CharField(max_length=Study.TITLE_MAX_LENGTH, help_text="Please enter the title of the study:")
	url = forms.URLField(help_text="Please enter the URL of the study:")
	up_votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	down_votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	study_slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Study
		exclude = ('category', 'study_slug', )
	# not to include foreign key or specify the fields to include fields = ('title', 'url', 'views', )


class GroupForm(forms.ModelForm):
	group_name = forms.CharField(max_length=Group.GROUP_NAME_MAX_LENGTH, help_text="Please enter the name of the group:")
	members = forms.ModelMultipleChoiceField(
		queryset=User.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		help_text="Members of the group: "
	)
	group_slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Group
		fields = ('group_name', 'members')

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'email', 'picture']

class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']




