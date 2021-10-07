from django.shortcuts import render
from games.models import GamesModel
from django.views.generic import ListView


class HomeView(ListView):
    template_name="home.html"
    queryset=GamesModel.objects.all()

#def index(request):
#    return render(request,"index.html")