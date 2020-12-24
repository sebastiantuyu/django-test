""" Escribir moddelos del post """

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    bio = models.TextField()

    bdate = models.DateField(blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    last = models.DateTimeField(auto_now=True)