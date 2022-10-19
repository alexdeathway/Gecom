"""seco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from seco.views import HomeView
from users.views import UserSignupView
from django.contrib.auth.views import (
                                        LoginView,
                                        LogoutView,
                                        PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView,
                                      )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(),name="home"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('signup/',UserSignupView.as_view(),name="signup"),
    path('reset-password/',PasswordResetView.as_view(),name="reset-password"), 
    path('reset-password-done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset-password-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset-password-complete/',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('games/',include('games.urls',namespace='games')),
    path('users/',include('users.urls',namespace='users')),
    path('components/',include('components.urls',namespace='components')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    django_toolbar_panel = [
        path('__debug__/', include(debug_toolbar.urls),)
        ] 
    urlpatterns = urlpatterns + django_toolbar_panel