from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from user.forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

# Homepage
def index(request):
    return render(request, 'homepage/index.html')

# Web Admin
def admin(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'webadmin/index.html')
    else:
        return redirect('/webmaster/login/')

def adminlogin(request):
        error = None
        if request.user.is_authenticated and request.user.is_staff:   #IF USER IS ALREADY LOGGED IN
            return redirect('/webmaster/')
        elif request.method == "POST":      #CHECK LOGIN CREDENTIALS
            form = LoginForm(request.POST)
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
            form = LoginForm()
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

def logout(request):
    if not request.user.is_authenticated:
        return redirect('/home/')
    auth_logout(request)
    return redirect('/login/')

def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    elif request.method == "GET":
        return render(request, 'account/login.html')
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request,user)
                    error= ''
                else:
                    error = " Sorry! Username and Password didn't match, Please try again ! "
        return JsonResponse({'error':error})

def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            error= ''
        else:
            error = " error occured while registering "
        # form=RegisterForm(request.POST)
        # if(form.is_valid()):
        #     form.save()
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password1']
        #     user = authenticate(username=username, password=password)
        #     auth_login(request,user)
        #     error= ''
        # else:
        #     error=request.POST
        return JsonResponse({'error':error})
    return render(request, 'account/register.html')

def profile(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/profile.html')
