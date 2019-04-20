from django.db import models
from .user import User



class Tag(models.Model):
    name = models.CharField(max_length=128)


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    creation_date = models.DateTimeField(auto_now_add=True)
    founder = models.ForeignKey(User, related_name='founded_projects', on_delete=models.CASCADE)
    cofounders = models.ManyToManyField(User, related_name='cofounded_projects')
    performers = models.ManyToManyField(User, related_name='performed_projects')
    required_investments = models.FloatField()


class Investment(models.Model):
    investor = models.ForeignKey(User, related_name='investments', on_delete='DO_NOTHING')
    project = models.ForeignKey(Project, related_name='investments', on_delete='DO_NOTHING')
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
