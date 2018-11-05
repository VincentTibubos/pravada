from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Reply, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','slug','tags','text','status','cover')

        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}),
            'author': forms.Select(attrs={'class' : 'form-control'}),
            'slug': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Slug'}),
            'text': forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Text'}),
            'status': forms.Select(attrs={'class' : 'form-control'}),
            'cover': forms.FileInput(attrs={'class' : 'btn btn-primary'}),
            'tags' :  forms.SelectMultiple(attrs={'class' : 'form-control'}),
        }


class CommentForm(forms.Form):
    comment_for = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.CharField(label='text',)
    created_on = forms.DateField(label='created_on',)
    username = forms.CharField(label='username',)

class ReplyForm(forms.Form):
    comment_for = forms.IntegerField(widget=forms.HiddenInput())
    comment_by = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.CharField(label='text',)
    created_on = forms.DateField(label='created_on',)
    username = forms.CharField(label='username',)
