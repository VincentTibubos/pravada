from django.urls import path
from django.contrib import admin

from . import views

app_name = 'app'
urlpatterns = [

    # Homepage View
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='newposts'),
    path('help/',views.help, name='help'),
    path('team/',views.team, name='team'),

    # Profile View
    path('writer/profile/',views.writerprofile, name='newposts'),
    path('publication/profile/',views.publicationprofile, name='newposts'),

    # Feeds
    path('new/',views.newposts, name='newposts'),
    path('hot/',views.hotposts, name='hotposts'),
    path('popular/',views.popularposts, name='popularposts'),

    # Top
    path('top/publications/',views.toppublications, name='new'),
    path('top/writers/',views.topwriters, name='new'),

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
    path('home/',views.home, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register, name='register'),
    # path('submit/',views.profile, name='profile'),
    # path('search/',views.search, name='search'),

    # Account Profile Views
    path('profile/',views.profile, name='profile'),
    path('profile/settings/',views.settings, name='settings'),
    path('profile/posts/',views.posts, name='posts'),
    path('profile/publications/',views.publications, name='publications'),
    path('profile/activitylog/',views.activitylog, name='activitylog'),
    path('profile/followers/',views.followers, name='followers'),
    path('profile/following/',views.following, name='following'),
    path('profile/subscriptions/',views.subscriptions, name='subscriptions'),

    # Post Views
    path('post/',views.article, name='article'), #replace article to post
    path('tag/',views.category, name='category'), #replace tag

    # Public Publication Views
    path('publication/',views.publication, name='publication'),
    # path('publication/posts/',views.dashboard, name='dashboard'),
    # path('publication/staff/',views.dashboard, name='dashboard'), # update
    # path('publication/category/',views.dashboard, name='dashboard'), # update

    # Publication Admin Views
    path('publication/dashboard/',views.dashboard, name='dashboard'),
    # path('publication/manage/',views.dashboard, name='dashboard'), # Pub Setttings Update
    # path('publication/manage/posts/',views.dashboard, name='dashboard'),
    # path('publication/manage/staff/',views.dashboard, name='dashboard'),
]
