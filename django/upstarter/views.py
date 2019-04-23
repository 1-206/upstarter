from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from upstarter.forms import ProjectCreationForm, ProjectInvestmentForm
from upstarter.models import Project, User
from upstarter.documents import ProjectDocument


def require_authentication(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return function(request, *args, **kwargs)
    return wrapper


@require_authentication
def personal_project_list(request):
    founded_projects = request.user.founded_projects.all()
    cofounded_projects = request.user.cofounded_projects.all()
    context = {
        'user': request.user,
        'founded_projects': founded_projects,
        'cofounded_projects': cofounded_projects,
    }
    return render(request, 'upstarter/personal_project_list.html', context)


@require_authentication
def project_detail(request, pk):
    RELEVANT_PROJECTS_AMOUNT = 3
    project = get_object_or_404(Project, pk=pk)
    # Use elasticsearch for relevant documents searching
    search = ProjectDocument.search()
    query = search.query(
        'more_like_this', fields=['name', 'description', 'tags'],
        like={'_id': project.id}, min_term_freq=1, min_doc_freq=1,
        max_query_terms=200, minimum_should_match='5%',
    )
    relevant_projects = query.to_queryset()[:RELEVANT_PROJECTS_AMOUNT]
    # Context initialization
    context = {
        'user': request.user,
        'project': project,
        'relevant_projects': relevant_projects,
    }
    return render(request, 'upstarter/project_detail.html', context)


@require_authentication
def project_create(request):
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.founder = request.user
            project.save()
            redirect_url = reverse('project-detail', kwargs={'pk': project.pk})
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProjectCreationForm()

    context = {'user': request.user, 'form': form}
    return render(request, 'upstarter/project_create.html', context)


@require_authentication
def project_search(request):
    return


@require_authentication
def personal(request):
    context = {'user': request.user}
    return render(request, 'upstarter/user.html', context)


@require_authentication
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'user': user}
    return render(request, 'upstarter/user.html', context)


@require_authentication
def investment_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectInvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.investor = request.user
            investment.project = project
            investment.save()
            redirect_url = reverse('project-detail', kwargs={'pk': pk})
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProjectCreationForm()

    context = {'user': request.user, 'form': form}
    return render(request, 'upstarter/investment_create.html', context)
