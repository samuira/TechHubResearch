from django.urls import path
from .views import order_refund_view

urlpatterns = [
    path('accounts/orders/refund/', order_refund_view, name='order-line-refund'),
]
