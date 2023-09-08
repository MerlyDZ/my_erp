# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
# from . import views
urlpatterns = [

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),    
    path('profil/', display_profile, name="display_profile"),
    path('change_password/', change_password, name="change_password"),
    path('change_username/', change_username, name="change_username"),
    path('change_email/', change_email, name='change_email'),
    path('logout/', logout, name="logout"),
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate_account'),
    path('activation_success/', activation_success, name='activation_success'),
    path('activation_failed/', activation_failed, name='activation_failed'),
    
    path('reset_failed/', reset_failed, name='reset_failed'),
    path('reset_complete/',reset_password_complete, name='reset_complete'),
    path('reset_password/', reset_password, name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', reset_password_confirm, name='reset_password_confirm'),
    path('password_reset_done/', reset_password_done, name='password_reset_done'),
]