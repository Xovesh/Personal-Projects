from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokedex, name="pokedex"),
    path('pokemon/<pname>', views.details, name="details"),
]
