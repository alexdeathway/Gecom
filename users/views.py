from django.http.response import Http404
from django.shortcuts import render,reverse,redirect
from django.views.generic import CreateView,DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm,UserUpdateForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib import messages
User=get_user_model()


class UserSignupView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreationForm
    
    def form_valid(self,form):
        user_Email=form.data['email']
        send_mail(
            "test subject",
            "this is test email for signup",
            "admin@gecom.com",
            [user_Email],
        )

        return super(UserSignupView,self).form_valid(form)

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
        organisation=self.get_object().OrganisationModel_User.all()              
        context["organisation"]=organisation
        return context

    

class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
    template_name="users/user_update.html"
    #form_class=UserUpdateForm
    model=User
    form_class=UserUpdateForm
    slug_url_kwarg="username"
    slug_field="username"
    
    def dispatch(self, request, *args, **kwargs):
        profile=self.get_object()
        if profile != self.request.user:
            raise Http404("Knock knock , Not you!")
        return super().dispatch(request, *args, **kwargs)
    
    # def form_valid(self):
    #     messages.success(self.request, f"Account updated successfully")
    #     return super(UserProfileUpdateView,self).form_valid(form)


    def get_success_url(self):
        return reverse("home")

def make_organiser(request):
   user = User.objects.get(username=request.user.username)
   user.is_organiser = True
   user.save()
   profile_url = reverse('users:profile', kwargs={'username': request.user.username})
   return redirect(profile_url)