from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('img-view/<int:id>', views.img_view, name='img_view'),
    path('img-upload/', views.img_upload, name='img_upload'),
    
]
