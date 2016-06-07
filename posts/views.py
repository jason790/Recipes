from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
    """
    Show the latest recipes
    """
    recipes = Post.objects.order_by('-created_at')[:6]
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
