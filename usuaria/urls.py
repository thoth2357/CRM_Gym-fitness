from django.urls import path, include
from .views import login, register


urlpatterns = [
    path('acceso/', login, name='login'),
]
