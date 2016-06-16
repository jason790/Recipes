from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import logging

from .models import Subscriber

# Create your views here.
def create(request):
    """
    Create a new subscriber
    """
    logger = logging.getLogger(__name__)
    # subscriber = Subscriber.objects.create(name=name, email=email)
    subscriber = Subscriber.objects.all()

    logger.debug(subscriber)
    logger.debug(subscriber==None)

    return JsonResponse(dict(subscriber))
