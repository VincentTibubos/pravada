from django.db import models
from django.conf import settings

class User(models.Model):
    email = models.CharField(max_length=120, null=False, blank=False)
    password = models.CharField(max_length=120, null=False, blank=False)
    f_name = models.CharField(max_length=120, null=False, blank=False)
    l_name = models.CharField(max_length=120, null=False, blank=False)
    reputation = models.IntegerField(default=1, null=False, blank=False)
