from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

# Homepage
def index(request):
    return render(request, 'homepage/index.html')

# Posts
def article(request):
    return render(request, 'post/article.html')

def category(request):
    return render(request, 'post/category.html')

def search(request):
    return render(request, 'post/search.html')

# tinyMCE

# Publications
def publication(request):
    return render(request, 'publication/index.html')

def dashboard(request):
    return render(request, 'publication/dashboard.html')

# Account
def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def home(request):
    return render(request, 'account/index.html')

def profile(request):
    return render(request, 'account/profile.html')
