"""This module holds views for listing/creating Poem objects
and for editing/deleting Poem objects."""

from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as drf_filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Poem
from .serializers import PoemSerializer


class PoemList(generics.ListCreateAPIView):
    """
    List poems or create a poem if logged in.
    """
    serializer_class = PoemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Poem.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    def perform_create(self, serializer):
        """Set current user as the owner of the poem."""
        serializer.save(owner=self.request.user)  


class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a poem, or update or delete it by id if the current user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PoemSerializer
    queryset = Poem.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
