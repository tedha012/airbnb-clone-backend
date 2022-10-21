from email.headerregistry import Address
from email.policy import default
from pydoc import describe
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class House(models.Model):

  """ Model Definition for Houses """
  name = models.CharField(max_length=140)
  price_per_night = models.PositiveIntegerField()
  description = models.TextField()
  Address = models.CharField(max_length=140)
  pet_allowed = models.BooleanField(default=True)