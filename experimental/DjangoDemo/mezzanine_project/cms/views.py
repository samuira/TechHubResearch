from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Index(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')