from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='title',)
    slug = forms.CharField(label='slug',)
    text = forms.CharField(label='text',)
    timestamp = forms.DateField(label='timestamp',)
    tag_line = forms.CharField(label='tagline',)
    is_published = forms.NullBooleanField()
    publish_date = forms.DateTimeField()
