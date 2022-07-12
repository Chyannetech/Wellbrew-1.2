
from django.db import models
from django.urls import reverse


# Create your models here.
# class Categories(models.Model):
#     name:




class Business(models.Model):
    name = models.CharField(max_length=100)
    booth = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    social = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'business_id': self.id})
