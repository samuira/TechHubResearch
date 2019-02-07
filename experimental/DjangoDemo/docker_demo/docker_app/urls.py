from django.urls import path
from .views import docker_app

urlpatterns = [
    path('', docker_app, name='docker_app'),
]
