from rest_framework.generics import CreateAPIView
from ..models import Contact
from .serializers import ContactSerializers
from rest_framework import permissions


class ContactCreatedAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = (permissions.IsAuthenticated,)
