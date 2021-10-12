from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

# Create your models here.

class User(AbstractUser):
    is_publisher=models.BooleanField(default=False)
    is_vendor=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"


