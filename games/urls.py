from django.urls import path
from .views import (
                   GamesListView,
                   GamesCreateView,
                   OrganisationCreateView,
                   GamesDetailView,
                   PublisherDetailView,
                   CategoryDetailView,
                   OrganisationUpdateView,
                   GameUpdateView,
                   #below view are not fir for production 
                   DemoNoPaymentView,
                   user_cart_item_count,
                   UserCart
                    )

app_name="games"


urlpatterns = [
    path('',GamesListView.as_view(),name="games"),
    path('create/', GamesCreateView.as_view(),name="gamecreate"),
    path('organisation/create/', OrganisationCreateView.as_view(),name="organisationcreate"),
    path('<int:pk>/',GamesDetailView.as_view(),name="gamedetail"),
    path('<int:pk>/update/',GameUpdateView.as_view(),name="gameupdate"),
    path("publisher/<slug:username>/",PublisherDetailView.as_view(),name="publisherdetail"),
    path("organisation/<int:pk>/update/",OrganisationUpdateView.as_view(),name="organisationupdate"),
    path("category/<str:name>/",CategoryDetailView.as_view(),name="categorydetail"),
    path("nopurchase/",DemoNoPaymentView.as_view(),name="nopurchase"),
    path("usercart/",UserCart.as_view(),name="usercart"),
    path("usercartitemcount/",user_cart_item_count,name="usercartitemcount"),
]