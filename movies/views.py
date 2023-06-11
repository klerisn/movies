from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": ["movie1", "movie2"]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home Page")
