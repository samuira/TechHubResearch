from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def index(request):
	return render(request, 'custom_admin/dashboard.html')
