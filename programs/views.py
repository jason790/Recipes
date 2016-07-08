from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from .models import Program

# Create your views here.
def start_here(request):
    template = loader.get_template('programs/start_here.html')
    context = {
        'title': 'Start Here - Healthy & Vegan Recipes',
        'description': 'Learn how to make healthy food at home, for dinner, for work. Vegan and healthy recipes with natural ingredients.'
    }
    return HttpResponse(template.render(context, request))
