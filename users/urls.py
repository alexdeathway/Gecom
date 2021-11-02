from django.urls import path
from .views import UserProfileView , testprofile
app_name="users"

urlpatterns = [
    path("<str:username>/",UserProfileView.as_view(),name="profile")
]

