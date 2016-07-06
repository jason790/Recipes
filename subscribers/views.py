from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
import logging

from datetime import datetime

from .models import Subscriber

# Create your views here.
def create(request):
    """
    Create a new subscriber
    """
    logger = logging.getLogger(__name__)

    name = request.POST.get('name')
    email = request.POST.get('email')
    subscriber = Subscriber(name=name, email=email, created_at=datetime.utcnow())
    subscriber.save()

    logger.debug(subscriber)

    return JsonResponse(subscriber)

def list(request):
    """
    List subscribers
    """
    subscribers = Subscriber.objects.all()

    return JsonResponse(dict(subscribers))
