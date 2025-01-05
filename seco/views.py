from django.shortcuts import render
from games.models import GamesModel,CategoryModel
from misc.models import ReviewModel
from django.views.generic import ListView
from django.http import Http404

class HomeView(ListView):
    template_name="home.html"
    context_object_name="games"
    queryset=GamesModel.objects.all()[:9]

    def get_context_data(self,**kwargs):
            context=super(HomeView,self).get_context_data(**kwargs)
            try:              
                context["latest_releases"]=GamesModel.objects.order_by('-release_date')[:4]
                context["games_sales"]=GamesModel.objects.filter(sale=True)[:3]
                context["categories"]=CategoryModel.objects.all()[:4]
                context["reviews"]=ReviewModel.objects.all()[:8]
            except IndexError:
                raise Http404("Homepage data missing,create superuser and dummy data in database!")
            return context


def error_404(request,exception):
    return render(request,"errors/404.html",status=404)

def error_500(request):
    return render(request,"errors/500.html",status=500)
