from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    phone = models.IntegerField()
    website = models.CharField(max_length=100)

