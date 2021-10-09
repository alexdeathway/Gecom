from django import forms
from games.models import GamesModel

class GameCreationForm(forms.ModelForm):
    
     class Meta:
         model=GamesModel
         fields=[
            "name",
            "cover",
            "price",
            "discription",
         ]