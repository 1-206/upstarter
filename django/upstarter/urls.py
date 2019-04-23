from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('authentication/', include('authentication.urls')),

    path('', RedirectView.as_view(pattern_name='project-list'), name='index'),

    path('projects/', views.list_all_projects, name='project-list'),
    path('projects/<int:id>/', views.list_all_projects, name='project-detail'),
    path('projects/create/', views.create_project, name='project-create'),
    path('projects/personal/', views.list_personal_projects,
         name='personal-project-list'),

    path('personal/', views.personal, name='personal'),
]
