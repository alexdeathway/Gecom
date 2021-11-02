from django import forms
from games.models import GamesModel, OrganisationModel


class GameCreationForm(forms.ModelForm):
      
      def __init__(self,*args, **kwargs):
            request=kwargs.pop("request")
            publisher=OrganisationModel.objects.filter(owner=request.user)
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

         

class OrganisationCreationForm(forms.ModelForm):

   class Meta:
      model=OrganisationModel
      labels={
            "name": "Organisation name",
            "email":"Organisation email",
        }
      
      fields=[
         "name",
         "email",
      ]         