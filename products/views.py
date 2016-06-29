from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product

# Create your views here.
def index(request):
    """
    Show the featured products
    """
    products = Product.objects.order_by('created_at')[:6]
    template = loader.get_template('products/index.html')
    context = {
        'title': 'Products',
        'products': products
    }

    return HttpResponse(template.render(context, request))

def show(request, id):
    """
    Show a single product
    """
    product = Product.objects.get(id=id)
    template = loader.get_template('products/show.html')
    context = {
        'title': product.name,
        'product': product
    }

    return HttpResponse(template.render(context, request))
