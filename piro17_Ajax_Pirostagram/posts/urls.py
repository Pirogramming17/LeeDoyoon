from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = "posts"

urlpatterns = [
  path('', views.main, name='main'),
  path('like_post/', views.like_post, name='like_post'),
  path('like_reply/', views.like_reply, name='like_reply'),
  # path('bookmark/', views.bookmark, name='bookmark'),
  path('add_reply/', views.add_reply, name='add_reply'),
  path('delete_reply/', views.delete_reply, name='delete_reply'),
  
  ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)