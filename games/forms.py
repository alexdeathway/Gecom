from django import forms
from games.models import GamesModel,PublisherModel


class GameCreationForm(forms.ModelForm):
      
      def __init__(self,*args, **kwargs):
            request=kwargs.pop("request")
            publisher=PublisherModel.objects.filter(owner=request.user)
            super(GameCreationForm,self).__init__(*args,**kwargs)
            self.fields["publisher"]=forms.ModelChoiceField(queryset=publisher)
               
      class Meta:
         model=GamesModel
         labels={
            "sale": "Allot for new release sale?",
        }
         fields=[
            "name",
            "category",
            "cover",
            "price",
            "sale",
            "discription",
            "publisher"      
         ]

         

class PublisherCreationForm(forms.ModelForm):

   class Meta:
      model=PublisherModel
      labels={
            "name": "Publisher/Organisation name",
            "email":"Publisher/Organisation email",
        }
      
      fields=[
         "name",
         "email",
      ]         