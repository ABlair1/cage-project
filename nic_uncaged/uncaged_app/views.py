from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Filmography

def catalog(request):
    # Get all films and film count from Nic Cage Filmography
    films = Filmography.objects.all()
    film_count = Filmography.objects.all().count()

    context = {
        'films': films, 
        'film_count': film_count,
    }

    # Render the movie catalog template with the data in the context variable
    return render(request, 'catalog.html', context=context)

class CatalogEntryView(generic.DetailView):
    model = Filmography