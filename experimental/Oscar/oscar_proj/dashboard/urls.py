from django.urls import path
from .views import actual_order_refund, actual_order_dispatch, fraud_alert

urlpatterns = [
    path('dashboard/orders/refund/', actual_order_refund, name='actual-order-refund'),
    path('dashboard/orders/dispatch/', actual_order_dispatch, name='actual-order-dispatch'),
    path('dashboard/orders/fraud-alert/', fraud_alert, name='fraud-alert'),
]
