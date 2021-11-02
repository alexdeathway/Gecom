from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

# Create your models here.

class User(AbstractUser):
    is_organiser=models.BooleanField(default=False)
    discription=models.CharField(max_length=80,null=True)

    def __str__(self):
        return f"{self.username}"


