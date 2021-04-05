from django.http import HttpResponse
from django.shortcuts import redirect


# Made this to abide by DNR, and though I will resuscitate (haha)
# With these, I need not repeat myself via if else statements 

# A custom decorator designed to prevent users from acessing 
# Functionalities that only staff should have access to
def user_permissions():
	def decorator(view_f):
		def wrapper(request, *args, **kwargs):
			if request.user.is_staff:
				return view_f(request, *args, **kwargs)
			else:
				return HttpResponse('You do not have the permissions to do that.\n'+
					'If you wish to change this, contact scisharegu@gmail.com about your request.')
		return wrapper
	return decorator

# If user logged in -> redirect to home (do not allow to visit login & register pages)
def logged_in_redirect(view_f):
	def wrapper_f(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('scishare:home')
		else:

			return view_f(request, *args, **kwargs)
	return wrapper_f

