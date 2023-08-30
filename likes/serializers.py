"""This module holds serailizer class for Like model."""

from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    The create method handles the unique constraint on 'owner' and 'poem.'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Define accessible fields."""
        model = Like
        fields = ['id', 'created_at', 'owner', 'poem']

    def create(self, validated_data):
        """
        If an integrity error occurs,
        tell 'possible duplicate.'
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
