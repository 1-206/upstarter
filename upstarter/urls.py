from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/projects/'), name='index'),
    path('projects/', views.list_all_projects, name='projects'),
    path('projects/<int:id>/', views.list_all_projects, name='project'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/personal/', views.list_personal_projects, name='personal_project'),
    path('personal/', views.personal, name='personal'),

    path('authentication/', include('authentication.urls')),
    path('admin/', admin.site.urls, name='admin'),
]