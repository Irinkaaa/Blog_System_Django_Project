from rest_framework import generics as views, permissions
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework.serializers import ModelSerializer

from Blog_System.blogs.models import Post, Blog


class PostSerializer(ModelSerializer):
    blog_id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ('title', 'text', 'blog_id')


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CreatePostApiView(views.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        blog = Blog.objects.get(pk=serializer.validated_data['blog_id'])
        if blog.user_id != self.request.user.id:
            raise PermissionDenied

        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
