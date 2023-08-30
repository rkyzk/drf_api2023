"""This module holds views for listing/creating Poem objects
and for editing/deleting Poem objects."""

from rest_framework import generics
from .models import Poem
from drf_api.permissions import IsOwnerOrReadOnly
from .serializers import PoemSerializer


class PoemList(generics.ListCreateAPIView):
    """
    List poems or create a poem if logged in.
    """
    serializer_class = PoemSerializer
    queryset = Poem.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        """Set current user as the owner of the poem."""
        serializer.save(owner=self.request.user)


class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a poem, or update or delete it by id if the current user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PoemSerializer
    queryset = Poem.objects.all().order_by('-created_at')
