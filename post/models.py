from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tag_line = models.CharField(max_length=100, null=True)
    recent_comments = models.IntegerField(default=5, null=True)
    is_published = models.BooleanField(default=True, null=True)
    publish_date = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.user.username+' '+self.title)

class BaseComment(models.Model):
    text = models.TextField()
    comment_for = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return str(self.username)

class Reply(BaseComment):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, blank=True, null=True)

    def __str__(self):
        return str(self.comment_by)
