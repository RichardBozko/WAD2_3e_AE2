from django.urls import path
from scishare import views
from django.contrib.auth import views as auth_views

app_name = 'scishare'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search_results/', views.search_results, name='search_results'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('categories/add_category', views.add_category, name='add_category'),
    path('categories/<category_name_slug>/add_study', views.add_study, name='add_study'),
    path('most_liked/', views.most_liked, name='most_liked'),
    path('groups/', views.groups, name='groups'),
    path('groups/add_group', views.add_group, name='add_group'),
    path('groups/<group_name_slug>', views.show_group, name='show_group'),
    #path('reset_password/', auth_views.PasswordResetViews.as_view()),
    #path('user/<str:pk>/', views.user, name = 'user'),
    path('user/', views.userAccount, name = 'userAccount'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),


]