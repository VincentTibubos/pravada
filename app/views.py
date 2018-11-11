from django.shortcuts import render,redirect,get_object_or_404

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
from user.forms import RoleForm, PublicationForm, UserForm, ProfileForm

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

def getstarted(request):
    return render(request, 'homepage/pages/get-started.html')

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
    return render(request, 'post/index.html')

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
        username = request.POST['username']
        password = request.POST['password']
        p_error=None
        u_error=None
        error="Sorry! Username and Password didn't match, Please try again ! "
        if len(username) < 5:
            u_error='Username must have atlest 5 characters'
        if len(password) < 8:
            p_error='Password must have atlest 8 characters'
        if p_error==None and u_error==None:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request,user)
                    error= None
        return JsonResponse({'p_error':p_error,'u_error':u_error,'error':error})

def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        u_error=None
        e_error=None
        l_error=None
        f_error=None
        p_error=None
        cp_error=None
        error='Sorry! Username or Email already been used'
        if len(username)<5:
            u_error='Username must have atleast 5 characters'
        elif User.objects.filter(username=username).exists():
            u_error='Username already exist'
        if len(email)==0:
            e_error='Email required'
        elif '@' in email:
            if(email.find('@')>=(len(email)-1)):
                e_error='Invalid email'
            elif User.objects.filter(email=email).exists():
                e_error='email already exist'
        else:
            e_error="'@' missing in email"
        if len(last_name)==0:
            l_error="Last name required"
        if len(first_name)==0:
            f_error="First name required"
        if len(password)<8:
            p_error="Password must be atleast 8 characters"
        if len(cpassword)<8:
            cp_error="Confirm Password must be atleast 8 characters"
        elif cpassword != password:
            cp_error="Password mismatch"
        if u_error == None and e_error == None and f_error == None and l_error == None and p_error == None and cp_error == None:
            user=User.objects.create_user(username,email,password)
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user) #uncomment
                error= None
        return JsonResponse({'error':error,'u_error':u_error,'e_error':e_error,'l_error':l_error,'f_error':f_error,'p_error':p_error,'cp_error':cp_error})
    return render(request, 'account/pages/register.html')

# User Profile Routes
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/index.html')

def followers(request):
    user = Profile.objects.get( user_id = request.user.id)
    follow = Profile.objects.filter(user_followers=user.id)
    # print(profile)
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/followers.html',{'follow':follow})

def following(request):
    user = Profile.objects.get( user_id = request.user.id)
    follow = user.user_followers.all()
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/following.html',{'follow':follow})

def publications(request):
    profile = Profile.objects.get( user_id = request.user.id)
    pub = Publication.objects.filter(pub_followers=profile.id)
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/publications.html',{'pubs':pub})

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
            # users = User.objects.all().order_by('date_joined').reverse()[:5]
            users = Profile.objects.select_related('user').order_by('auth_user.date_joined').reverse()[:5]
            posts = Post.objects.all().order_by('created').reverse()[:5]
            publications = Publication.objects.all().order_by('created').reverse()[:5]
            postform = PostForm()
            roleform = RoleForm()
            profileform = ProfileForm()
            userform = UserForm()
            publicationform = PublicationForm()
            args = {'profile' : users ,'posts' : posts, 'publications' : publications, 'postform' : postform, 'roleform' : roleform, 'publicationform' : publicationform, 'profileform' : profileform, 'userform' : userform }
            if request.method == "POST":
                if 'add_post' in request.POST:
                    postform = PostForm(request.POST, request.FILES)
                    if postform.is_valid():
                        postform.save()
                    else:
                        print("errors : {}".format(postform.errors.as_data()))
                elif 'add_role' in request.POST:
                    roleform = RoleForm(request.POST)
                    if roleform.is_valid():
                        roleform.save()
                    else:
                        print("errors : {}".format(roleform.errors.as_data()))
                elif 'add_publication' in request.POST:
                    publicationform = PublicationForm(request.POST, request.FILES)
                    if publicationform.is_valid():
                        publicationform.save()
                    else:
                        print("errors : {}".format(publicationform.errors.as_data()))
                elif 'add_user' in request.POST:
                    profileform = ProfileForm(request.POST)
                    userform = UserForm(request.POST)
                    if profileform.is_valid() and userform.is_valid():
                        profile = profileform.save(commit=False)
                        user = userform.save()
                        profile.user = user
                        profile.save()
                    else:
                        print("errors : {}".format(profileform.errors.as_data()))
                        print("errors : {}".format(userform.errors.as_data()))
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
    postform = PostForm()
    roleform = RoleForm()
    profileform = ProfileForm()
    userform = UserForm()
    publicationform = PublicationForm()
    args = {'postform' : postform, 'roleform' : roleform, 'publicationform' :publicationform, 'profileform' : profileform, 'userform' : userform }
    if request.method == "POST":
        if 'add_post' in request.POST:
            postform = PostForm(request.POST, request.FILES)
            if postform.is_valid():
                postform.save()
            else:
                print("errors : {}".format(postform.errors.as_data()))
        elif 'add_role' in request.POST:
            roleform = RoleForm(request.POST)
            if roleform.is_valid():
                roleform.save()
            else:
                print("errors : {}".format(roleform.errors.as_data()))
        elif 'add_publication' in request.POST:
            publicationform = PublicationForm(request.POST, request.FILES)
            if publicationform.is_valid():
                publicationform.save()
            else:
                print("errors : {}".format(publicationform.errors.as_data()))
        elif 'add_user' in request.POST:
            profileform = ProfileForm(request.POST)
            userform = UserForm(request.POST)
            if profileform.is_valid() and userform.is_valid():
                profile = profileform.save(commit=False)
                user = userform.save()
                profile.user = user
                profile.save()
            else:
                print("errors : {}".format(profileform.errors.as_data()))
                print("errors : {}".format(userform.errors.as_data()))
    return render(request, 'webadmin/pages/database/index.html',args)

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
    users = Profile.objects.select_related('user').order_by('auth_user.date_joined').reverse()[:5]
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

def managepost(request, slug_url):
    post = get_object_or_404(Post, slug = slug_url)
    postform = PostForm(instance = post)
    args = {'postform' : postform, 'post' : post}
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            args = {'postform' : postform, 'post' : post}
        else:
            print("errors : {}".format(postform.errors.as_data()))
    return render(request, 'webadmin/pages/manage/index.html',args)

def managepage(request, slug_url):
    page = get_object_or_404(Publication, slug = slug_url)
    pageform = PublicationForm(instance = page)
    args = {'publicationform' : pageform, 'page' : page}
    if request.method == 'POST':
        pageform = PublicationForm(request.POST, request.FILES, instance=page)
        if pageform.is_valid():
            pageform.save()
            args = {'publicationform' : pageform, 'page' : page}
        else:
            print("errors : {}".format(pageform.errors.as_data()))
    return render(request, 'webadmin/pages/manage/publication/index.html',args)

def manageuser(request, slug_url):
    user = get_object_or_404(Profile, slug = slug_url)
    profileform = ProfileForm(instance = user)
    userform = UserForm(instance = user.user)
    args = {'profileform' : profileform, 'userform' : userform, 'user' : user, }
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES, instance = user)
        userform = UserForm(request.POST, instance = user.user)
        if profileform.is_valid() and userform.is_valid():
            profileform.save()
            userform.save()
            args = {'profileform' : profileform, 'userform' : userform, 'user' : user, }
        else:
            print("errors : {}".format(profileform.errors.as_data()))
            print("errors : {}".format(userform.errors.as_data()))
    return render(request, 'webadmin/pages/manage/user/index.html',args)
