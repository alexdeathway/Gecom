from django.shortcuts import render
from games.models import GamesModel
from games.models import CategoryModel
from django.views.generic import ListView
from django.http import Http404

class HomeView(ListView):
    template_name="home.html"
    context_object_name="games"
    queryset=GamesModel.objects.all()[:8]

    def get_context_data(self,**kwargs):
            context=super(HomeView,self).get_context_data(**kwargs)
            try:              
                context["latest_release"]=GamesModel.objects.latest('release_date')
                context["games_sales"]=GamesModel.objects.filter(sale=True)[:3]
                context["categories"]=CategoryModel.objects.all()[:4] 
            except IndexError:
                raise Http404("Homepage data missing,create superuser and dummy data in database!")
            return context

#def index(request):
#    return render(request,"index.html")