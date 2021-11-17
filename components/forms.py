from django import  forms
from .models import ComponentsModel
from games.models import  OrganisationModel


class ComponentCreationForm(forms.ModelForm):
      
      def __init__(self,*args, **kwargs):
            request=kwargs.pop("request")
            vendor=OrganisationModel.objects.filter(owner=request.user)
            super(ComponentCreationForm,self).__init__(*args,**kwargs)
            self.fields["vendor"]=forms.ModelChoiceField(queryset=vendor)
               
      class Meta:
         model=ComponentsModel
         labels={
            "vendor": "Vendor or your organisation",
        }
         fields=[
            "name",
            "category",
            "cover",
            "price",
            "description",
            "vendor"      
         ]

class ComponentUpdateForm(forms.ModelForm):
      
      def __init__(self,*args, **kwargs):
            request=kwargs.pop("request")
            vendor=OrganisationModel.objects.filter(owner=request.user)
            super(ComponentUpdateForm,self).__init__(*args,**kwargs)
            self.fields["vendor"]=forms.ModelChoiceField(queryset=vendor)
               
      class Meta:
         model=ComponentsModel
         labels={
            "vendor": "Vendor or your organisation",
        }
         fields=[
            "name",
            "category",
            "cover",
            "price",
            "description",
            "vendor"      
         ]
