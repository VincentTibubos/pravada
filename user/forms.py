from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Role, Publication
from user.models import Category, Profile

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

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('user_id','role',)

        widgets = {
            'user_id' : forms.Select(attrs={'class' : 'form-control'}),
            'role' : forms.Select(attrs={'class' : 'form-control'}),
        }

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = (
            'name',
            'description',
            'cover',
            'categories'
        )

        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}),
            'description': forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Description'}),
            'cover': forms.FileInput(attrs={'class' : 'btn btn-primary'}),
            'categories' : forms.SelectMultiple(attrs={'class' : 'form-control'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type','birth_date','city','country','phone')

        widgets = {
            'user_type' : forms.Select(attrs={'class' : 'form-control'}),
            'birth_date' :  forms.DateInput(attrs={'class' : 'form-control', 'value' : date.today()}),
            'city' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'city'}),
            'country' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Country'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Phone'}),
        }

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : 'Password'}))
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : 'Confirm Password'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Last Name'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username'}),
        }
