from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from users.models import User
User=get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        labels={
            "password2":"confirm password"
        }
        fields=[
            "username",
            "profile_image",
            "bio",
            "email",
            "password1",
            "password2",
        ]

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model =User
        fields=[
            "username",
            "profile_image",
            "email",
            "bio",
        ]
