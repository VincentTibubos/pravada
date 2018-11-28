from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'app'
urlpatterns = [

    # Homepage View
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('help/',views.help, name='help'),
    path('team/',views.team, name='team'),
    path('getstarted/',views.getstarted, name='team'),

    # Search View
    path('search/user/',views.searchuser, name='searchuser'),
    path('search/publication/',views.searchpublication, name='searchpublication'),
    path('search/tag/',views.searchtag, name='searchtag'),
    path('search/category/',views.searchcategory, name='searchcategory'),

    # Profile View
    path('writer/profile/',views.writerprofile, name='writerprofile'),
    path('publication/profile/',views.publicationprofile, name='publicationprofile'),

    # Feeds
    path('new/',views.newposts, name='newposts'),
    path('hot/',views.hotposts, name='hotposts'),
    path('popular/',views.popularposts, name='popularposts'),

    # Top
    path('top/publications/',views.toppublications, name='toppublications'),
    path('top/writers/',views.topwriters, name='topwriters'),

    # Account Views
    path('home/',views.home, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register, name='register'),

    # Account Profile Views
    path('profile/',views.profile, name='profile'),
    path('getuserdata',views.getuserdata, name='getuserdata'),
    path('profile/posts/',views.posts, name='posts'),
    path('profile/publications/',views.publications, name='publications'),
    path('profile/activitylog/',views.activitylog, name='activitylog'),
    path('profile/followers/',views.followers, name='followers'),
    path('profile/following/',views.following, name='following'),
    path('profile/subscriptions/',views.subscriptions, name='subscriptions'),
    path('profile/reputation/',views.reputation, name='reputation'),

    # Account Profile Settings
    path('settings/profile/',views.settings, name='settings'),
    path('settings/account/',views.settings_account, name='settings_account'),
    path('settings/account/delete_account/',views.delete_account, name='delete_account'),
    path('settings/notifications/',views.settings_notifications, name='settings_notifications'),
    path('settings/activity-log/',views.settings_activity_log, name='settings_activity_log'),
    path('settings/publications/',views.settings_publications, name='settings_publications'),
    path('settings/posts/',views.settings_posts, name='settings_posts'),
    path('settings/blocked-users/',views.settings_blocked_users, name='settings_blocked_users'),

    # Post Views
    path('post/',views.post, name='post'),
    path('post/write/',views.writepost, name='writepost'),
    path('post/edit/',views.editpost, name='editpost'),

    # Public Publication Views
    path('publication/',views.publication, name='publication'),
    path('publication/posts/',views.publicationposts, name='publicationposts'),
    path('publication/staff/',views.publicationstaff, name='publicationstaff'),
    path('publication/reputation/',views.publicationreputation, name='publicationstaff'),
    path('publication/subscribers/',views.publicationsubscribers, name='publicationstaff'),

    # Publication Admin Views
    path('publication/dashboard/',views.dashboard, name='dashboard'),
    path('publication/manage/',views.publicationsettings, name='publicationsettings'),
    path('publication/manage/posts/',views.pubmanageposts, name='pubmanageposts'),
    path('publication/manage/staff/',views.pubmanagestaff, name='pubmanagestaff'),

    # Web Admin
    path('webmaster/',views.admin, name='index'),
    path('webmaster/login/',views.adminlogin, name='adminlogin'),
    path('webmaster/logout/',views.adminlogout, name='adminlogout'),
    path('webmaster/reports/',views.adminreports, name='adminreports'),
    path('webmaster/settings/',views.adminsettings, name='adminsettings'),

    # Web Admin CRUD
    path('webmaster/database/',views.admindatabase, name='admindatabase'),
    path('webmaster/database/posts/',views.adminposts, name='adminposts'),
    path('webmaster/database/publications/',views.adminpublications, name='adminpublications'),
    path('webmaster/database/roles/',views.adminroles, name='adminroles'),
    path('webmaster/database/users/',views.adminusers, name='adminusers'),

    # Web Admin Dashboard Manage
    path('webmaster/post/<str:slug_url>/', views.managepost, name='managepost'),
    path('webmaster/publication/<str:slug_url>/', views.managepage, name='managepage'),
    path('webmaster/user/<str:username>/', views.manageuser, name='manageuser'),

    # Web Admin Dashboard Delete
    path('webmaster/post/<str:slug_url>/delete', views.deletepost, name='managepost'),
    path('webmaster/publication/<str:slug_url>/delete', views.deletepage, name='managepage'),
    path('webmaster/user/<str:username>/delete', views.deleteuser, name='deleteuser'),

    # Web Admin Database Manage
    path('webmaster/database/posts/<str:slug_url>/', views.managepost, name='managepost'),
    path('webmaster/database/publications/<str:slug_url>/', views.managepage, name='managepage'),
    path('webmaster/database/users/<str:username>/', views.manageuser, name='manageuser'),
    path('webmaster/database/roles/<str:pk>/', views.managerole, name='managerole'),

    # Web Admin Database Manage
    path('webmaster/database/posts/<str:slug_url>/delete', views.deletepost, name='deletepost'),
    path('webmaster/database/publications/<str:slug_url>/delete', views.deletepage, name='deletepage'),
    path('webmaster/database/users/<str:username>/delete', views.deleteuser, name='deleteuser'),
    path('webmaster/database/roles/<str:pk>/delete', views.deleterole, name='deleterole'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
