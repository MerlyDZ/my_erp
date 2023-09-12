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
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('O', 'Non-binaire'),
    ]
    username = models.CharField(unique=True, max_length=150, verbose_name='username')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField(unique=True,null= True)
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Entreprise(models.Model):
    COUNTRIES_CHOICES = [
        ('', 'Bénin'),
        ('', 'Togo'),
        ('', 'Mali'),
        ('', 'Burkina-faso'),
        ('', 'Guinée'),
        ('', 'Etats-Unis'),
        ('', 'Gnambie'),
        ('', 'France'),
        ('', 'Maroc'),
        ('', 'Rwanda'),
    ]
    LANGUAGES_CHOICES = [
        ('', 'Anglais'),
        ('', 'Allemand'),
        ('', 'Britanique'),
        ('', 'Chinois'),
        ('', 'Espagnol'),
        ('', 'Français'),
        
    ]
    
    TAILLE_CHOICES = [
        ('', '<10'),
        ('', '10 - 55'),
        ('', '>55'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    entreprise_name = models.CharField(max_length=200)
    taille = models.CharField(max_length=50, choices=TAILLE_CHOICES)
    description = models.TextField(max_length=300)
    email = models.EmailField(max_length=200)
    countries = models.CharField(max_length=100, choices=COUNTRIES_CHOICES)
    languages = models.CharField(max_length=100, choices=LANGUAGES_CHOICES)

    def __str__(self):
        return self.entreprise_name
