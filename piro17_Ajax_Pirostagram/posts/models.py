from django.db import models

# Create your models here.

class Post(models.Model):
  like = models.BooleanField(default=False, verbose_name='좋아요')
  content = models.TextField(verbose_name='내용')
  photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
  bookmark = models.BooleanField(default=False, verbose_name='북마크')
  
class Reply(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
  content = models.CharField(max_length=200, verbose_name='댓글')
  like = models.BooleanField(default=False, verbose_name='좋아요')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
  
  def __str__(self):
    return self.content
  class Meta:
    ordering = ['-created_at']
    verbose_name = '댓글'
    verbose_name_plural = '댓글'
