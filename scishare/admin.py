# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from scishare.models import UserProfile, Category, Study, Group

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Study)
admin.site.register(Group)
#admin.site.register(User)	
