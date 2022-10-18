from django.db import models
from django.urls import reverse

# Create your models here.
class Candy(models.Model):
    name = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'candy_id': self.id})