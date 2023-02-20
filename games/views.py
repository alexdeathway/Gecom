from django.http.response import Http404
from django.shortcuts import render,reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                            CreateView,
                            ListView,
                            DetailView,                    
                                )
from django.views.generic.edit import UpdateView
from .models import CategoryModel, GamesModel, OrganisationModel
from django.contrib import messages
from games.forms import ( 
                            GameCreationForm,
                            OrganisationCreationForm,
                            OrganisationUpdateForm,
                            GameUpdateForm,
                        )    
from games.models import OrganisationModel

class GamesListView(ListView):
    template_name="games/games_list.html"
    context_object_name="games"
    paginate_by=15
    queryset=GamesModel.objects.all()


class GamesDetailView(DetailView):
      template_name="games/games_detail.html"
      context_object_name="game"
      model=GamesModel


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
        return reverse("games:gamedetail",kwargs={"pk":self.get_object().id})

class OrganisationCreateView(LoginRequiredMixin ,CreateView):
    template_name="games/organisation_create.html"
    form_class=OrganisationCreationForm
    model=OrganisationModel
    
    def form_valid(self,form):
        organisation = form.save(commit=False)
        organisation.owner = self.request.user
        organisation.save()

        return super(OrganisationCreateView,self).form_valid(form)

    def get_success_url(self):
         return reverse("games:publisherdetail",kwargs={"pk":self.get_object().id})

class PublisherDetailView(DetailView):
    template_name="games/publisher_detail.html"
    model=OrganisationModel
    context_object_name="publisher"
    slug_url_kwarg = "username"
    slug_field = "username"

    def get_context_data(self,**kwargs):
        context=super(PublisherDetailView,self).get_context_data(**kwargs)
        games=self.get_object().GameModel_OrganisationModel.all()              
        context["games"]=games
        return context

class CategoryDetailView(DetailView):
    template_name="games/category_detail.html"
    model=CategoryModel
    context_object_name="category"
    slug_url_kwarg = "name"
    slug_field = "name"

    def get_context_data(self,**kwargs):
        context=super(CategoryDetailView,self).get_context_data(**kwargs)
        games=self.get_object().GameModel_CategoryModel.all()              
        context["games"]=games
        return context


class OrganisationUpdateView(LoginRequiredMixin,UpdateView):
    template_name="games/organisation_update.html"
    #form_class=UserUpdateForm
    model=OrganisationModel
    form_class=OrganisationUpdateForm
    # slug_url_kwarg="username"
    # slug_field="username"
    
    def dispatch(self, request, *args, **kwargs):
        organisation=self.get_object()
        if organisation.owner != self.request.user:
            raise Http404("Knock knock , Not you!")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        messages.success(self.request,"successfully update")
        return super(OrganisationUpdateView,self).form_valid(form) 

    def get_success_url(self):
         return reverse("games:publisherdetail",kwargs={"pk":self.get_object().id})

class GameUpdateView(LoginRequiredMixin,UpdateView):
    template_name="games/game_update.html"
    model=GamesModel
    form_class=GameUpdateForm
    # slug_url_kwarg="username"
    # slug_field="username"
    
    def get_form_kwargs(self,**kwargs):
        kwargs=super(GameUpdateView,self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request
        })
        return kwargs

    def form_valid(self,form):
        messages.success(self.request,"successfully update")
        return super(GameUpdateView,self).form_valid(form) 
    
    def dispatch(self, request, *args, **kwargs):
        game=self.get_object()
        if game.publisher.owner != self.request.user:
            raise Http404("Knock knock , Not you!")
        return super().dispatch(request, *args, **kwargs)
    
    

    def get_success_url(self):
        return reverse("games:gamedetail",kwargs={"pk":self.get_object().id})
