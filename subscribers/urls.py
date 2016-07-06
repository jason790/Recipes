from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create.json$', views.create, name='create'),
    url(r'^all.json$', views.list, name='all'),
]
