from django.shortcuts import render
from oscar.apps.promotions.views import HomeView
from oscar.apps.catalogue.models import Product
from django.db.models import Q


# Create your views here.
class HomeView(HomeView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['products'] = Product.objects.filter(Q(structure='standalone') | Q(structure='parent'))
        print(context['products'])
        return context
