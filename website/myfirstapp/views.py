from django.shortcuts import render
from .models import Pokemon
from django.http import HttpResponse
# Create your views here.

def pokedex(request):
    all_pokemons = Pokemon.objects.all()
    context = {"all_pokemons" : all_pokemons}
    return render(request, "myfirstapp/pokedex.html", context)

def details(request, pname):
    pokemon = Pokemon.objects.all().filter(name=pname)

    #For evolutions
    evolutions = [pokemon[0]]
    i = 1
    if pokemon[0].firstevolution == 1:
        auxpok = Pokemon.objects.all().filter(pk=pokemon[0].pk + i)
        while auxpok[0].firstevolution != 1:
            evolutions.append(auxpok[0])
            i += 1
            auxpok = Pokemon.objects.all().filter(pk=pokemon[0].pk + i)
    else:
        auxpok = Pokemon.objects.all().filter(pk=pokemon[0].pk - i)
        while auxpok[0].firstevolution != 1:
            evolutions.insert(0, auxpok[0])
            i += 1
            auxpok = Pokemon.objects.all().filter(pk=pokemon[0].pk - i)
        evolutions.insert(0, auxpok[0])
        i = 1
        auxpok = Pokemon.objects.all().filter(pk=pokemon[0].pk + i)
        while auxpok[0].firstevolution != 1:
            evolutions.append(auxpok[0])
            i += 1
            auxpok = Pokemon.objects.all().filter(pk=pokemon[0].pk + i)

    context = {"pokemon": pokemon, "evolutions": evolutions}
    return render(request, "myfirstapp/details.html", context)








