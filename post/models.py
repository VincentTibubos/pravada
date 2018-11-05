from django.db import models
from django.contrib.auth.models import User

# Post Models
class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)
    cover = models.ImageField(blank=True, upload_to='storage/uploads/post/cover/%Y/%m/%d/')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1,default='d')
    comments = models.ManyToManyField('Comment',blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user.username+': '+self.title)

    def vote_sum(self):
        return self.upvotes - self.downvotes

    def is_published(self):
        return self.status == 'p'

    def is_draft(self):
        return self.status == 'd'

class Comment(models.Model):
    text = models.TextField(blank=True)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, blank=True, null=True)
    comment_for = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField('Reply',blank=True)

    def __str__(self):
        return str(self.text)

class Reply(models.Model):
    text = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    reply_by = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Replies"

    def __str__(self):
        return str(self.text)

class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)
