"""This module holds serailizer class for Poem model."""

from rest_framework import serializers
from poems.models import Poem
from datetime import datetime


class PoemSerializer(serializers.ModelSerializer):
    """Add or modify 7 fields"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    profile_name = serializers.ReadOnlyField(
        source='owner.profile.display_name')
    featured_flag = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Return if the poem is owned by the current user.
        :return: true/false
        :rtype: boolean
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """Define which fields will be accessible."""
        model = Poem
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'profile_name', 'created_at', 'published_at',
            'updated_at', 'title', 'content', 'category', 'published',
            'featured_flag'
        ]
