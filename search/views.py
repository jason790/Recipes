from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from .models import Search
from posts.models import WPPost

# Create your views here.
def search(request):
    """
    The search page
    """
    # products = Product.objects.order_by('created_at')[:6]
    term = request.GET.get('q', None)
    page = int(request.GET.get('page', '0'))
    template = loader.get_template('search/index.html')

    # check if there is a search term
    if term == None:
        context = {
            'title': 'Search Vegan Healthy Recipes'
        }
        return HttpResponse(template.render(context, request))

    # save the term in the database

    # look for the term in the database
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
            AND wp_posts.post_status = %(post_status)s
            AND MATCH(post_content) AGAINST (%(term)s)
        ORDER BY
            wp_posts.post_date_gmt DESC
        LIMIT 12
        OFFSET %(page)s
    """
    entries = WPPost.objects.raw(query, {
        "post_status": "publish",
        "page": page,
        "term": term
    })

    context = {
        'title': 'Search Vegan Healthy Recipes',
        'entries': entries
    }

    return HttpResponse(template.render(context, request))
