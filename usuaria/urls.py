from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import dashboard_view

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard")
]

