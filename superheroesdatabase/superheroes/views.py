from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero
# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def details(request, superhero_id):
    specific_superhero = Superhero.objects.get(id=superhero_id)
    context = {
        'specific_superhero':specific_superhero
    }
    return render(request, 'superheroes/details.html', context)
