from django.http import HttpResponse
from django.shortcuts import redirect

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
