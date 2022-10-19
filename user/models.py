from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): 
    user = models.CharField(max_length=150, null=True)
    name =models.CharField(max_length=20, null=True)
    
    
   