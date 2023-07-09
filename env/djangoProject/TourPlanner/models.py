from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    tag = models.CharField(max_length=32)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(null=True, blank=True, upload_to ='post_images/')

class Hotel(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    rent = models.FloatField()
    rating = models.IntegerField()
    description = models.TextField()
    hotel_image = models.ImageField(null=True, blank=True, upload_to ='hotels/')

class Package(models.Model):
    location = models.CharField(max_length=64)
    rating = models.IntegerField()
    person = models.IntegerField()
    destination = models.CharField(max_length=256)
    hotelRoom = models.CharField(max_length=256)
    transport = models.CharField(max_length=256)
    datetime = models.CharField(max_length=128)
    food = models.CharField(max_length=256)
    price = models.FloatField()
    package_image = models.ImageField(null=True, blank=True, upload_to ='package_images/')
    package_image1 = models.ImageField(null=True, blank=True, upload_to ='package_images/details')
    package_image2 = models.ImageField(null=True, blank=True, upload_to ='package_images/details')
    package_image3 = models.ImageField(null=True, blank=True, upload_to ='package_images/details')
