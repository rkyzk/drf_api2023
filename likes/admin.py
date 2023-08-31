"""This module holds class to customize the admin panel."""

from django.contrib import admin
from django.db import models
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Add list, search and filter items on admin panel."""
    list_display = ('owner', 'poem', 'created_at')
    search_fields = ('owner', 'poem',)
    list_filter = ('owner', 'poem',)
