from django.shortcuts import render,reverse
from django.views.generic import (
                            CreateView,                    
                                )

from games.forms import GameCreationForm

class GamesCreateView(CreateView):
    template_name="games/games_create.html"
    form_class=GameCreationForm

    def get_success_url(self):
        return reverse("home")


