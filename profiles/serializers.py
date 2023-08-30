"""This module holds serializer class for Profile model."""

from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Add or modify 5 fields."""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    user_id = serializers.ReadOnlyField(source='owner.pk')

    def get_is_owner(self, obj):
        """
        Return if the current user is the profile owner.
        :return: true/false
        :rtype: boolean
        """
        request = self.context['request']
        return request.user == obj.owner


    def validate_image(self, value):
        """
        Raise error if file size exceeds 800KB,
        or the image height or width exceeds 1000px
        otherwise return the uploaded file.
        :return: value
        :rtype: django uploaded file object
        """
        if value.size > 800 * 1024:
            raise serializers.ValidationError(
                "Files larger than 800KB can't be uploaded."
            )
        if value.image.height > 1000:
            raise serializers.ValidationError(
                "Images with height over 1000px can't be uploaded."
            )
        if value.image.width > 1000:
            raise serializers.ValidationError(
                "Images with width over 1000px can't be uploaded."
            )
        return value

    class Meta:
        """Define which fields will be accessible."""
        model = Profile
        fields = [
            'id', 'owner', 'display_name', 'created_at', 'updated_at',
            'about_me', 'favorites', 'image', 'is_owner', 'user_id',
        ]
