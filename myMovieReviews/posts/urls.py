from django.urls import path
from django.contrib import admin
from . import views

app_name="posts"
urlpatterns = [
  path('', views.review_list, name='review_list'),
  path('create', views.create, name='create'),
  path('detail/<int:id>', views.detail, name='detail'),
  path('update/<int:id>', views.update, name='update'),
  path('delete/<int:id>', views.delete, name='delete'),
]