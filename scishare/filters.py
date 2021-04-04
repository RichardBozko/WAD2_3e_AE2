import django_filters

from .models import *

class OrderFilter(django_filters.filterset):
	class Meta:
		model = Order 
		feilds = '__all__'