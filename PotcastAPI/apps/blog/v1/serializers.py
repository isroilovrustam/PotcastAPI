from rest_framework import serializers
from ..models import Blog, BlogComment
from apps.main.v1.serializers import MiniCategorySerializer, MiniTagSerializer


class MiniBlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['author', 'message']


class BlogGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'category', 'image', 'tags', 'description', 'comment_blog', 'update_date',
                  'created_date']

    category = MiniCategorySerializer(read_only=True)
    tags = MiniTagSerializer(read_only=True, many=True)
    comment_blog = MiniBlogCommentSerializer(read_only=True, many=True)


class BlogPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'category', 'image', 'tags', 'description', 'update_date', 'created_date']


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['id', 'author', 'blog', 'message']

    def create(self, validated_data):
        request = self.context['request']
        blog_id = self.context['blog_id']
        author_id = request.user.profile_user.id
        message = validated_data.get('message')
        instance = BlogComment.objects.create(blog_id=blog_id, author_id=author_id, message=message)
        return instance
