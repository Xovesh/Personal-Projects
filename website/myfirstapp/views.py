from django.shortcuts import render
from .models import Pokemon
from django.http import HttpResponse
# Create your views here.

def index(request):
    all_pokemons = Pokemon.objects.all()
    context = {"all_pokemons" : all_pokemons}
    return render(request, "myfirstapp/pokedex.html", context)

def details(request, pname):
    try:
        pokemon = Pokemon.objects.all().filter(name=pname)
        context = {"pokemon": pokemon}
        return render(request, "myfirstapp/details.html", context)
    except:
        return HttpResponse("<h1>404 not found</h1>")
