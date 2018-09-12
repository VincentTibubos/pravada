from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    reputation = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username)

class Organization(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Role(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=120,default='Staff', null=False, blank=False)

    def __str__(self):
        return str(self.org_id)
