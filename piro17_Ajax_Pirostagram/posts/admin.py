from django.contrib import admin
from .models import Post, Reply

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['like']
    list_display_links = ['like']
    
@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'like']
    list_display_links = ['post', 'content', 'like']