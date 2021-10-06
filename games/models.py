from django.db import models
from django.db.models.base import Model

# Create your models here.

class GamesModel(models.Model):
    name=models.CharField(max_length=30)
    cover=models.ImageField()
    price=models.IntegerField()
    discription=models.CharField(max_length=500)
    publisher=models.CharField(max_length=50)
    release_date=models.DateField() 

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name