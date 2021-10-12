from django.shortcuts import render,reverse
from django.views.generic import CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.

class UserSignupView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreationForm

    def get_success_url(self):
        return reverse("home")

class UserProfileView(LoginRequiredMixin ,DetailView):
    template_name="users/profile.html"
    context_object_name="userprofile"
    
    def get_queryset(self):
        user=self.request.user.pk
        queryset=User.objects.get(id=user)

        return queryset



def testprofile(request):
    return render(request,"users/profile.html")