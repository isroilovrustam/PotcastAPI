from rest_framework.generics import ListAPIView, CreateAPIView
from ..models import Category, Tag, Subscribe
from .serializers import CategorySerializer, TagSerializer, SubscribeSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SubscribeCreatedAPIView(CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
