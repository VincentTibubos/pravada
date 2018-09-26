from django import forms
from .models import Post, BaseComment, Reply, Category

class PostForm(forms.Form):
    title = forms.CharField(label='title',)
    slug = forms.CharField(label='slug',)
    text = forms.CharField(label='text',)
    timestamp = forms.DateField(label='timestamp',)
    tag_line = forms.CharField(label='tagline',)
    is_published = forms.NullBooleanField()
    publish_date = forms.DateTimeField()

class CommentForm(forms.Form):
    comment_for = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.TextField()
    created_on = forms.DateField(label='created_on',)
    username = forms.CharField(label='username',)

class ReplyForm(forms.Form):
    comment_for = forms.IntegerField(widget=forms.HiddenInput())
    comment_by = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.TextField()
    created_on = forms.DateField(label='created_on',)
    username = forms.CharField(label='username',)
