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
    model=User
    template_name="users/profile.html"
    context_object_name="userprofile"
    slug_url_kwarg="username"
    slug_field="username"

    def get_context_data(self,**kwargs):
        context=super(UserProfileView,self).get_context_data(**kwargs)
        publishers=self.get_object().PublisherModel_User.all()              
        context["publishers"]=publishers
        return context
    



def testprofile(request):
    return render(request,"users/profile.html")