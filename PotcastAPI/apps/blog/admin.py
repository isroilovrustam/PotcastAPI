from django.contrib import admin
from .models import Blog, BlogComment
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']