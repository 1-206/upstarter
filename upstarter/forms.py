from django import forms



class ProjectCreationForm(forms.Form):

    name = forms.CharField(
            label="Name",
            required=True
            )
    description = forms.TextField(
            label="Description",
            required=True
            )
    required_investments = forms.FloatField(
            label="Required investments",
            required=True,
            )

    def clean(self):
        cleaned_data = super().clean()
        required_investments = cleaned_data.get('required_investments')

        if required_investments < 0:
            self.add_error(
                'required_investments',
                "Must be positive or 0"
            )

        return cleaned_data

