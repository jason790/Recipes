from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.start_here, name='start_here')
]
