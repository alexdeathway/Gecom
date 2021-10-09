from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

# Create your models here.

class User(AbstractUser):
    is_publisher=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"

class PublisherModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f"{self.name}"
