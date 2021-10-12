from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
# Create your models here.

User=get_user_model()

class GamesModel(models.Model):
    name=models.CharField(max_length=30)
    cover=models.ImageField(default="default_cover.jpg", upload_to="games_cover")
    category=models.ForeignKey('CategoryModel',null=True,blank=True,on_delete=models.SET_NULL,related_name="GameModel_CategoryModel")
    price=models.PositiveIntegerField ()
    discription=models.CharField(max_length=500)
    sale=models.BooleanField(default=False)
    publisher=models.ForeignKey('PublisherModel',on_delete=models.CASCADE,related_name="GameModel_PublisherModel")
    release_date=models.DateField(auto_now=True) 

    def __str__(self):
        return self.name

class PublisherModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=True)
    email=models.EmailField(blank=True, max_length=50)

    def __str__(self):
        return f"{self.name}"


class CategoryModel(models.Model):
    name=models.CharField(max_length=20,unique=True)
    cover=models.ImageField(default="default_category_cover.jpg",upload_to="category_cover")
    def __str__(self):
        return self.name
