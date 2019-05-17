from django.urls import path
from .views import *

urlpatterns = [
	path('blog-list', BlogList.as_view(), name='blog_list'),
]
