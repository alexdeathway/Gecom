from django.shortcuts import render,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                            CreateView,                    
                                )

from games.forms import GameCreationForm,PublisherCreationForm

class GamesCreateView(LoginRequiredMixin ,CreateView):
    template_name="games/games_create.html"
    form_class=GameCreationForm

    def get_form_kwargs(self,**kwargs):
        kwargs=super(GamesCreateView,self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("home")

class PublisherCreateView(LoginRequiredMixin ,CreateView):
    template_name="games/publisher_create.html"
    form_class=PublisherCreationForm
    
    def form_valid(self,form):
        publisher = form.save(commit=False)
        publisher.owner = self.request.user
        publisher.save()

        return super(PublisherCreateView,self).form_valid(form)

    def get_success_url(self):
        return reverse("home")


