"""This module holds Poem model."""

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


CATEGORY = (('nature', 'nature'),
            ('love', 'love'),
            ('people', 'people'),
            ('humor', 'humor'),
            ('self', 'self'),
            ('haiku', 'haiku'),
            ('other', 'other'))


class Poem(models.Model):
    """List fields of Poem model and functions around them."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=80)
    content = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY,
                                default='other')
    published = models.BooleanField(default=False)
    featured_flag = models.BooleanField(default=False)

    class Meta:
        """Define options for how the poems will be ordered."""
        ordering = ['-created_at']

    def __str__(self):
        """
        Return the title.
        :return: title
        :rtype: str
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        If the poem is published, set published_at.
        """
        if self.published and not self.published_at:
            self.published_at = datetime.utcnow()
        super().save(*args, **kwargs)
