from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('user/sign-up/', views.sign_up, name='sign-up'),
]
