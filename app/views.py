from django.shortcuts import render,redirect,get_object_or_404
from pprint import pprint
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
from user.forms import RoleForm, PublicationForm, UserForm, ProfileForm, SearchUserForm, SearchPostForm, SearchPageForm

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
    return render(request, 'publication/pages/publication/posts.html')

def publicationstaff(request):
    return render(request, 'publication/pages/publication/staff.html')

def publicationreputation(request):
    return render(request, 'publication/pages/publication/reputation.html')

def publicationsubscribers(request):
    return render(request, 'publication/pages/publication/subscribers.html')

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
    follow = request.user.profile.user_followers.all()
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/following.html',{'follow':follow})

def publications(request):
    roles=Role.objects.filter(user_id=request.user.id)
    pub = Publication.objects.filter(roles=request.user.id)
    # print(pub)
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/publications.html',{'pubs':pub})

def subscriptions(request):
    # pub = Publication.objects.filter(pub_followers=request.user.id)
    # pub = Publication.objects.all()
    user=User.objects.get(id=request.user.id)
    # pprint(Publication.objects.get(id=1).publications.all())# get all subscribers
    # pprint(user.profile.follows.all())# get all subscribers
    pub=user.profile.subscriptions.all()
    if not request.user.is_authenticated:
        return redirect('/login/')
    # return render(request, 'account/pages/profile/subscriptions.html')
    return render(request, 'account/pages/profile/subscriptions.html',{'pubs':pub})

def posts(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/posts.html')

def reputation(request):
    user = Profile.objects.get( user_id = request.user.id)
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/profile/reputation.html',{'user':user})

# User Settings Routes
def settings(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/index.html',{'header':'Profile'})
def settings_account(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/account.html',{'header':'Account'})
def settings_notifications(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/notifications.html',{'header':'Notifications'})
def settings_activity_log(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/settings-list.html',{'header':'Activity Log'})
def settings_posts(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/settings-list.html',{'header':'Posts'})
def settings_publications(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/settings-list.html',{'header':'Publications'})
def settings_blocked_users(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'account/pages/settings/settings-list.html',{'header':'Blocked Users'})
    # User Settings Routes
def getuserdata(request):
    return JsonResponse({'first_name':request.user.first_name,'last_name':request.user.last_name,'email':request.user.email})

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

            # Data
            users = Profile.objects.select_related('user').order_by('auth_user.date_joined').reverse()[:5]
            posts = Post.objects.all().order_by('created').reverse()[:5]
            publications = Publication.objects.all().order_by('created').reverse()[:5]

            # Forms
            postform = PostForm()
            roleform = RoleForm()
            profileform = ProfileForm()
            userform = UserForm()
            publicationform = PublicationForm()
            searchuserform = SearchUserForm()
            searchpostform = SearchPostForm()
            searchpageform = SearchPageForm()

            # Counter
            rolecount = Role.objects.count()
            usercount = Profile.objects.count()
            pagecount = Publication.objects.count()
            postcount = Post.objects.count()

            args = {'profile' : users ,'posts' : posts, 'publications' : publications, 'postform' : postform, 'roleform' : roleform, 'publicationform' : publicationform, 'profileform' : profileform, 'userform' : userform, 'searchuser' : searchuserform, 'searchpost' : searchpostform, 'searchpage' : searchpageform, 'rolec' : rolecount, 'userc' : usercount, 'pagec' : pagecount, 'postc' : postcount,}
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
                elif 'search_user' in request.POST:
                    searchuserform = SearchUserForm(request.POST)
                    if searchuserform.is_valid():
                        try:
                            user = User.objects.get(username = searchuserform.cleaned_data['username'])
                            return redirect('user/'+searchuserform.cleaned_data['username'])
                        except User.DoesNotExist:
                            print('User does not exist')
                    else:
                        print("errors : {}".format(searchuserform.errors.as_data()))
                elif 'search_post' in request.POST:
                    searchpostform = SearchPostForm(request.POST)
                    if searchpostform.is_valid():
                        try:
                            post = Post.objects.get(slug = searchpostform.cleaned_data['slug'])
                            return redirect('post/'+searchuserform.cleaned_data['slug'])
                        except Post.DoesNotExist:
                            print('Post does not exist')
                    else:
                        print("errors : {}".format(searchpostform.errors.as_data()))
                elif 'search_page' in request.POST:
                    searchpageform = SearchPageForm(request.POST)
                    if searchpageform.is_valid():
                        try:
                            page = Publication.objects.get(slug = searchpageform.cleaned_data['slug'])
                            return redirect('page/'+searchpageform.cleaned_data['slug'])
                        except Publication.DoesNotExist:
                            print('Page does not exist')
                    else:
                        print("errors : {}".format(searchpageform.errors.as_data()))
                elif 'dsearch_user' in request.POST:
                    searchuserform = SearchUserForm(request.POST)
                    if searchuserform.is_valid():
                        try:
                            user = User.objects.get(username = searchuserform.cleaned_data['username'])
                            user.delete()
                        except User.DoesNotExist:
                            print('User does not exist')
                    else:
                        print("errors : {}".format(searchuserform.errors.as_data()))
                elif 'dsearch_post' in request.POST:
                    searchpostform = SearchPostForm(request.POST)
                    if searchpostform.is_valid():
                        try:
                            post = Post.objects.get(slug = searchpostform.cleaned_data['slug'])
                            post.delete()
                        except Post.DoesNotExist:
                            print('Post does not exist')
                    else:
                        print("errors : {}".format(searchpostform.errors.as_data()))
                elif 'dsearch_page' in request.POST:
                    searchpageform = SearchPageForm(request.POST)
                    if searchpageform.is_valid():
                        try:
                            page = Publication.objects.get(slug = searchpageform.cleaned_data['slug'])
                            page.delete()
                        except Publication.DoesNotExist:
                            print('Page does not exist')
                    else:
                        print("errors : {}".format(searchpageform.errors.as_data()))
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
    postform = PostForm()
    args = {'posts' : posts, 'postform' : postform}
    if request.method == "POST":
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            postform.save()
        else:
            print("errors : {}".format(postform.errors.as_data()))
    return render(request, 'webadmin/pages/database/posts/index.html',args)

# Web Admin Publications Routes
def adminpublications(request):
    publications = Publication.objects.all()
    publicationform = PublicationForm()
    args ={'publications' : publications, 'publicationform' :publicationform}
    if request.method == "POST":
        publicationform = PublicationForm(request.POST, request.FILES)
        if publicationform.is_valid():
            publicationform.save()
        else:
            print("errors : {}".format(publicationform.errors.as_data()))
    return render(request, 'webadmin/pages/database/publications/index.html', args)

# Web Admin Roles Routes
def adminroles(request):
    roles = Role.objects.all()
    roleform = RoleForm()
    args = {'roles' : roles, 'roleform' : roleform}
    if request.method == "POST":
        roleform = RoleForm(request.POST)
        if roleform.is_valid():
            roleform.save()
        else:
            print("errors : {}".format(roleform.errors.as_data()))
    return render(request, 'webadmin/pages/database/roles/index.html', args)

# Web Admin Users Routes
def adminusers(request):
    users = Profile.objects.select_related('user')
    profileform = ProfileForm()
    userform = UserForm()
    args = {'profile' : users, 'profileform' : profileform, 'userform' : userform}
    if request.method == 'POST':
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
            return redirect('/webmaster/post/'+post.slug)
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
            return redirect('/webmaster/page/'+page.slug)
        else:
            print("errors : {}".format(pageform.errors.as_data()))
    return render(request, 'webadmin/pages/manage/publication/index.html',args)

def manageuser(request, username):
    user = get_object_or_404(User, username = username)
    user2 = Profile.objects.get(user = user.pk)
    profileform = ProfileForm(instance = user2)
    userform = UserForm(instance = user)
    args = {'profileform' : profileform, 'userform' : userform, 'user' : user2, }
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES, instance = user2)
        userform = UserForm(request.POST, instance = user)
        if profileform.is_valid() and userform.is_valid():
            profileform.save()
            userform.save()
            args = {'profileform' : profileform, 'userform' : userform, 'user' : user2, }
            return redirect('/webmaster/user/'+user.username)
        else:
            print("errors : {}".format(profileform.errors.as_data()))
            print("errors : {}".format(userform.errors.as_data()))
    return render(request, 'webadmin/pages/manage/user/index.html',args)

def managerole(request, pk):
    role = get_object_or_404(Role, pk = pk)
    roleform = RoleForm(instance = role)
    args = {'roleform' : roleform}
    if request.method == 'POST':
        roleform = RoleForm(request.POST,instance = role)
        if roleform.is_valid():
            roleform.save()
            return redirect('/webmaster/database/roles/'+str(roleform.cleaned_data['user_id']))
        else:
            print("errors : {}".format(roleform.errors.as_data()))
    return render(request, 'webadmin/pages/manage/role/index.html',args)

def deleteuser(request, username):
    user = get_object_or_404(User, username = username)
    user.delete()
    return redirect('/webmaster/')

def deleterole(request, pk):
    role = get_object_or_404(Role, pk = pk)
    role.delete()
    return redirect('/webmaster/')

def deletepost(request, slug_url):
    post = get_object_or_404(Post, slug = slug_url)
    post.delete()
    return redirect('/webmaster/')

def deletepage(request, slug_url):
    page = get_object_or_404(Publication, slug = slug_url)
    page.delete()
    return redirect('/webmaster/')
