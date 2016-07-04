from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from .models import Post
from .models import WPPost
from .models import WpPostmeta

# Create your views here.
def index(request):
    """
    Show the latest recipes
    """
    query = """
        SELECT
            ID, post_title,post_status,thumbnail.meta_key,thumbnail.meta_value
        FROM wp_posts
        RIGHT JOIN
            (
                SELECT
                    m.post_id,m.meta_id,t.meta_key,t.meta_value
                FROM wp_postmeta AS t
                    LEFT JOIN wp_postmeta AS m
                    ON m.meta_value = t.post_id
                WHERE t.meta_key = "_wp_attached_file"
                    AND m.meta_key = "_thumbnail_id"
            ) AS thumbnail
            ON thumbnail.post_id = wp_posts.id
        WHERE wp_posts.post_type = "post"
            AND wp_posts.post_status = post_status
        ORDER BY
            wp_posts.post_date_gmt DESC
        LIMIT 12
    """
    recipes = WPPost.objects.raw(query, {
        "post_status": "publish"
    })

    template = loader.get_template('recipes/index.html')
    context = {
        'title': 'Recipes',
        'recipes': recipes
    }

    return HttpResponse(template.render(context, request))

def show(request, slug):
    """
    Show a single recipe
    """
    query = """
        SELECT
                ID,post_title,post_content,post_date_gmt,thumbnail.meta_value
            FROM wp_posts
            RIGHT JOIN
                (
                    SELECT
                        m.post_id,m.meta_id,t.meta_key,t.meta_value
                    FROM wp_postmeta AS t
                        LEFT JOIN wp_postmeta AS m
                        ON m.meta_value = t.post_id
                    WHERE t.meta_key = "_wp_attached_file"
                        AND m.meta_key = "_thumbnail_id"
                ) AS thumbnail
            ON thumbnail.post_id = wp_posts.id
        WHERE wp_posts.post_type = "post"
            AND wp_posts.post_status = "publish"
            AND post_name=post_name
        LIMIT 1
    """
    recipe = WPPost.objects.raw(query, {
        "post_name": slug
    })[:1]

    if recipe == list():
        return redirect('/recipes')

    template = loader.get_template('recipes/show.html')
    context = {
        'title': recipe[0].title,
        'recipe': recipe[0]
    }

    return HttpResponse(template.render(context, request))
