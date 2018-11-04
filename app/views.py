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

# Homepage Routes
def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/webmaster/')
        else:
            return redirect('/home/')
    else:
        return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/pages/about.html')

def contact(request):
    return render(request, 'homepage/pages/contact.html')

def help(request):
    return render(request, 'homepage/pages/help.html')

def team(request):
    return render(request, 'homepage/pages/team.html')

def toppublications(request):
    return render(request, 'homepage/pages/top/top-publications.html')

def topwriters(request):
    return render(request, 'homepage/pages/top/top-writers.html')

def writerprofile(request):
    return render(request, 'homepage/pages/writer/writer-profile.html')

def publicationprofile(request):
    return render(request, 'homepage/pages/publication/publication-profile.html')

#Feeds Routes
def hotposts(request):
    return render(request, 'homepage/pages/post/hot-posts.html')

def popularposts(request):
    return render(request, 'homepage/pages/post/popular-posts.html')

def newposts(request):
    return render(request, 'homepage/pages/post/new-posts.html')

# Search Routes
def search(request):
    return render(request, 'search/index.html')

def searchuser(request):
    return render(request, 'search/pages/tag.html')

def searchpublication(request):
    return render(request, 'search/pages/tag.html')

def searchtag(request):
    return render(request, 'search/pages/tag.html')

def searchcategory(request):
    return render(request, 'search/pages/category.html')

# Posts
def post(request):
    return render(request, 'post/pages/post.html')

def writepost(request):
    return render(request, 'post/pages/write-post.html')

def editpost(request):
    return render(request, 'post/pages/edit-post.html')

# Publications
def publication(request):
    return render(request, 'publication/index.html')

def dashboard(request):
    return render(request, 'publication/pages/dashboard/index.html')

def publicationposts(request):
    return render(request, 'publication/pages/posts.html')

def publicationstaff(request):
    return render(request, 'publication/pages/staff.html')

def publicationsettings(request):
    return render(request, 'publication/pages/settings/index.html')

def pubmanagestaff(request):
    return render(request, 'publication/pages/settings/manage-staff.html')

def pubmanageposts(request):
    return render(request, 'publication/pages/settings/manage-posts.html')

# Account Routes
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
        return render(request, 'account/pages/login.html')
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
        return JsonResponse({'error':error})
    return render(request, 'account/pages/register.html')

# User Profile Routes
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/index.html')

def followers(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/followers.html')

def following(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/following.html')

def publications(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/publications.html')

def posts(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/posts.html')

def reputation(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/reputation.html')

def subscriptions(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/subscriptions.html')

# User Settings Routes
def settings(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/index.html')

def publicationsettings(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/publication.html')

def postsettings(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/post.html')

def activitylog(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/activity-log.html')

# Web Admin Routes
def admin(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            users = User.objects.all().order_by('date_joined').reverse()[:5]
            posts = Post.objects.all().order_by('created').reverse()[:5]
            publications = Publication.objects.all().order_by('created').reverse()[:5]
            form = PostForm()
            args = {'profile' : users ,'posts' : posts, 'publications' : publications, 'form' : form }
            if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    print("errors : {}".format(form.errors.as_data()))
            return render(request, 'webadmin/index.html',args)
        else:
            return index(request)
    else:
        return redirect('/webmaster/login/')

def adminlogin(request):
        error = ''
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

# Web Admin Posts Routes
def adminposts(request):
    posts = Post.objects.all()
    args = {'posts' : posts}
    return render(request, 'webadmin/pages/database/posts/index.html',args)

# Web Admin Publications Routes
def adminpublications(request):
    publications = Publication.objects.all()
    args ={'publications' : publications}
    return render(request, 'webadmin/pages/database/publications/index.html', args)

# Web Admin Roles Routes
def adminroles(request):
    roles = Role.objects.all()
    args = {'roles' : roles}
    return render(request, 'webadmin/pages/database/roles/index.html', args)

# Web Admin Users Routes
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
