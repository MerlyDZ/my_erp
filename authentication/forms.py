# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import PasswordResetForm,PasswordChangeForm,UserCreationForm
from django.contrib.auth import get_user_model
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Prémon",
                "class": "form-control"
            }
        ))
    
    sex = forms.ChoiceField(
        choices=User.SEX_CHOICES, 
        widget=forms.Select(  
            attrs={
                "placeholder": "Sexe",
                "class": "form-control" 
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password confirm",
                "class": "form-control"
            }
        ))
    class Meta:
        model = get_user_model()
        fields = ('username', 'last_name', 'first_name', 'sex', 'email')
        
    
class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(max_length=150, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "new username",
                "class": "form-control"
            }
        )) 


class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(max_length=254,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "new email",                
                "class": "form-control"
            }
        ))                         
                                 

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
      widget=forms.PasswordInput(
          attrs={
              "placeholder": "Ancien mot de passe",
              "class": "form-control"
          }
      ))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "nouveau mot de passe",
                "class": "form-control"
            }
        ))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "confirmer le mot de passe",
                "class": "form-control"
            }
        ))
