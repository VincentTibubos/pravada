from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect ('app:home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html',{ 'form':form })

def register(request):
    return render(request, 'account/register.html')

def home(request):
    return render(request, 'account/home.html')
