from rest_framework import serializers
from ..models import Blog, CommentBlog
from apps.main.models import Category, Tag


class MiniCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MiniTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class MiniCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBlog
        fields = ['id', 'message']


class MiniBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title']


class BlogSerializer(serializers.ModelSerializer):
    category = MiniCategorySerializer(read_only=True)
    tags = MiniTagSerializer(read_only=True, many=True)
    comment_blog = MiniCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'category', 'image', 'description', 'tags', 'comment_blog', 'update_date',
                  'created_date']


class BlogPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'category', 'image', 'description', 'tags', 'update_date',
                  'created_date']

    def create(self, validated_data):
        request = self.context['request']
        author_id = request.user.profile_user.id
        instance = super().create(validated_data)
        instance.author_id = author_id
        instance.save()
        return instance


class CommentBlogGETSerializer(serializers.ModelSerializer):
    blog = MiniBlogSerializer(read_only=True)

    class Meta:
        model = CommentBlog
        fields = ['id', 'author', 'blog', 'message', 'created_date']


class CommentBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBlog
        fields = ['id', 'author', 'blog', 'message', 'created_date']

        extra_kwargs = {
            "blog": {'required': False},
            "author": {'required': False},
        }

    def create(self, validated_data):
        request = self.context['request']
        blog_id = self.context['blog_id']
        author_id = request.user.profile_user.id
        message = validated_data.get('message')
        instance = CommentBlog.objects.create(blog_id=blog_id, author_id=author_id, message=message)
        return instance
