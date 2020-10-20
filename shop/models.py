from django.db import models

# Create your models here.

# https://docs.djangoproject.com/en/3.1/ref/models/fields/

class Item(models.Model):
  name = models.CharField(max_length=100)
  img = models.ImageField(upload_to='pics')
  price = models.IntegerField()
  sale = models.BooleanField(default=False)