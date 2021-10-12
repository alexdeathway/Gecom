from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
# Create your models here.

# User=get_user_model()

class VendorModel(models.Model):
    
    name=models.CharField(unique=True,max_length=50)
    email=models.EmailField(max_length=254)