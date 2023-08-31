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
    filterset_fields = {
        'owner__followed__owner__profile': ['exact'],
        'likes__owner__profile': ['exact'],
        'owner__profile': ['exact'],
        'owner__profile__display_name': ['icontains'],
        'title': ['icontains'],
        'published_at': ['date__gte', 'date__lte'],
        'category': ['exact'],
        'published': ['exact'],
        'featured_flag': ['exact']
    }
    search_fields = (
        'title',
        'content',
    )
    ordering_fields = (
        'likes_count',
        'comments_count',
        'likes__created_at',
        'published_at',
        'created_at',
    )

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
