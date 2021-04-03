# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from scishare.forms import UserCreateForm, UserUpdateForm, CategoryForm, StudyForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log_in
from django.urls import reverse
from django.shortcuts import redirect
#from django.contrib import send_mail
#from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from django_email_verification import send_mail
from django.contrib import messages
from scishare.models import Category, Study, UserProfile
from django.contrib.auth.decorators import login_required

def home(request):
    context_dict = {'boldmessage': 'context dictionary'}
    return render(request, 'scishare/home.html', context=context_dict)
'''
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
        'registration/registration_complete.html',
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
        password = request.POST.get('password')
        # Check whether UN+PW combination is valid
        user = authenticate(username = username, password = password)

        # If UN & PW = OK -> User object (True) othwerwise -> None (False)
        if user:

            # Is account active (might not keep this block in the final app version)
            if user.is_active:
                login(request,user)
                return redirect(reverse('scishare:home'))
            else:
                return HttpResponse("You cannot access your account right now")
        else:
            # User object is None -> we got faulty details
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        # We did not arrive ehre via a HTTP POST
        return render(request,'registration/login.html')
'''

def register(request):
    if request.user.is_authenticated:
        return redirect('scishare:home')
    else:
        rform = UserCreateForm()

        if request.method == "POST":
            rform = UserCreateForm(request.POST)
            if rform.is_valid():
                user = rform.save()

                username = rform.cleaned_data.get('username')

                UserProfile.objects.create(user = user)
                messages.success(request, f'Account created for {user}.')


                return redirect('scishare:login')

        context = {'rform':rform}
        return render(request, 'registration/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('scishare:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user:
                log_in(request,user)
                return redirect('scishare:home')
            else:
                messages.info(request, 'Username or password incorrect.')
        else:
            return render(request,'registration/login.html')
    


def userAccount(request):

    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, request.FILES, instance = request.user)
        if uform.is_valid():
            uform.save()
    else:
        uform = UserUpdateForm(instance = request.user)
            
    context = {'uform' : uform}
    return render(request, 'registration/user.html', context)

#following make visible only after log in

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('scishare:home'))

#@login_required
def search_results(request):
    return HttpResponse("show search results")

#@login_required
def categories(request):
    obj = Category.objects.all()

    context_dict = {}
    context_dict['categories'] = obj
    return render(request, 'scishare/categories.html', context=context_dict)

#@login_required
def study_list(request, id):
    obj = get_object_or_404(Category, pk = id)
    
    return render(request, 'scishare/study_list.html', {'obj':obj})

#@login_required
def add_category(request):
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the home page.
            return redirect('/scishare/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'scishare/add_category.html', {'form': form})

#@login_required
def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        studies = Study.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['studies'] = studies
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['studies'] = None
        # Go render the response and return it to the client.
    return render(request, 'scishare/category.html', context=context_dict)

#@login_required
def add_study(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    
    # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/scishare/')
    
    form = StudyForm()
    if request.method == 'POST':
        form = StudyForm(request.POST)
            
        if form.is_valid():
            if category:
                study = form.save(commit=False)
                study.category = category
                study.save()
                return redirect(reverse('scishare:show_category',
                kwargs={'category_name_slug':
                category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'scishare/add_study.html', context=context_dict)

#@login_required
def most_liked(request):
    study_list = Study.objects.order_by('-up_votes')[:5]
    
    context_dict = {}
    context_dict['studies'] = study_list
    
    return render (request, 'scishare/most_liked.html', context=context_dict)

#@login_required
def groups(request):
    obj  = Group.object.all()
    
    return render (request, 'scishare/groups.html', {'obj':obj})

#@login_required
def create_group(request):
    form = GroupForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the home page.
            return redirect('/scishare/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'scishare/create_group.html', {'form': form})

#@login_required
def group_list(request, id):
    obj = get_object_or_404(Group, pk = id)
    
    return render(request, 'group_list.html', {'obj':obj})
  




