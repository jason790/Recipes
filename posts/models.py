from django.db import models
from meta.models import ModelMeta

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

    body = models.TextField()
    views = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')

    _metadata = {
        'title': title,
        'description': description,
        'excerpt': excerpt
    }

    def get_absolute_url(self):
        return reverse('post:title', kwargs={
            'slug': self.slug
        })

    class Meta():
        managed = False
        db_table = 'posts_post'


class WPPost(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.

    title = models.TextField(db_column='post_title')
    link = models.CharField(db_column='guid', max_length=255)
    slug = models.CharField(db_column='post_name', max_length=200)
    description = models.TextField(db_column='post_excerpt')
    picture = models.CharField(db_column='picture', max_length=255)
    body = models.TextField(db_column='post_content')

    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    # post_content = models.TextField()
    # post_title = models.TextField()
    # post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    # post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    # guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()


    # def picture():
    #     objects = models.Manager()
    #
    #     # res = objects.filter(meta_id=self.id, meta_key='_wp_attached_file')[:1][0]
    #     res = objects.all()[:1][0]
    #     return 'http://www.pesachisaholiday.com/assets/{}'.format(res.meta_value)

    def get_absolute_url(self):
        return reverse('post:title', kwargs={
            'id': self.id
        })

    class Meta():
        managed = False
        # WordPress table
        db_table = 'wp_posts'


class WpTermRelationships(models.Model):
    object_id = models.BigIntegerField()
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)

class WpTerms(models.Model):
    term_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta():
        managed = False
        db_table = 'wp_terms'

class WpPostmeta(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='meta_id')
    # post_id = models.BigIntegerField()
    post = models.ForeignKey('WPPost', related_name='meta', on_delete=models.CASCADE, db_column='post_id', blank=False, null=False)
    meta_key = models.CharField(max_length=255, blank=False, null=False, db_column='meta_key')
    meta_value = models.TextField(blank=False, null=False, db_column='meta_value')

    # picture = 'http://www.pesachisaholiday.com/assets/{}'.format(meta_value)


    class Meta:
        managed = False
        db_table = 'wp_postmeta'
        ordering = ['-pk']

# class WpPostThumbnail(models.Model):
#     id = models.ForeignKey('WpPostmeta', related_name='thumbnail', on_delete=models.CASCADE, db_column='meta_id', blank=False, null=False)
#     path = models.ForeignKey('WpPostmeta', related_name='path', on_delete=models.CASCADE, db_column='meta_value', blank=False, null=False)
