from django.urls import path
form . import views

urlpatterns = [
  path('', views.post_list, name='post_list')
]