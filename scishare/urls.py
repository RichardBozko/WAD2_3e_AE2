from django.urls import path
from scishare import views
from django.contrib.auth import views as auth_views

app_name = 'scishare'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    #path('search_results/', views.search_results, name='search_results'),
    path('categories/', views.categories, name='categories'),
    #path('categories/<category_name>', views.groups, name='groups'),
    path('categories/add_category', views.add_category, name='add_category'),
    #path('categories/<category_name>/add_study', views.add_study, name='add_study'),
    path('most_liked/', views.most_liked, name='most_liked'),
    path('groups/', views.groups, name='groups'),
    path('groups/create_group', views.create_group, name='create_group'),
    #path('groups/<group_name>', views.show_group, name='show_group'),
   # path('reset_password/', auth_views.PasswordResetViews.as_view()),
    #path('user/<str:pk>/', views.user, name = 'user'),
    path('user/', views.userAccount, name = 'userAccount'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name = 'reset_password'),

    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    # uid64 & token as per official Django documentation; former -> encode in b64
    # latter token to check validity of PW
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),




]