from django.shortcuts import render
from games.models import GamesModel
from games.models import CategoryModel
from django.views.generic import ListView


class HomeView(ListView):
    template_name="home.html"
    context_object_name="games"
    queryset=GamesModel.objects.all()[:8]

    def get_context_data(self,**kwargs):
            context=super(HomeView,self).get_context_data(**kwargs)              
            context["latest_release"]=GamesModel.objects.all().order_by('-release_date')[1]
            context["games_sales"]=GamesModel.objects.filter(sale=True)[:3]
            context["categories"]=CategoryModel.objects.all()[:4] 
            return context

#def index(request):
#    return render(request,"index.html")