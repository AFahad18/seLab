from django.db import models

# Create your models here.
class Guide(models.Model):
    name = models.CharField(max_length=1000000)
    email = models.EmailField(max_length=254)
    location = models.CharField(max_length=1000000)
    number = models.CharField(max_length=11)
    password = models.CharField(max_length=20)