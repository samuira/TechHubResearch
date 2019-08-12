from django.urls import path
from .views import ImageAnalysisView, ImageListView

urlpatterns = [
	path('', ImageAnalysisView.as_view(), name='image_analysis'),
	path('img-list/', ImageListView.as_view(), name='img_list'),
]