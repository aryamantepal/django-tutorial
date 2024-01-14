from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Movie

# Create your views here.
# Usually, index represents the main page of an app
def index(request):
    movies = Movie.objects.all()
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)
    return render(request, 'index.html', {'movies': movies})

def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'detail.html', {"movie":movie})
    except Movie.DoesNotExist:
        raise Http404()
    # return HttpResponse(movie_id)
    