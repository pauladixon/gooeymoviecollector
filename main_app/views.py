from django.shortcuts import render
from .models import Movie

# Add the following import
# from django.http import HttpResponse

# class Movie:
#   def __init__(self, title, service, year):
#     self.title = title
#     self.service = service
#     self.year = year

# movies = [
#   Movie('Always Be My Maybe', 'Netflix', 2019),
#   Movie('Her', 'Netflix',  2013),
#   Movie('The Lobster', 'Netflix', 2016),
#   Movie('Moonstruck', 'Amazon Prime', 1987),
#   Movie('Obvious Child', 'Netflix', 2014),
#   Movie("To All The Boys I've Loved Before", 'Netflix', 2018),
#   Movie('Crazy, Stupid Love', 'Hulu', 2011),
#   Movie('Scott Pilgrim vs. The World', 'Netflix', 2010),
#   Movie('10 Things I Hate About You', 'Disney+', 1999)
# ]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, 'movies/detail.html', {'movie': movie})