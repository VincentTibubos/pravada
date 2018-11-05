from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Role, Publication
from user.models import Category

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
