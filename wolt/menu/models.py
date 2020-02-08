from django.db import models
from django.conf import settings

class Coordinate(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()

class Trendy(models.Model):
    tag_1 = models.CharField(max_length=255)
    tag_2 = models.CharField(max_length=255)

class Example(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    online = models.BooleanField()

class Restaurants(models.Model):
        blurhash = models.CharField(max_length=300)
        city = models.CharField(max_length=255)
        currency = models.CharField(max_length=255)
        delivery_price = models.FloatField()
        description = models.TextField()
        image = models.URLField(max_length=300)
        location = models.ForeignKey(Coordinate, on_delete=models.CASCADE)
        name = models.CharField(max_length=300, unique=True)
        online = models.BooleanField()
        tags = models.ForeignKey(Trendy, on_delete=models.CASCADE)




# Create your models here.
