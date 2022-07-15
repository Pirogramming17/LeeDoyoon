from statistics import mode
from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  # GENRE_CHOICE = ( 
  #   ('SF', 'SF'), ('판타지', '판타지'), ('액션', '액션'), ('로맨스', '로맨스'),
  #   ('코미디','코미디'), ('애니메이션', '애니메이션'), ('공포', '공포'), ('멜로','멜로'),
  #   ('스릴러', '스릴러')
  #   )
  title = models.CharField(max_length=50, verbose_name='제목')
  date = models.IntegerField(verbose_name='개봉 년도')
  genre = models.CharField(max_length=50, verbose_name='장르')
  # genre = models.CharField(max_length=50, verbose_name='장르', choices=GENRE_CHOICE)
  score = models.FloatField(verbose_name='별점')
  runningtime = models.CharField(max_length=50, verbose_name='상영 시간')
  reviewcontent = models.TextField(verbose_name='리뷰')
  director = models.CharField(max_length=50, verbose_name='감독')
  actors = models.CharField(max_length=50, verbose_name='배우')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)