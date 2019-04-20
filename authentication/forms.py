from django import forms


class AuthorizationForm(forms.Form):
    email = forms.CharField(label="Email",
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'type': 'email',
                                                          'id': 'email',
                                                          'placeholder': 'Email'})
                            )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': "form-control",
                                          'type': 'password',
                                          'id': 'password',
                                          'placeholder': 'Password'})
    )


class RegistrationForm(forms.Form):
    USER_TYPES = (
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Admin', 'Admin'),
    )

    name = forms.CharField(
        label="Name",
        required=True,
        widget=forms.TextInput(attrs={'type': "name",
                                      'class': 'form-control mr-2',
                                      'id': "name",
                                      'placeholder': "Name"})
    )
    surname = forms.CharField(
        label="Surname",
        required=True,
        widget=forms.TextInput(attrs={'type': "surname",
                                      'class': "form-control",
                                      'id': "surname",
                                      'placeholder': "Surname"})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control",
                                      'type': 'email',
                                      'id': 'email',
                                      'placeholder': 'Email'})
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={'class': "form-control",
                                          'type': 'password',
                                          'id': 'password',
                                          'placeholder': 'Password'})
    )
    password_repeat = forms.CharField(
        label="Repeat password",
        required=True,
        widget=forms.PasswordInput(attrs={'class': "form-control",
                                          'type': 'password',
                                          'id': 'repeat',
                                          'placeholder': 'Repeat password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            self.add_error(
                'password_repeat',
                "Passwords do not match"
            )

        return cleaned_data
