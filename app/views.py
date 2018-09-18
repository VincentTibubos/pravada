from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from user.forms import UserLoginForm

# Create your views here.

# Homepage
def index(request):
    return render(request, 'homepage/index.html')

# Web Admin
def admin(request):
    if request.user.is_authenticated:
        return render(request, 'webadmin/index.html')
    else:
        return redirect('/webmaster/login/')

def adminlogin(request):
        error = None
        if request.user.is_authenticated:   #IF USER IS ALREADY LOGGED IN
            return redirect('/webmaster/')
        elif request.method == "POST":      #CHECK LOGIN CREDENTIALS
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request,user)
                    return redirect('/webmaster/')
                else:
                    error = " Sorry! Username and Password didn't match, Please try again ! "
        else:
            form = UserLoginForm()
        return render(request, 'webadmin/account/login.html', {"form":form, "error":error})

def adminlogout(request):
    auth_logout(request)
    return redirect('/webmaster/login/')

# Posts
def article(request):
    return render(request, 'post/article.html')

def category(request):
    return render(request, 'post/category.html')

def search(request):
    return render(request, 'post/search.html')

# Publications
def publication(request):
    return render(request, 'publication/index.html')

def dashboard(request):
    return render(request, 'publication/dashboard.html')

# Account
def home(request):
    return render(request, 'account/index.html')

def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def profile(request):
    return render(request, 'account/profile.html')
