#from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from users.models import User
User=get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        labels={
            "is_publisher":"Are you publisher ?"
        }
        fields=[
            "username",
            "email",
            "password1",
            "password2",
            "is_publisher" 
        ]
