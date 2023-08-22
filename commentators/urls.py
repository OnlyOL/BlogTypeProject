from django.contrib import admin
from django.urls import path, include
from commentators.views import *

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name="logout"),
    path('register_user', register_user, name="register")
]