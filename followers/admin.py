"""This module holds a class to customize the admin panel."""

from django.contrib import admin
from django.db import models
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    """Add list, search, filter items on the admin panel."""
    list_display = ['owner', 'followed', 'created_at']
    search_fields = ['owner', 'followed']
    list_filter = ['owner', 'followed']
