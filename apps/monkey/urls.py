from django.conf.urls import url
from . import views

# all of our routes for monkey
urlpatterns = [
    # localhost:8000/
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^monkey$', views.monkey),
    # localhost:8000/monkey/:monkey_id
    url(r'^monkey/(?P<monkey_id>[0-9]+)$', views.show),
    # localhost:8000/monkey/:monkey_name
    url(r'^monkey/(?P<monkey_name>[A-Za-z]+)$', views.name),
    url(r'^dashboard$', views.dashboard),
    url(r'^create/post$', views.newPost)
]
