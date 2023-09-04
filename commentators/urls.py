from django.contrib import admin
from django.urls import path, include
from commentators.views import *

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name="logout"),
    path('edit_user/', UserEditView.as_view(), name="edit_profile"),
    path('register_user', register_user, name="register"),

]