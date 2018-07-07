from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('',views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/',views.register, name='register'),
    path('userhomepage/',views.userhomepage, name='userhomepage'),
    path('profile/',views.profile, name='profile')
]
