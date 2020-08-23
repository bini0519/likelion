from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jasoseol(models.Model):
    #제목 글자 제한
    title = models.CharField(max_length=50)
    #내용
    content = models.TextField()
    #날짜와 시간은 자동생성
    updated_at = models.DateTimeField(auto_now=True)
    #작성자가 지워질 때 연결된 자소설도 지워진다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseal = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)

