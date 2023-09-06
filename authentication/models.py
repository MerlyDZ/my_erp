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
    email = models.EmailField(unique=True,null= True)
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


