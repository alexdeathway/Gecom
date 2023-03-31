from django.urls import path
from .views import (
                        UserProfileView ,
                        UserProfileUpdateView,
                        make_organiser,
                    )    
app_name="users"

urlpatterns = [
    path("make-organiser/",make_organiser,name="makeorganiser"),
    path("<str:username>/",UserProfileView.as_view(),name="profile"),
    path("<str:username>/update/",UserProfileUpdateView.as_view(),name="profileupdate"),
]

