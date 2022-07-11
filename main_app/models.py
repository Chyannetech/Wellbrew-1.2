from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name
