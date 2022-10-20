from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('diary/', views.diary_create, name='diary_create'),
    path('diary/<int:id>', views.diary_detail, name='diary_detail'),
    path('diary/update/<int:id>', views.diary_update, name='diary_update'),
    path('diary/delete/<int:id>', views.diary_delete, name='diary_delete'),
    path('img-view/<int:id>', views.img_view, name='img_view'),
    path('img-upload/', views.img_upload, name='img_upload'),
]
