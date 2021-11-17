from django.urls import path
from components.views import (
                                ComponentCategoryDetailView,
                                ComponentsListView,
                                ComponentsDetailView,
                                ComponentCreateView,
                                ComponentCategoryDetailView,
                                ComponentUpdateView
                            )    


app_name="components"

urlpatterns = [
    path('',ComponentsListView.as_view(),name="components"),
    path('<int:pk>/',ComponentsDetailView.as_view(),name="componentdetail"),
    path('<int:pk>/update/',ComponentUpdateView.as_view(),name="componentupdate"),
    path('create/',ComponentCreateView.as_view(),name="componentcreate"),
    path('category/<str:name>/',ComponentCategoryDetailView.as_view(),name="categorydetail"),
]