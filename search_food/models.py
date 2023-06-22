from django.db import models

# Create your models here.
class hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    items = models.TextField()
    lat_long = models.TextField()
    f_details = models.TextField()
