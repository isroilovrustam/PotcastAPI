from django.urls import path
from .views import CategoryListAPIView, TagListAPIView, SubscribeCreatedAPIView


urlpatterns = [
    path('category-list/', CategoryListAPIView.as_view()),
    path('tag-list/', TagListAPIView.as_view()),
    path('subscribe-create/', SubscribeCreatedAPIView.as_view()),
]