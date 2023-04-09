from rest_framework import serializers

from ..models import Category, Tag, Subscribe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'email']


class MiniCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class MiniTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']
