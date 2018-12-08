from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Role, Publication
from user.models import Category, Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
class UsernameChangeForm(forms.ModelForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Old Password'}))

    class Meta:
        model = User
        fields = (
            # 'username'
        )
        widgets = {
            # 'username': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username'})
        }
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password",widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Old Password'}))
    new_password1 = forms.CharField(label="New Password",widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'New Password'}))
    new_password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Confirm Password'}))
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.CharField(max_length=254)
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('user_id','role','publication')

        widgets = {
            'user_id' : forms.Select(attrs={'class' : 'form-control'}),
            'role' : forms.Select(attrs={'class' : 'form-control'}),
            'publication' : forms.Select(attrs={'class' : 'form-control'}),
        }

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = (
            'name',
            'description',
            'cover',
            'categories',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}),
            'description': forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Description'}),
            'cover': forms.FileInput(attrs={'class' : 'btn btn-primary'}),
            'categories' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type','birth_date','city','country','phone','avatar')

        widgets = {
            'user_type' : forms.Select(attrs={'class' : 'form-control'}),
            'birth_date' :  forms.DateInput(attrs={'class' : 'form-control', 'value' : date.today()}),
            'city' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'city'}),
            'country' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Country'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Phone'}),
            'avatar' : forms.FileInput(attrs={'class' : 'btn btn-primary'}),
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

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)

        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Last Name'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username'}),
        }

class RoleEditForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('role',)

        widgets = {
            'role' : forms.Select(attrs={'class' : 'form-control'}),
        }

class SearchUserForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Username'}))

class SearchPageForm(forms.Form):
    slug = forms.CharField(label='slug',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Slug'}))

class SearchPostForm(forms.Form):
    slug = forms.CharField(label='slug',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Slug'}))
