from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=155)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title