# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class User(AbstractUser):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    sex = models.CharField(max_length=1, choices=SEX_CHOICES,)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True,null= True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=50)     
    residence = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    contacts = models.CharField(max_length=50)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


