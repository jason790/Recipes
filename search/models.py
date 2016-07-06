from django.db import models

# Create your models here.
class Search(models.Model):
    term = models.CharField(max_length=60, default='')
    searches = models.IntegerField(default=1)
