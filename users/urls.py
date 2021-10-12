from django.urls import path
from .views import UserProfileView , testprofile
app_name="users"

urlpatterns = [
    path("",testprofile,name="profile")
]

