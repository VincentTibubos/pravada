from django.db import models
from django.conf import settings

class User(models.Model):
    email = models.CharField(max_length=120, null=False, blank=False)
    password = models.CharField(max_length=120, null=False, blank=False)
    f_name = models.CharField(max_length=120, null=False, blank=False)
    l_name = models.CharField(max_length=120, null=False, blank=False)
    reputation = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return str(self.email)

class Organization(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Role(models.Model):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=120,default='Staff' , null=False, blank=False)
    staff_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default='Anonymous')

    def __str__(self):
        return str(self.org_id)
