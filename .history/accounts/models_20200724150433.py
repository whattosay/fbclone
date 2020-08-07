from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(null = True, max_length=200)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    


    def __str__(self):
        return self.name

