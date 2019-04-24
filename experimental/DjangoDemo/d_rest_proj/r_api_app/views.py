from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hi there</h1>')