from django.shortcuts import render
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
    recipes = WPPost.objects.prefetch_related('meta').filter(meta__meta_key='_wp_attached_file').order_by('-post_date_gmt')[:6]
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
    recipe = Post.objects.get(slug=slug)
    template = loader.get_template('recipes/show.html')
    context = {
        'title': recipe.title,
        'recipe': recipe
    }

    return HttpResponse(template.render(context, request))
