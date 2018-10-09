from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [

    # Homepage View
    path('',views.index, name='index'),

    # Web Admin
    path('webmaster/',views.admin, name='index'),
    path('webmaster/login/',views.adminlogin, name='index'),
    path('webmaster/logout/',views.adminlogout, name='index'),
    path('webmaster/reports/',views.adminreports, name='index'),
    path('webmaster/settings/',views.adminsettings, name='index'),

    # Account Views
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register, name='register'),
    path('home/',views.home, name='home'),
    path('profile/',views.profile, name='profile'),

    # Post Views
    path('article/',views.article, name='article'),
    path('category/',views.category, name='category'),
    path('search/',views.search, name='search'),

    # Publication Views
    path('publication/',views.publication, name='publication'),
    path('publication/dashboard/',views.dashboard, name='dashboard'),

]
