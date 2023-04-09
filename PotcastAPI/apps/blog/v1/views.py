from rest_framework import generics, permissions
from . import serializers
from ..models import Blog, BlogComment


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.order_by('-id')
    serializer_class = serializers.BlogGETSerializer


class BlogCreateAPIView(generics.CreateAPIView):
    queryset = Blog.objects.order_by('-id')
    serializer_class = serializers.BlogPOSTSerializer


class BlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.order_by('-id')
    serializer_class = serializers.BlogGETSerializer


class BlogCommentCreateAPIView(generics.CreateAPIView):
    queryset = BlogComment.objects.order_by('-id')
    serializer_class = serializers.BlogCommentSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        qs = super().get_queryset()
        blog_id = self.kwargs.get("blog_id")
        if blog_id:
            qs = qs.filter(blog_id=blog_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['blog_id'] = self.kwargs.get('blog_id')
        return ctx
