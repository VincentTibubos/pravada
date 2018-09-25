from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='username',)
    password = forms.CharField(label='password', widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=30,)
    last_name=forms.CharField(max_length=30)
    email=forms.CharField(max_length=254)
    
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')
