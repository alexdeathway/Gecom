import re
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
            "description",
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
         "username",
         "email",
      ]
   def clean_code_name(self):
        username= self.cleaned_data['username']
        if not re.match(r'^[0-9a-zA-Z]*$',username) or username.lower() != username:
                raise forms.ValidationError("Sorry , you can only have lower alphanumeric in username") 
        return username     

class OrganisationUpdateForm(forms.ModelForm):

   class Meta:
      model=OrganisationModel
      labels={
            "name": "Organisation name",
            "email":"Organisation email",
        }
      
      fields=[
         "name",
         "logo",
         "username",
         "email",
         "about",

      ]
   def clean_code_name(self):
        username= self.cleaned_data['username']
        if not re.match(r'^[0-9a-zA-Z]*$',username):
                raise forms.ValidationError("Sorry , you can only have alphanumeric in username") 
        return username   

class GameUpdateForm(forms.ModelForm):
      
      def __init__(self,*args, **kwargs):
            request=kwargs.pop("request")
            publisher=OrganisationModel.objects.filter(owner=request.user)
            super(GameUpdateForm,self).__init__(*args,**kwargs)
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
            "description",
            "publisher"      
         ]
