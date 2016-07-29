from django.db import models

from posts.models import WPPost

# Create your models here.
class Search(models.Model):
    term = models.CharField(max_length=60, default='')
    searches = models.IntegerField(default=1)

    def find(term, page):
        query = """
            SELECT
                ID,
                post_title,
                post_status,
                CONCAT('http://www.pesachisaholiday.com/assets/uploads/',
                    thumbnail.meta_value) AS picture,
                MATCH (post_title) AGAINST (%(term)s) AS title_score,
                MATCH (post_excerpt) AGAINST (%(term)s) AS excerpt_score,
                MATCH (post_content) AGAINST (%(term)s) AS content_score
            FROM wp_posts
            RIGHT JOIN
                (
                    SELECT
                        m.post_id,
                        m.meta_id,
                        t.meta_key,
                        t.meta_value
                    FROM wp_postmeta AS t
                        LEFT JOIN wp_postmeta AS m
                        ON m.meta_value = t.post_id
                    WHERE t.meta_key = "_wp_attached_file"
                        AND m.meta_key = "_thumbnail_id"
                ) AS thumbnail
                ON thumbnail.post_id = wp_posts.id
            WHERE wp_posts.post_type = "post"
                AND wp_posts.post_status = %(post_status)s
                AND (
                    wp_posts.post_title REGEXP(%(term)s)
                    OR MATCH (wp_posts.post_excerpt) AGAINST (%(term)s)
                    OR MATCH (wp_posts.post_content) AGAINST (%(term)s)
                )
            ORDER BY
                title_score DESC,
                content_score DESC,
                excerpt_score DESC,
                wp_posts.post_date_gmt DESC
            LIMIT 20
            OFFSET %(page)s
        """
        entries = WPPost.objects.raw(query, {
            'post_status': 'publish',
            'page': page,
            'term': term,
            'picture': 'picture'
        })

        return entries
