from django.db import models

# Create your models here.
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length=50) # 제목
    writer = models.CharField(max_length=30) # 작성자
    content = models.TextField() # 내용
    regdate = models.DateTimeField(auto_now=timezone.now) # 등록날짜
    readcount = models.IntegerField(default=0) # 조회수

def __str__(self):
    return '%s. %s(%d)' % (self.title, self.writer, self.readcount)

def incrementReadCount(self):
    self.readCount += 1 # readCount = readCount + 1
    self.save