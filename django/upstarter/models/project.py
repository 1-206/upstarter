from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.CharField(max_length=1024, blank=True)
    required_investments = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)

    founder = models.ForeignKey(
        'User',
        related_name='founded_projects',
        on_delete=models.CASCADE,
    )

    cofounders = models.ManyToManyField(
        'User', related_name='cofounded_projects',
    )

    @property
    def raised(self):
        total = sum(i.amount for i in self.investments.all())
        return total

    def __str__(self):
        return f'{self.name}'


class Investment(models.Model):
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(
        Project,
        related_name='investments',
        on_delete=models.DO_NOTHING,
    )

    investor = models.ForeignKey(
        'User',
        related_name='investments',
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f'from {self.investor} to {self.project}'
