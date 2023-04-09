from django.contrib import admin
from .models import Blog, CommentBlog
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    filter_horizontal = ('tags',)


@admin.register(CommentBlog)
class CommentBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'blog']

