"""This module holds a class to customize the admin panel."""

from django.contrib import admin
from django.db import models
from .models import Profile


@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    """Customize list items of Profile model on admin panel."""
    list_display = ('owner', 'display_name', 'created_at')
    search_fields = ('owner', 'display_name')
    list_filter = ('owner', 'display_name')
