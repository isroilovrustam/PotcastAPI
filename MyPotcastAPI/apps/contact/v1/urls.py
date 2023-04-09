from django.urls import path
from .views import ContactCreatedAPIView

urlpatterns = [
    path('contact-create/', ContactCreatedAPIView.as_view())
]