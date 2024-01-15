from django.urls import path
from misc.views import DevelopmentStatusView

app_name="misc"

urlpatterns=[
     path('development-status/',DevelopmentStatusView.as_view(),name="development-status"),
]