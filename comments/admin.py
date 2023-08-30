"""This module holds a class to customize the admin panel."""

from django.contrib import admin
from django.db import models
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Customizes list, filter and search items on admin panel."""
    list_display = ('owner', 'status', 'created_at')
    search_fields = ('owner',)
    list_filter = ('owner',)
