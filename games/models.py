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
    publisher=models.ForeignKey('OrganisationModel',on_delete=models.CASCADE,related_name="GameModel_OrganisationModel")
    release_date=models.DateField(auto_now=True) 
    
    @property
    def all_image(self):
        return GameImageModel.objects.filter(game=self)

    def __str__(self):
        return self.name

class OrganisationModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="OrganisationModel_User")
    name=models.CharField(max_length=50,unique=True)
    about=models.CharField(max_length=120, null=True,blank= True)
    username=models.CharField(max_length=20)
    email=models.EmailField(blank=True, max_length=50)

    def __str__(self):
        return f"{self.name}"

    
class CategoryModel(models.Model):
    name=models.CharField(max_length=20,unique=True)
    cover=models.ImageField(default="default_category_cover.jpg",upload_to="category_cover")
    description=models.CharField(null=True, max_length=400)
    def __str__(self):
        return self.name

class GameImageModel(models.Model):
    game=models.ForeignKey("GamesModel", on_delete=models.CASCADE,related_name="GameImageModel_GameModel")
    url=models.URLField(max_length=200)

    def __str__(self):
        return f"{self.game}'s image"

class BoughtModel(models.Model):
      buyer=models.ForeignKey(User, on_delete=models.CASCADE,related_name="BoughtModel_User")
      game=models.ForeignKey("GamesModel", on_delete=models.CASCADE,related_name="BoughtModel_GamesModel")
      
      def __str__(self):
          return f"{self.buyer} bought {self.game}"