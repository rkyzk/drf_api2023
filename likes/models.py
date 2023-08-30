"""This module holds Like model."""

from django.db import models
from django.contrib.auth.models import User
from poems.models import Poem


class Like(models.Model):
    """
    Like model, related to User and Poem.
    'owner' is a User instance and 'poem' is a Poem instance.
    'unique_together' makes sure a user can't like the same poem twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    poem = models.ForeignKey(
        Poem, related_name='likes', on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Define options for how the Like objects will be ordered.
        By defining 'unique_together' prevent the same user
        from liking the same poem multiple times.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'poem']

    def __str__(self):
        """Return the poem id and the owner's username."""
        return f"{self.poem} {self.owner}"
