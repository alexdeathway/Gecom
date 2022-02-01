from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

# Create your models here.

class User(AbstractUser):
    is_organiser=models.BooleanField(default=False)
    bio=models.CharField(max_length=80,null=True)
    profile_image=models.ImageField(default="default_profile_image.jpg", upload_to="profile_image", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f"{self.username}"


