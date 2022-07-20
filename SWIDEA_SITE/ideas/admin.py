from django.contrib import admin
from .models import Idea

@admin.register(Idea)
class PostAdmin(admin.ModelAdmin):
    pass