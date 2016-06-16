from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    created_at = models.DateTimeField('date created')
