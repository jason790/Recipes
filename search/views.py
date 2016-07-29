from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.template import loader

from react import jsx

from .models import Search

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
    else:
        # put a limit on the length of the term
        term = term[:40]

    # save the term in the database
    search, created = Search.objects.get_or_create(term=term)
    search.searches = search.searches+1
    search.save()

    # look for the term in the database
    entries = Search.find(term, page)

    context = {
        'title': 'Search Vegan Healthy Recipes',
        'entries': entries
    }

    return HttpResponse(template.render(context, request))

# For client side search
def autocomplete(request):
    """
    Client side search
    """
    # products = Product.objects.order_by('created_at')[:6]
    term = request.GET.get('q', None)
    page = int(request.GET.get('page', '0'))
    if term == None:
        return JsonResponse(dict(data=str()))

    entries = Search.find(term, page)

    return JsonResponse(dict(data=serialize('json', entries)))
    # return JsonResponse(dict(data=serialize("json", subscribers)))
