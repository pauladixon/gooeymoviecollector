from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie, Service
from .forms import ViewingForm

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'

class MovieUpdate(UpdateView):
  model = Movie
  fields = '__all__'

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', {'movies':movies})

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  services_movie_doesnt_stream = Service.objects.exclude(id__in = movie.services.all().values_list('id'))
  viewing_form = ViewingForm()
  return render(request, 'movies/detail.html', {
    'movie': movie, 'viewing_form': viewing_form, 
    'services': services_movie_doesnt_stream
  })

def add_viewing(request, movie_id):
  form = ViewingForm(request.POST)
  if form.is_valid():
    new_viewing =  form.save(commit=False)
    new_viewing.movie_id = movie_id
    new_viewing.save()
  return redirect('detail', movie_id=movie_id)

def assoc_service(request, movie_id, service_id):
  Movie.objects.get(id=movie_id).services.add(service_id)
  return redirect('detail', movie_id=movie_id)

def unassoc_service(request, movie_id, service_id):
  Movie.objects.get(id=movie_id).services.remove(service_id)
  return redirect('detail', movie_id=movie_id)

class ServiceList(ListView):
  model = Service

class ServiceDetail(DetailView):
  model = Service

class ServiceCreate(CreateView):
  model = Service
  fields = '__all__'

class ServiceUpdate(UpdateView):
  model = Service
  fields = '__all__'

class ServiceDelete(DeleteView):
  model = Service
  success_url = '/services/'