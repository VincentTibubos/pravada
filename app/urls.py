from django.urls import path
from django.contrib import admin

from . import views

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

    # Web Admin CRUD
    path('webmaster/database/',views.admindatabase, name='index'),
    path('webmaster/database/posts/',views.adminposts, name='index'),
    path('webmaster/database/publications/',views.adminpublications, name='index'),
    path('webmaster/database/roles/',views.adminroles, name='index'),
    path('webmaster/database/users/',views.adminusers, name='index'),

    # Account Views
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register, name='register'),
    path('home/',views.home, name='home'),
    path('settings/',views.profile, name='profile'), #update
    path('submit/',views.profile, name='profile'),
    path('search/',views.search, name='search'),

    # Account Profile Views
    path('profile/',views.profile, name='profile'),
    path('profile/posts/',views.profile, name='profile'), #update
    path('profile/posts/draft/',views.profile, name='profile'), #update
    path('profile/posts/published/',views.profile, name='profile'), #update
    path('profile/publications/',views.profile, name='profile'), #update

    # Post Views
    path('post/',views.article, name='article'), #replace article to post
    path('tag/',views.category, name='category'), #replace tag

    # Public Publication Views
    path('publication/',views.publication, name='publication'),
    path('publication/posts/',views.dashboard, name='dashboard'),
    path('publication/staff/',views.dashboard, name='dashboard'), # update
    path('publication/category/',views.dashboard, name='dashboard'), # update

    # Publication Admin Views
    path('publication/dashboard/',views.dashboard, name='dashboard'),
    path('publication/manage/',views.dashboard, name='dashboard'), # Pub Setttings Update
    path('publication/manage/posts/',views.dashboard, name='dashboard'),
    path('publication/manage/staff/',views.dashboard, name='dashboard'),

    # Feeds (Please Update!!)
    path('subscriptions/',views.home, name='new'),
    path('new/',views.home, name='new'),
    path('hot/',views.home, name='new'),
    path('popular/',views.home, name='new'),

    # Top
    path('top/',views.home, name='new'),
    path('top/publications/',views.home, name='new'),
    path('top/writers/',views.home, name='new'),
]
