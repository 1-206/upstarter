from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    path('authentiation/', include('authentication.urls')),
    path('admin/', admin.site.urls, name='admin'),
]
