from django.db import models

from datetime import datetime

# Create your models here.
class Program(models.Model):
    slug = models.CharField(max_length=255)

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)

    body = models.TextField()

    starting_at = models.DateTimeField('date starting at', default=datetime.now, blank=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now_add=True)
