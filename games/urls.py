from django.urls import path
from .views import (
                   GamesCreateView,
                    )

app_name="games"


urlpatterns = [
    path('create', GamesCreateView.as_view(),name="gamecreate"),
]