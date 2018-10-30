from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from user.forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from . import views

# Model import
from post.models import Post
from user.models import Profile, Publication, Role

# Form import
from post.forms import PostForm

# Create your views here.

# Homepage
def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/webmaster/')
        else:
            return redirect('/home/')
    else:
        return render(request, 'homepage/index.html')

# Web Admin
def admin(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            users = User.objects.all().order_by('date_joined').reverse()[:5]
            posts = Post.objects.all().order_by('created').reverse()[:5]
            publications = Publication.objects.all().order_by('created').reverse()[:5]
            args = {'profile' : users ,'posts' : posts, 'publications' : publications }
            return render(request, 'webadmin/index.html',args)
        else:
            return index(request)
    else:
        return redirect('/webmaster/login/')

def adminlogin(request):
        error = None
        if request.user.is_authenticated:
            if not request.user.is_staff:
                return index(request)
            return redirect('/webmaster/')
        elif request.method == "POST":
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

def admindatabase(request):
    return render(request, 'webadmin/pages/database/index.html')

# Posts
def adminposts(request):
    posts = Post.objects.all()
    args = {'posts' : posts}
    return render(request, 'webadmin/pages/database/posts/index.html',args)

# Publications
def adminpublications(request):
    publications = Publication.objects.all()
    args ={'publications' : publications}
    return render(request, 'webadmin/pages/database/publications/index.html', args)

#Roles
def adminroles(request):
    roles = Role.objects.all()
    args = {'roles' : roles}
    return render(request, 'webadmin/pages/database/roles/index.html', args)

#Users
def adminusers(request):
    users = User.objects.all()
    args = {'profile' : users}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'webadmin/pages/database/users/index.html',args)
    else:
        return render(request, 'webadmin/pages/database/users/index.html',args)

def adminreports(request):
    return render(request, 'webadmin/pages/reports/index.html')

def adminsettings(request):
    return render(request, 'webadmin/pages/settings/index.html')

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
    if request.user.is_authenticated:
        if request.user.is_staff:
            return index(request)
        return render(request, 'account/index.html')
    else:
        return redirect('/login/')

def logout(request):
    if not request.user.is_authenticated:
        return index(request)
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

# Direct Views

# def page_home(request):
