# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from scishare.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect

def home(request):
    context_dict = {'boldmessage': 'context dictionary'}
    return render(request, 'scishare/home.html', context=context_dict)

def register(request):
    #Determines the success status of the registration
    registered = False

    # Extract relevant data from relevant type of request
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # If the above 2 forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save user form data into database, has PW, save user object
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            # Set up the profile pic if the user provided one
            if 'picture' in request.FILES:
                profile.pricture=  request.FILES['picture']

            # Save profile and register user 
            profile.save()
            registered = True
        else:
            # Invalid form(s)
            print(user_form.errors, profile_form.errors)
    else:
        # If not HTTP POST request -> blank forms ready for user input
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request,
        'scishare/register.html',
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        })

def login(request):
    # Extract relevant data from relevant type of request
    if request.method=='POST':
        # Get UN and PW from user login form
        username = request.POST.get('username')
        password = reqest.POST.get('password')
        # Check whether UN+PW combination is valid
        user = authenticate(username = username, password = password)

        # If UN & PW = OK -> User object (True) othwerwise -> None (False)
        if user:

            # Is account active (might not keep this block in the final app version)
            if user.is_active:
                login(request,user)
                return redirect(reverse('scishare:base'))
            else:
                return HttpResponse("You cannot access your accout right now")
        else:
            # User object is None -> we got faulty details
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        # We did not arrive ehre via a HTTP POST
        return render(request,'scishare/login.html')



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




