# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context_dict = {'boldmessage': 'context dictionary'}
    return render(request, 'scishare/home.html', context=context_dict)

def register(request):
    return HttpResponse("Register page.")

def login(request):
    return HttpResponse("Login page.")

#following make visible only after log in
def search_results(request):
    return HttpResponse("show search results")

def categories(request):
    return HttpResponse("list of categories")

def add_category(request):
    return HttpResponse("add category form")

def show_category(request):
    return HttpResponse("show category studies")

def add_study(request):
    return HttpResponse("add study")

def most_liked(request):
    return HttpResponse("list of most liked studies")

def groups(request):
    return HttpResponse("list of groups")

def create_group(request):
    return HttpResponse("create a group")

def show_group(request):
    return HttpResponse("show list of pages of the group")




