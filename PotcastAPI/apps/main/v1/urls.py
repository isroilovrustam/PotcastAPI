from django.urls import path
from .views import CategoryListAPIView, TagListAPIView, SubscribeCreateAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('tag/', TagListAPIView.as_view()),
    path('subscribe/', SubscribeCreateAPIView.as_view()),
]
