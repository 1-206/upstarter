from django.db.models import Q
from .models import Project
from django.shortcuts import render
from django.urls import reverse
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
)

from django.contrib.auth import get_user_model
User = get_user_model()


def require_authorized(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return function(request, *args, **kwargs)
    return wrapper


@require_authorized
def list_all_projects(request):
    user = User.objects.get(pk=request.user.id)
    projects = Project.objects.all()
    data = {'user': user, 'projects': projects}
    return render(request, 'upstarter/search.html', data)


@require_authorized
def list_personal_projects(request):
    user = User.objects.get(pk=request.user.id)
    data = {
            'user': user,
            'founded': user.founded_projects,
            'cofounded': user.cofounded_projects,
            'performed': user.performed_projects,
            }
    return render(request, 'upstarter/personal_projects.html', data)


@require_authorized
def project(request, id):
    user = User.objects.get(pk=request.user.id)
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return HttpResponse('No such project')
    data = {'user': user, 'project': project}
    return render(request, 'upstarter/project.html', data)


@require_authorized
def create_project(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            id = Project.objects.create(
                    name=data['name'],
                    description=data['description'],
                    founder=user,
                    required_investments=data['required_investments']
                    )
            return HttpResponseRedirect(reverse('project', kwargs={'id': id}))
    else:
        form = ProjectCreationForm()

    data = {'user': user, 'form': form}
    return render(request, 'upstarter/project_creation.html', data)
