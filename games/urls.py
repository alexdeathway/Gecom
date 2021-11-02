from django.urls import path
from .views import (
                   GamesListView,
                   GamesCreateView,
                   OrganisationCreateView,
                   GamesDetailView,
                   PublisherDetailView,
                   CategoryDetailView,
                    )

app_name="games"


urlpatterns = [
    path('',GamesListView.as_view(),name="games"),
    path('create/', GamesCreateView.as_view(),name="gamecreate"),
    path('organisation/create/', OrganisationCreateView.as_view(),name="organisationcreate"),
    path('<int:pk>/',GamesDetailView.as_view(),name="gamedetail"),
    path("publisher/<str:name>/",PublisherDetailView.as_view(),name="publisherdetail"),
    path("category/<str:name>/",CategoryDetailView.as_view(),name="categorydetail"),
]