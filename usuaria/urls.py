from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from .views import dashboard_view

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    # path('/', home_view, name="homepage"),
    path('', lambda request: redirect('accounts/login', permanent=True)), #temporary redirect for homepage for now
]

