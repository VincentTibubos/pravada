from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return str(self.username+'('+self.email+')')