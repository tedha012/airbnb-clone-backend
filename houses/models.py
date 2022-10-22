from email.headerregistry import Address
from email.policy import default
from pydoc import describe
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models


class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Positive Numbers Only"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True,
        help_text="Does this house allow pets?",
    )
    owver = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
