from django.db import models
from django.contrib.auth import get_user_model
from games.models import OrganisationModel
# Create your models here.

User=get_user_model()

class ComponentsModel(models.Model):
    name=models.CharField(max_length=50)
    cover=models.ImageField(default="default_cover.jpg", upload_to="components_cover")
    price=models.PositiveIntegerField(default=0)
    description=models.CharField(max_length=50)
    vendor=models.ForeignKey(OrganisationModel, on_delete=models.CASCADE,related_name="ComponentsModel_OrganisationModel")
    category=models.ForeignKey("ComponentCategoryModel",null=True,blank=True,on_delete=models.SET_NULL,related_name="ComponentsModel_ComponentCategoryModel")

    def __str__(self):
        return f"{self.name}"



class ComponentCategoryModel(models.Model):
    name=models.CharField(max_length=20,unique=True)
    cover=models.ImageField(default="default_category_cover.jpg",upload_to="component_category_cover")
    
    
    def __str__(self):
        return self.name
