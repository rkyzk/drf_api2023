"""This module holds views for listing Profile objects
and for editing Profile objects."""

from rest_framework import generics
from .models import Profile
from drf_api.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
