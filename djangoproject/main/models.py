from django.db import models

# Create your models here.

class Jasoseol(models.Model):
    #제목 글자 제한
    title = models.CharField(max_length=50)
    #내용
    content = models.TextField()
    #날짜와 시간은 자동생성
    updated_at = models.DateTimeField(auto_now=True)