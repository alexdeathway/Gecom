from django.shortcuts import render,reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                            CreateView,
                            ListView,
                            DetailView,                    
                                )
from .models import ComponentsModel,ComponentCategoryModel
from games.models import OrganisationModel
from .forms import ComponentCreationForm

class ComponentsListView(ListView):
    template_name="components/components_list.html"
    context_object_name="components"
    paginate_by=16
    queryset=ComponentsModel.objects.all()


class ComponentsDetailView(DetailView):
      template_name="components/components_detail.html"
      context_object_name="component"
      model=ComponentsModel


class ComponentCreateView(LoginRequiredMixin ,CreateView):
    template_name="components/components_create.html"
    form_class=ComponentCreationForm

    def get_form_kwargs(self,**kwargs):
        kwargs=super(ComponentCreateView,self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("components:components")




class ComponentCategoryDetailView(DetailView):
    template_name="components/component_category_detail.html"
    model=ComponentCategoryModel
    context_object_name="category"
    slug_url_kwarg = "name"
    slug_field = "name"

    def get_context_data(self,**kwargs):
        context=super(ComponentCategoryDetailView,self).get_context_data(**kwargs)
        components=self.get_object().ComponentsModel_ComponentCategoryModel.all()              
        context["components"]=components
        return context

