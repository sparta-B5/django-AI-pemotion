from django.db import models

class Diary(models.Model):
    #게시글일지 모델 필드
    # user = models.CharField(max_length=50, null=False)
    # pet = models.CharField(max_length=50, null=False)
    petemotion = models.CharField(max_length=50, null=False)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=100)
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