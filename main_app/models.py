from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    social = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'business_id': self.id})
