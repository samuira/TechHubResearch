# yourproject/catalogue/models.py

from django.db import models

from oscar.apps.order.abstract_models import AbstractOrder, AbstractLine


class Order(AbstractOrder):
    plan_id = models.CharField(max_length=20, default='')
    is_dispatched = models.CharField(max_length=10, default='0', help_text='0=No, 1=Yes')
    is_refund_all = models.CharField(max_length=10, default='0',
                                     help_text='0=No, '
                                               '1=Yes')
    is_alert_send = models.CharField(max_length=10, default='0', help_text='0=No, 1=Yes')
    refund_amount = models.FloatField(default=0.00)

from oscar.apps.order.models import *