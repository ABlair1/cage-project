from django.shortcuts import render
from django.http import HttpResponse
from .models import Filmography

def index(request):
    # Get all films and film count from Nic Cage Filmography
    films = Filmography.objects.all()
    film_count = Filmography.objects.all().count()

    context = {
        'films': films, 
        'film_count': film_count,
    }

    # Render the home template with the data in the context variable
    return render(request, 'home.html', context=context)