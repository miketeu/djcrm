"""Represents a contact associated with a user."""

from django.conf import settings as django_settings
from django.db import models


class Settings:
    """Small convenience layer over Django's settings object."""

    @staticmethod
    def get(name, default=None):
        """Return a Django setting with a fallback value if missing."""
        return getattr(django_settings, name, default)

    @staticmethod
    def set(name, value):
        """Set a Django setting value at runtime and return it."""
        setattr(django_settings, name, value)
        return value

    @staticmethod
    def has(name):
        """Return True if the setting exists on Django's settings object."""
        return hasattr(django_settings, name)

    @staticmethod
    def as_dict():
        """Return all uppercase settings as a dictionary."""
        return {
            key: value for key, value in vars(django_settings).items() if key.isupper()
        }


# This points to the user model defined in settings.AUTH_USER_MODEL, which is
# "auth.User" by default. If AUTH_USER_MODEL is changed to a custom user model,
# this will point to that model instead.
User = (
    django_settings.AUTH_USER_MODEL
)  # -> "auth.User" by default, can be changed to a custom user model if needed

# Create your models here


class Contact(models.Model):
    """Represents a contact associated with a user."""

    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.CASCADE,
    )  # null=True allows for the possibility of a contact not being associated with a user
    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name="ID",
    )  # BigAutoField is used for the primary key, which is an auto-incrementing integer
    email = models.EmailField()
    notes = models.TextField(blank=True, default="This is my other default note.")  #
