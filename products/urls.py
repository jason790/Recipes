from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^/products/(?P<id>[0-9]+)/?$', views.show, name='show'),
url(r'^/products', views.index, name='index'),
url(r'^/$', views.index, name='index'),
]
