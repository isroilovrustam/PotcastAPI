from django.urls import path
from .views import BlogListAPIView, BlogRUDAPIView, BlogCreateAPIView, CommentBlogListAPIView, CommentBlogCreateAPIView

urlpatterns = [
    path('blog-list/', BlogListAPIView.as_view()),
    path('blog-create/', BlogCreateAPIView.as_view()),
    path('blog-rud/<int:pk>/', BlogRUDAPIView.as_view()),
    path('comment-blog-list/', CommentBlogListAPIView.as_view()),
    path('<int:blog_id>/comment-blog-create/', CommentBlogCreateAPIView.as_view()),
]