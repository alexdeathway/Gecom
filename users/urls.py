from django.urls import path
from .views import (
                        UserProfileView ,
                        UserProfileUpdateView,
                    )    
app_name="users"

urlpatterns = [
    path("<str:username>/",UserProfileView.as_view(),name="profile"),
    path("<str:username>/update/",UserProfileUpdateView.as_view(),name="profileupdate")
]

