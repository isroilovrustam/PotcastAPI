from django.urls import path
from . import views

urlpatterns = [
    path('blog-list/', views.BlogListAPIView.as_view()),
    path('blog-create/', views.BlogCreateAPIView.as_view()),
    path('blog-retrieve/<int:pk>/', views.BlogRetrieveAPIView.as_view()),
    path('blog-comment/<int:blog_id>/', views.BlogCommentCreateAPIView.as_view()),
]