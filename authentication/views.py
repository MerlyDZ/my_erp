# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from mailjet_rest import Client
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ChangeUsernameForm, ChangeEmailForm, PasswordChangeForm, PasswordResetForm,  LoginForm, SignUpForm
from django.contrib.auth import logout as auth_logout

user = get_user_model()

def login_view(request):
    form = LoginForm(request.POST)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "authentication/login.html", {"form": form, "msg": msg})


def register_user(request):
    form = SignUpForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = form.save(commit=False)
            user.is_active = False  
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"{request.scheme}://{request.get_host()}/activate/{uid}/{token}/"

            api_key ='c271420fc766e2f9bf76ba649e08b642'
            api_secret ='3c2d7b04ea5871619dbb6ee6c1482eb5'

            mailjet = Client(auth=(api_key, api_secret))
            data = {
	            'FromEmail': 'lougbegnona@gmail.com',
	            'FromName': 'Django DJ',
	            'Subject': 'Activate your account',
                'Text-part': 'Bienvenu sur votre page d\activation',
                'Html-part': f'Veuillez cliquer sur le lien <a href="{activation_link}">Activate my account</a> pour activer votre compte.',
                'Recipients': [{'Email':user.email}]
            }
            try:
                response = mailjet.send.create(data=data)
                if response.status_code == 200:
                    return redirect('login')
                else:
                    print(response.status_code)
                    print("Erreur lors de l'envoi de l'e-mail de confirmation :", response.content)
                    form.add_error(None, "Désolé, une erreur s'est produite lors de l'envoi de l'e-mail de confirmation. Veuillez réessayer plus tard.")
            except Exception as e:
                print("Erreur lors de l'envoi de l'e-mail de confirmation :",str(e))
                form.add_error(None, "Désolé, une erreur s'est produite lors de l'envoi de l'e-mail de confirmation. Veuillez réessayer plus tard.")
        else:
            print(form.errors)

    return render(request, 'authentication/register.html', {'form': form})


@login_required
def display_profile(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    context = {

    }
    return render(request, 'authentication/new_profil.html', context)


@login_required
def profil(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    return render(request, 'authentication/profil.html')

def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            if request.user.check_password(form.cleaned_data['old_password']):
                if form.cleaned_data['new_password1'] == form.cleaned_data['new_password2']:
                    user = form.save()
                    print("Mot de passe changé avec succès.")
                    return redirect('login')
                else:
                    print("Le nouveau mot de passe et la confirmation sont différents.")
            else:
                print("Ancien mot de passe incorrect.")
        else:
            form = PasswordChangeForm(request.user)
    context =  {
        "form": form
    }      
    return render(request, 'authentication/change_password.html', context)

def change_email(request):
    form = None
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            print(new_email)
            request.user.email = new_email
            request.user.save()
            return redirect('display_profile')
        else:
            print(form.errors)
    else:
        form = ChangeEmailForm()
    context = {
        "form": form
    }
    return render(request, 'authentication/change_email.html', context)


def change_username(request):
    form = None
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            request.user.username = new_username
            request.user.save()
            return redirect('display_profile')
        else:
            print(form.errors)
    else:
        form = ChangeUsernameForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/change_username.html', context)



def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('activation_success')
        else:
            return redirect('activation_failed')
    except User.DoesNotExist:
        return render(request, 'authentication/activation_failed.html')


def activation_success(request):
    return render(request, 'authentication/activation_success.html')


def activation_failed(request):
    return render(request, 'authentication/activation_failed.html')


def reset_password(request):
    form = None
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
        
            email = form.cleaned_data.get("email")
            user = User.objects.get(email=email)
            print(user)
            token = default_token_generator.make_token(user)
            reset_password_url = reverse('reset_password_confirm', kwargs={'uidb64': user.pk, 'token': token})
            reset_password_url = request.build_absolute_uri(reset_password_url)

            api_key ='c271420fc766e2f9bf76ba649e08b642'
            api_secret ='3c2d7b04ea5871619dbb6ee6c1482eb5'

            print(reset_password_url)
            mailjet = Client(auth=(api_key, api_secret))
            data = {
                'FromEmail': 'lougbegnona@gmail.com',
                'FromName': 'Django DJ',
                'Subject': 'Réinitiliser votre mot de passe',
                'Text-part': 'Bienvenu sur la page de réinitialisation',
                'Html-part': f'Veuillez cliquer sur le lien suivant :<a href="{reset_password_url}">REINITIALISER</a> pour continuer.',
                
                'Recipients': [{'Email':user.email}]
            }
             
            try:
                response = mailjet.send.create(data=data) 
                if response.status_code == 200:
                    return redirect('password_reset_done')
                else:
                    print(response.status_code)
                    print("Erreur lors de l'envoi de l'e-mail de confirmation :", response.content)
                    form.add_error(None, "Désolé, une erreur s'est produite lors de l'envoi de l'e-mail de confirmation. Veuillez réessayer plus tard.")
            except Exception as e:
                    print("Erreur lors de l'envoi de l'e-mail de confirmation :",str(e))
                    form.add_error(None, "Désolé, une erreur s'est produite lors de l'envoi de l'e-mail de confirmation. Veuillez réessayer plus tard.")
                    return redirect('password_reset_done')

        else:
            print(form.errors)
    else:
        form = PasswordResetForm()
    context = {
        "form": form
    }
    return render(request, 'authentication/password_reset_form.html', context)


def reset_password_confirm(request, uidb64, token):
    try:
        user = User.objects.get(pk=uidb64)
    except:
        user = None
    if default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('reset_complete')
            else:
                print(form.errors)
        else:
            form = PasswordChangeForm(user)
    else:
        return redirect('reset_failed')
    context = {
        "form": form
    }        
    return render(request, 'authentication/password_reset_confirm.html', context)
       
def reset_password_complete(request):
    return render(request, 'authentication/password_reset_complete.html')


def reset_failed(request):
    return render(request, 'authentication/reset_failed.html')

def reset_password_done(request):
    return render(request, 'authentication/password_reset_done.html')

def logout(request):
    auth_logout(request)
    response = redirect("login")
    return response
   

