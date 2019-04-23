from django.forms import ModelForm

from .models import Project, Investment


class ProjectCreationForm(ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'tags', 'required_investments')


class ProjectInvestmentForm(ModelForm):

    class Meta:
        model = Investment
        fields = ('amount',)
