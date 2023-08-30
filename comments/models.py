"""This module holds Comment model."""

from django.db import models
from django.contrib.auth.models import User
from poems.models import Poem

STATUS = (('0', 'original'), ('1', 'edited'), ('2', 'deleted'))


class Comment(models.Model):
    """
    Comment model, related to User and Poem.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS,
                              default='0')
    content = models.TextField()

    class Meta:
        """Define how Comment objects will be ordered."""
        ordering = ['-created_at']

    def __str__(self):
        """Return the content."""
        return self.content
