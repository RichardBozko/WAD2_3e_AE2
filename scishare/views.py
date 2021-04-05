# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
#from scishare.forms import UserCreateForm, UserUpdateForm, CategoryForm, StudyForm
from django.shortcuts import render, get_object_or_404, HttpResponse
from scishare.forms import UserCreateForm, UserUpdateForm, CategoryForm, StudyForm, GroupForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log_in
from django.urls import reverse
from django.shortcuts import redirect
#from django.contrib import send_mail
#from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from django_email_verification import send_mail
from django.contrib import messages
from scishare.models import Category, Study, UserProfile, Order,Group
#from scishare.models import Category, Study, UserProfile, Group
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .decorators import user_permissions, logged_in_redirect

def home(request):
    context={}
    return render(request, 'scishare/home.html', context=context)
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
@logged_in_redirect
def register(request):
    # If user is logged-in -> redirect to homepage
    # Extract relevant data from relevant type of request
    rform = UserCreateForm()
    if request.method == "POST":
        rform = UserCreateForm(request.POST)
        if rform.is_valid():
            user = rform.save()

            # Construct a user object from provided data
            username = rform.cleaned_data.get('username')
            email = rform.cleaned_data.get('email')
            UserProfile.objects.create(user = user, username = username, email = email)
            messages.success(request, f'Account created for {user}.')
            # Allow freshly registered user to log in
            return redirect('scishare:login')

# if GET -> return the page 
    context = {'rform':rform}
    return render(request, 'registration/register.html', context)

@logged_in_redirect
def login(request):
    # If user is logged-in -> redirect to homepage
    # Extract relevant data from relevant type of request
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check whether UN+PW combination is valid
        user = authenticate(request, username = username, password = password)
        if user:
            # log the user in if ^ is valid
            log_in(request,user)
            return redirect('scishare:home')
        else:
            messages.info(request, 'Username or password incorrect.')
            # pass a message to login.html that ^
    # refresh the page + do ^
    return render(request,'registration/login.html')
    

@login_required
def userAccount(request):
    # Check whether there is a user logged in whose account we are to inspect
    if request.user.is_authenticated:
        # If this is not a refresh following a user info change, 
        # get the relevant data if the user changed any
        uform = UserUpdateForm(instance = request.user)
        if request.method == 'POST':
            # if POST (if this is a page refresh following user info changes)
            # gather data from page request  
            uform = UserUpdateForm(request.POST, request.FILES, instance = request.user.userprofile)
            if uform.is_valid():
                uform.save()
                # use this data to update user info
        context = {'uform' : uform}
        return render(request, 'registration/user.html', context)
    else:
        # If logged in -> redirect to homepage
        return redirect(reverse('scishare:home'))

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('scishare:home'))

@login_required
def search_results(request):
    search_study = request.GET.get('search')
    if search_study:
        studies = Study.objects.filter(Q(title__icontains=search_study) | Q(category__name__icontains=search_study))
    else:
        studies = None
    # if no studies were found
    if not bool(studies):
        studies = None

    context = {'studies': studies, 'search': search_study}
    return render(request, 'scishare/search_results.html', context=context)

@login_required
def vote(request,id,method):
    if request.method=="POST":
      try:
       study_obj=Study.objects.get(id=id)
       if method=="voted":
           study_obj.up_votes=study_obj.up_votes+1
       else:
           study_obj.down_votes=study_obj.down_votes+1
       study_obj.save()
       return JsonResponse({"code":200,"msg":"Successful！"})
      except:
          return JsonResponse({"code": 200, "msg": "Failed"})






@login_required
def categories(request):
    obj = Category.objects.all()

    context_dict = {}
    context_dict['categories'] = obj
    return render(request, 'scishare/categories.html', context=context_dict)

@user_permissions()
@login_required
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
            return redirect('/scishare/categories')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'scishare/add_category.html', {'form': form})

@login_required
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

@login_required
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

@login_required
def most_liked(request):
    study_list = Study.objects.order_by('-up_votes')[:5]
    
    context_dict = {}
    context_dict['studies'] = study_list
    
    return render (request, 'scishare/most_liked.html', context=context_dict)

@login_required
def groups(request):
    # select groups the user is a member of
    my_groups = Group.objects.filter(members=request.user)
    return render(request, 'scishare/groups.html', {'groups': my_groups})

@login_required
def add_group(request):
    form = GroupForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = GroupForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the home page.
            return redirect('/scishare/groups')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'scishare/add_group.html', {'form': form})

@login_required
def show_group(request, group_name_slug):
    context_dict = {}
    try:
        group = Group.objects.get(group_slug=group_name_slug)
        context_dict['group'] = group
        context_dict['studies'] = group.group_studies.all()
        context_dict['members'] = group.members.all()
    except Group.DoesNotExist:
        context_dict['group'] = None
        # Go render the response and return it to the client.
    return render(request, 'scishare/group.html', context=context_dict)

@login_required
def add_study_to_group(request):
    context_dict = {}
    selected_study = Study.objects.get(id=request.GET.get('study'))
    my_groups = Group.objects.filter(members=request.user)
    context_dict['studies'] = selected_study
    context_dict['my_groups'] = my_groups
    return render(request, 'scishare/add_study_to_group.html', context=context_dict)


@login_required
def add_selected_study_to_group(request):
    context_dict = {}
    if request.method == 'POST':
        groups = request.POST.getlist('groups')
        study_id = request.POST.get('study')
        selected_study = Study.objects.get(id=study_id)
        context_dict['my_groups'] = []
        for g in groups:
            group = Group.objects.get(group_slug=g)
            group.group_studies.add(selected_study)
            context_dict['my_groups'].append(group)
        context_dict['study'] = selected_study
        return render(request, 'scishare/successfully_added.html', context=context_dict)
  




