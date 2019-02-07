from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def docker_app(request):
    return render(request, 'docker_app/docker_page.html', {'status':'ok'})