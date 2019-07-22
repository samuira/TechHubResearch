from django.urls import path
from .views import get_stock_record

urlpatterns = [
    path('catalogue/stockrecord/', get_stock_record, name='get-stock-record'),
]
