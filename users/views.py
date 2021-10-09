from django.shortcuts import render,reverse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
# Create your views here.

class UserSignupView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreationForm

    def get_success_url(self):
        return reverse("home")