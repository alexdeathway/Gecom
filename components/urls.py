from django.urls import path
from components.views import component 
app_name="components"

urlpatterns = [
    path('', component,name="component"),
]