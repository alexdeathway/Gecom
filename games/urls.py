from django.urls import path
from .views import (
                   GamesListView,
                   GamesCreateView,
                   PublisherCreateView,
                   GamesDetailView,
                    )

app_name="games"


urlpatterns = [
    path('',GamesListView.as_view(),name="games"),
    path('create/', GamesCreateView.as_view(),name="gamecreate"),
    path('publisher/create/', PublisherCreateView.as_view(),name="publishercreate"),
    path('<int:pk>/',GamesDetailView.as_view(),name="gamedetail"),
]