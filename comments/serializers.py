
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from datetime import datetime, timedelta


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds ??    extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    profile_name = serializers.ReadOnlyField(
                       source='owner.profile.display_name')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        if obj.created_at.date() > datetime.now().date() - timedelta(days=7):
            return naturaltime(obj.created_at)
        return obj.created_at.strftime("%d %b %Y")

    def get_updated_at(self, obj):
        if obj.updated_at.date() > datetime.now().date() - timedelta(days=7):
            return naturaltime(obj.updated_at)
        return obj.updated_at.strftime("%d %b %Y")

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'profile_name', 'poem', 'created_at',
            'status', 'content', 'updated_at'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Poem is a read only field so that we dont have to set it on each update
    """
    poem = serializers.ReadOnlyField(source='poem.id')
