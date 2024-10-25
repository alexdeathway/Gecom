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
   def clean_username(self):
        username= self.cleaned_data['username']
        if not re.match(r'^[0-9a-z]*$',username) or username.lower() != username:
                raise forms.ValidationError("Sorry , username can contain only lower case alphabets and numbers") 
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
   def clean_username(self):
        username= self.cleaned_data['username']
        if not re.match(r'^[0-9a-z]*$',username):
                raise forms.ValidationError("Sorry , username can contain only lower case alphabets and numbers") 
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
