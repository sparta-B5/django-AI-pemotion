from django.db import models

class Feed(models.model):
    #게시글일지 모델 필드
    user_id = models.CharField(max_length=50, null=False)
    pet_id = models.CharField(max_length=50, null=False)
    image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    content = models.TextField(max_length=2200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #모델의 메타정보
    class Meta:
        db_table = 'diary'
        verbose_name = '게시글'  # 단수형 
        verbose_name_plural = '게시글들'  # 복수형