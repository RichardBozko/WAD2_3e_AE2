from django.urls import path
from scishare import views

app_name = 'scishare'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    #path('search_results/', views.search_results, name='search_results'),
    path('categories/', views.categories, name='categories'),
    #path('categories/<category_name>', views.groups, name='groups'),
    path('categories/add_category', views.add_category, name='add_category'),
    #path('categories/<category_name>/add_study', views.add_study, name='add_study'),
    path('most_liked/', views.most_liked, name='most_liked'),
    path('groups/', views.groups, name='groups'),
    path('groups/create_group', views.create_group, name='create_group'),
    #path('groups/<group_name>', views.show_group, name='show_group'),

]