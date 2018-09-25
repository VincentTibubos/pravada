from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=40, unique=True)
    tag_line = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_published = models.NullBooleanField()
    publish_date = models.DateTimeField(null=True)
    cover = models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1,default='d')

    def __str__(self):
        return str(self.user.username+': '+self.title)

    def is_published(self):
        return self.status == 'p'

    def is_draft(self):
        return self.status == 'd'

class BaseComment(models.Model):
    text = models.TextField()
    comment_for = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return str(self.username)

class Reply(BaseComment):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Replies"

    def __str__(self):
        return str(self.comment_by)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.title)
