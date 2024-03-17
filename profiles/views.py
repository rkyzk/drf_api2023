"""This module holds views for listing Profile objects
and for editing Profile objects."""

from django.db.models import Count
from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        poems_count=Count('owner__poem', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
        'featured_flag'
    ]
    search_fields = ('display_name',)
    ordering_fields = [
        'poems_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if the current user is the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        poems_count=Count('owner__poem', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer


class DeleteUser(APIView):
    """
    Set user inactive and delete associated profile.
    Action can be performed only by users on their own account or
    by staff members on any accounts.
    The code was taken from below and was modified.
    https://github.com/andy-guttridge/tribehub_drf/blob/main/profiles/views.py
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        user_to_delete = User.objects.filter(
            pk=pk
        ).first()
        profile_to_delete = Profile.objects.filter(
            user=pk
        ).first()
        # raise 'not found' error if the user doesn't exist.
        if user_to_delete is None or profile_to_delete is None:
            raise Http404
        # if the user is staff member or the user is the owner of the account,
        # set the user account inactive and delete the profile.
        if request.user.is_staff == True or user_to_delete == request.user:
            try:
                user_to_delete.is_active(False)
                user_to_delete.save()
                profile_to_delete.delete()
            except Exception as e:
                return Response(
                    str(e),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            # set success message
            return Response(
                {'detail': 'The user account has been deleted.'},
                status=status.HTTP_200_OK
            )
        else:
            # set 403 error message
            return Response(
                {"detail": "You are not allowed to perform this action"},
                status=status.HTTP_403_FORBIDDEN
        )
