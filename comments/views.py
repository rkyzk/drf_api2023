"""This module holds views for listing/creating Comment objects
and for editing/deleting Comment objects."""

from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """
        Set the current user as the owner
        when a new object is created.
        """
        serializer.save(owner=self.request.user)
