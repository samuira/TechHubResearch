"""oscar_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from oscar.app import application
from oscarapi.app import application as api
from stores.app import application as stores_app
from stores.dashboard.app import application as dashboard_app
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', admin.site.urls),

    url(r'', application.urls),
    url(r'^api/', include('customer.urls')),
    url(r'^api/', include('dashboard.urls')),
    url(r'^api/', include('catalogue.urls')),
    path('oscarapi/', api.urls),

    # adds URLs for the dashboard store manager
    url(r'^dashboard/stores/', dashboard_app.urls),

    # adds URLs for overview and detail pages
    url(r'^stores/', stores_app.urls),

    # adds internationalization URLs
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name="javascript-catalogue"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)