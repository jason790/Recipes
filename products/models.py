from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    price = models.IntegerField()

    created_at = models.DateTimeField('date created')
