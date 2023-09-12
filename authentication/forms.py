# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import PasswordResetForm,PasswordChangeForm,UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from .models import Entreprise
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
                "placeholder": "Mot de passe",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmer mot de passe",
                "class": "form-control"
            }
        ))
    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name', 'sex', 'email')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = "@" + self.cleaned_data['first_name']
        if commit:
            user.save()
        return user   
    
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


class EntrepriseForm(forms.ModelForm):
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
    entreprise_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom de l'entreprise",
                "class": "form-control"
            }
        ))
    taille = forms.ChoiceField(
        choices=Entreprise.TAILLE_CHOICES, 
        widget=forms.Select(  
            attrs={
                "placeholder": "Taille",
                "class": "form-control" 
            }
        ))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Description",
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
    
    countries = forms.ChoiceField(
        choices=Entreprise.COUNTRIES_CHOICES, 
        widget=forms.Select(  
            attrs={
                "placeholder": "Pays",
                "class": "form-control" 
            }
        ))
    languages = forms.ChoiceField(
        choices=Entreprise.LANGUAGES_CHOICES, 
        widget=forms.Select(  
            attrs={
                "placeholder": "langue",
                "class": "form-control" 
            }
        ))
    class Meta:
        model = Entreprise
        fields = ['first_name', 'last_name', 'entreprise_name', 'taille', 'description', 'email', 'countries', 'languages']
