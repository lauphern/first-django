from django.db import models

# Create your models here.
class Item:
  id: int
  name: str
  image: str
  price: int
  sale: bool