from django.db import models

class Location(models.Model):
    ip_address = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=100, null=True, blank=True)

   