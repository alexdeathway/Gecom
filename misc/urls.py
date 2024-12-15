from django.urls import path
from misc.views import DevelopmentStatusView,Error404TestView,Error500TestView
from django.conf import settings

app_name="misc"

urlpatterns=[
     path('development-status/',DevelopmentStatusView.as_view(),name="development-status"),
]

#error pages in the development environment
if settings.DEBUG:
    urlpatterns+=[
        path('404/',Error404TestView.as_view(),name="error404"),
        path('500/',Error500TestView.as_view(),name="error500"),
    ]