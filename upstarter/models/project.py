from django.db import models
from .user import User



class Tag(models.Model):
    name = models.CharField(max_length=128)


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    founder = models.ForeignKey(User, related_name='founded_projects', on_delete=models.CASCADE)
    cofounders = models.ManyToManyField(User, related_name='cofounded_projects', blank=True)
    performers = models.ManyToManyField(User, related_name='performed_projects', blank=True)
    required_investments = models.FloatField()

    @property
    def raised(self):
        total = sum([i.amount for i in self.investments])
        return total


class Investment(models.Model):
    investor = models.ForeignKey(User, related_name='investments', on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, related_name='investments', on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
