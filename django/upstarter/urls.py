from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('authentication/', include('authentication.urls')),

    path('', RedirectView.as_view(pattern_name='personal-project-list'),
         name='index'),

    path('projects/', views.personal_project_list,
         name='personal-project-list'),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),
    path('projects/create/', views.project_create, name='project-create'),
    path('projects/search/', views.project_search, name='project-search'),

    path('profile/', views.personal, name='personal'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
]
