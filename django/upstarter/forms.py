from django.forms import ModelForm

from .models import Project, Investment


class ProjectCreationForm(ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'tags', 'required_investments')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ProjectInvestmentForm(ModelForm):

    class Meta:
        model = Investment
        fields = ('amount',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
