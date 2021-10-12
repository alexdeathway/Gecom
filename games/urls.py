from django.urls import path
from .views import (
                   GamesCreateView,
                   PublisherCreateView,
                    )

app_name="games"


urlpatterns = [
    path('create/', GamesCreateView.as_view(),name="gamecreate"),
    path('publisher/create/', PublisherCreateView.as_view(),name="publishercreate"),
]