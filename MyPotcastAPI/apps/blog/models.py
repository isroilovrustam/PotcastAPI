from django.db import models
from apps.main.models import Category, Tag
from apps.profile.models import Profile


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=202)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_blog')
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='tags_blog')

    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment_blog')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username
