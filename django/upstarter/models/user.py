from django.db import models

from authentication.models import BaseUser


class User(BaseUser):
    birthday = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=256, blank=True)
    skills = models.CharField(max_length=1024, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
