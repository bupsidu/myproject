# rest_app/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True) 
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)