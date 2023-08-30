"""This module holds Profile model."""

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """List fields of Profile model and functions around them."""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_name = models.CharField(max_length=25, blank=True)
    about_me = models.TextField(null=True, blank=True)
    favorites = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../sunset.jpg'
    )
    featured_flag = models.BooleanField(default=False)

    class Meta:
        """Define options for how the profiles will be ordered."""
        ordering = ['-created_at']

    def __str__(self):
        """
        Return the owner's username
        :return: owner's username
        :rtype: str
        """
        return f"{self.owner}'s profile"

    def save(self, *args, **kwargs):
        """
        If display name is left blank, set username to it.
        """
        if not self.display_name:
            self.display_name = self.owner.username
        super().save(*args, **kwargs)


def create_profile(sender, instance, created, **kwargs):
    """Create Profile instance if a new user is created."""
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
