from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
from django.core.serializers import serialize
import logging

from datetime import datetime
from django.utils import timezone

from .models import Subscriber

# Create your views here.
def create(request):
    """
    Create a new subscriber
    """
    logger = logging.getLogger(__name__)

    name = request.POST.get('name')
    email = request.POST.get('email')
    subscriber = Subscriber.objects.create(name=name, email=email, created_at=timezone.now())
    data = Subscriber.objects.filter(id=subscriber.id).values()

    return JsonResponse(dict(data=data[0]))

def list(request):
    """
    List subscribers
    """
    subscribers = Subscriber.objects.all()

    return JsonResponse(dict(data=serialize("json", subscribers)))
