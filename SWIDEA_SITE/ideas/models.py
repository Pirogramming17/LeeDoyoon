from django.db import models
from django.utils import timezone

class DevTool(models.Model):
  name = models.CharField(max_length=50, verbose_name='name')
  kind = models.CharField(max_length=50, verbose_name='kind')
  content = models.TextField(verbose_name='content')

# Create your models here.
class Idea(models.Model):
  title = models.CharField(max_length=50, verbose_name='title')
  image = models.ImageField(blank = True, upload_to='idea/%Y%m%d', verbose_name='image')
  content = models.TextField(verbose_name='content')
  interest = models.IntegerField(verbose_name = 'interest')
  devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name='devtool_list')
  select = models.BooleanField(default=False, verbose_name='select')
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now = True)

# class OrderBy(models.Model):
#   ORDER_CHOICE = (
#     ('recent', 'recent'),
#     ('create', 'create'),
#     ('name', 'name'),
#     ('select', 'select')
#   )
#   order = models.CharField(max_length=10, choices = ORDER_CHOICE)