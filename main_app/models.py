from django.db import models
from django.urls import reverse

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'pk': self.id})

class Candy(models.Model):
    name = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # add the M:M relationship
    brand = models.ManyToManyField(Brand)

    def __str__(self):
        return self.name

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'candy_id': self.id})

class Ingredients(models.Model):
    ing1= models.CharField(max_length=100)
    exp_date= models.DateField('Expiration Date')

    candy= models.ForeignKey(Candy, on_delete=models.CASCADE)

    def __str__(self):
        return self.ing1

    class Meta:
        ordering = ['-exp_date']

