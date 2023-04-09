from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Blog, CommentBlog
from .serializers import BlogSerializer, BlogPOSTSerializer, CommentBlogSerializer, CommentBlogGETSerializer
from rest_framework import permissions


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.order_by('-id')
    serializer_class = BlogSerializer


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.order_by('-id')
    serializer_class = BlogPOSTSerializer
    permission_classes = (permissions.IsAdminUser, )


class BlogRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    # serializer_class = BlogPOSTSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogSerializer
        return BlogPOSTSerializer


class CommentBlogListAPIView(ListAPIView):
    queryset = CommentBlog.objects.order_by('-id')
    serializer_class = CommentBlogGETSerializer


class CommentBlogCreateAPIView(CreateAPIView):
    queryset = CommentBlog.objects.order_by('-id')
    serializer_class = CommentBlogSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        blog_id = self.kwargs.get('blog_id')
        if blog_id:
            qs = qs.filter(blog_id=blog_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['blog_id'] = self.kwargs.get('blog_id')
        return ctx
