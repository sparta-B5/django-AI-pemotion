from django.db import models
import os
from uuid import uuid4

def upload_to_func(instance, filename):
    upload_to = f'diary/'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    filename = '{}.{}'.format(uuid, ext)
    
    return os.path.join(upload_to, filename)

# Create your models here.
class Diary(models.Model):

  # 이미지업로드 필드
  image = models.ImageField(upload_to=upload_to_func, max_length=255 )