from django.conf.urls import url
from . import views

# all of our routes for monkey
urlpatterns = [
    # localhost:8000/
    url(r'^$', views.index),
    # localhost:8000/monkey/banana
    url(r'^monkey$', views.monkey),
    # localhost:8000/monkey/:monkey_id
    url(r'^monkey/(?P<monkey_id>[0-9]+)$', views.show),
    # localhost:8000/monkey/:monkey_name
    url(r'^monkey/(?P<monkey_name>[A-Za-z]+)$', views.name)
]