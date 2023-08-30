"""This module holds a class to customize the admin panel."""

from django.contrib import admin
from django.db import models
from .models import Poem


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    """Customize list items of Poem model on admin panel."""
    list_display = ('owner', 'published', 'published_at',
                    'featured_flag')
    search_fields = ('owner', 'featured_flag')
    list_filter = ('owner',)
