from django.db import models

from authentication.models import BaseUser


class Skill(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class User(BaseUser):
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='users')
