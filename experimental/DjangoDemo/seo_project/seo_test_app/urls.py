from django.urls import path
from .views import seo_list, seo_create, seo_drug_edit, seo_liquor_edit, seo_drug_delete, seo_liquor_delete

urlpatterns = [
    path('', seo_list, name='seo_list'),
    path('seo_create', seo_create, name='seo_create'),
    path('seo_drug_edit/<int:id>', seo_drug_edit, name='seo_drug_edit'),
    path('seo_drug_delete/<int:id>', seo_drug_delete, name='seo_drug_delete'),
    path('seo_liquor_edit/<int:id>', seo_liquor_edit, name='seo_liquor_edit'),
    path('seo_liquor_delete/<int:id>', seo_liquor_delete, name='seo_liquor_delete'),
]
