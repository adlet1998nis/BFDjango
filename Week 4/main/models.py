from django.db import models

# Create your models here.
from django.db.models import CharField


class Owner(models.Model):
    type = models.CharField(max_length = 100)
    def __str__(self):
        return self.type

class Task(models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateField()
    due_to = models.DateField()
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    mark = models.BooleanField()
    def __str__(self):
        return '{} {}'.format(self.name, self.owner)



