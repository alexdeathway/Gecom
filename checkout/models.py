from django.db import models
from django.contrib.auth import get_user_model
from games.models import GamesModel
from components.models import ComponentsModel

User=get_user_model()



class CartGameItemModel(models.Model):
      buyer=models.ForeignKey(User, on_delete=models.CASCADE,related_name="BoughtModel_User")
      game=models.ForeignKey(GamesModel, on_delete=models.CASCADE,related_name="BoughtModel_GamesModel")
      
      def __str__(self):
          return f"{self.buyer} bought game: {self.game}"


class CartComponentItemModel(models.Model):
      buyer=models.ForeignKey(User, on_delete=models.CASCADE,related_name="CartComponentItemModel_User")
      component=models.ForeignKey(ComponentsModel, on_delete=models.CASCADE,related_name="CartComponentItemModel_ComponentModel")
      
      def __str__(self):
          return f"{self.buyer} bought component: {self.component}"
      

