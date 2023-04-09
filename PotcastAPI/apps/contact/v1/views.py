from rest_framework import generics
from .serializers import ContactSerializer
from ..models import Contact


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.order_by('-id')
    serializer_class = ContactSerializer
