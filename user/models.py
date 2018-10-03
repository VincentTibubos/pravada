from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    USER_TYPES = (
        ('u', 'User'),
        ('w', 'Webmaster')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='u')
    avatar = models.ImageField(blank=True, upload_to='uploads/avatar/%Y/%m/%d/')
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    reputation = models.IntegerField(default=1)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        if self.id and self.avatar:
            current_avatar = Profile.objects.get(pk=self.id).avatar
            if current_avatar != self.avatar:
                current_avatar.delete()
        super(Profile, self).save(*args, **kwargs)

    def is_user(self):
        return self.user_type == 'u'

    def is_webmaster(self):
        return self.user_type == 'w'

class Publication(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Role(models.Model):
    pub_id = models.ForeignKey(Publication, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=120,default='Staff', null=False, blank=False)

    def __str__(self):
        return str(self.pub_id)
