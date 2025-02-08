from django.conf import settings
from django.db import models


# Create your models here.
class Position(models.Model):
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    lead = models.CharField(max_length=200)
    start_date = models.DateField()
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company_name} - {self.role}'


class Note(models.Model):
    description = models.CharField(max_length=500)
    happened_at = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return f'{self.happened_at}: {self.position} - {self.description[:20]}'
