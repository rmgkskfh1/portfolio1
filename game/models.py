from django.db import models
from django.utils import timezone


#퍼즐

class Puzzle(models.Model):
    author = models.ForeignKey('auth.User') #퍼즐 생성자
    title = models.CharField(max_length=200) #퍼즐 이름
    text = models.TextField()  #퍼즐 내용
    score = models.TextField() #퍼즐 점수
    created_date = models.DateTimeField(default=timezone.now) #퍼즐 생성날짜
    
    def modify(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title


#각 퍼즐의 점수 (퍼즐 수에 따라 추가로 생성 가능)

class History(models.Model):
    author = models.ForeignKey('auth.User')

    created_date = models.DateTimeField(default=timezone.now) #기록날짜
    gametitle = models.CharField(max_length=140, default='gametitle')
    score = models.PositiveSmallIntegerField() #퍼즐점수
    savedata = models.TextField() #상태저장

    def modify(self):
        self.created_date = timezone.now()
        self.save()


    def __str__(self):
        return self.gametitle



