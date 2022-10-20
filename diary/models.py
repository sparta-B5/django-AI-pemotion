from unittest.util import _MAX_LENGTH
from django.db import models
import os
from uuid import uuid4

def upload_to_func(instance, filename):
    upload_to = f'diary/'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    filename = '{}.{}'.format(uuid, ext)
    
    return os.path.join(upload_to, filename)

class Diary(models.Model):
    # 게시글일지 모델 필드
    # user = models.CharField(max_length=50, null=False)
    # pet = models.CharField(max_length=50, null=False)
    # 이미지업로드 필드
    image = models.ImageField(upload_to=upload_to_func, max_length=255,null = True)
    emotion_predict = models.TextField(null = True)
    emotion_label = models.CharField(max_length=20,null = True)
    emotion_percent = models.FloatField(null = True)
    content = models.TextField(max_length=2200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #모델의 메타정보
    class Meta:
        db_table = 'diary'
        verbose_name = '게시글'  # 단수형 
        verbose_name_plural = '게시글들'  # 복수형

    def __str__(self):
        return f'{self.id} | {self.created_at} | {self.content}'

