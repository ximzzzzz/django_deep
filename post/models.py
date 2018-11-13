from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50) #컬럼 두개 추가
    content = models.CharField(max_length=100)
    
    def __str__(self): #오브젝트 출력할때 타이틀로 출력하도록 재설정
        return self.title