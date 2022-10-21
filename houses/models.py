from email.headerregistry import Address
from pydoc import describe
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class House(models.Model):

  """ Model Definition for Houses """
  name = models.CharField(max_length=140)
  price = models.PositiveIntegerField()
  description = models.TextField()
  Address = models.CharField(max_length=140)