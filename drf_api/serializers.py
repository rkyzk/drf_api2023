"""
This modul holds a serializer class for CurrentUser,
which provides the info of currently logged in user.
 """

from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Add three extra fields the profile id, image and profile name."""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    profile_name = serializers.ReadOnlyField(source='profile.display_name')

    class Meta(UserDetailsSerializer.Meta):
        """Make the profile id, image and profile name accessible."""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'profile_name'
        )
