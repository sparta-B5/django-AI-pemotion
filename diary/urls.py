from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('feed/create/', views.feed_create, name='feed_create'),
    path('feed/<int:id>', views.feed_detail, name='feed_detail'),
    path('feed/delete/<int:id>', views.feed_delete, name='feed_delete'),
]
