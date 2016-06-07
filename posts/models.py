from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    slug = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    post_status = models.CharField(max_length=12)
    post_type = models.CharField(max_length=255)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)

    body = HTMLField()
    views = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')

    def get_absolute_url(self):
        return reverse('post:title', kwargs={
            'slug': self.slug
        })