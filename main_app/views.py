from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Movie, Service
from .forms import ViewingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = '__all__'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = '__all__'

class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies/'

@login_required
def home(request):
  return render(request, 'home.html')

@login_required
def about(request):
  return render(request, 'about.html')

@login_required
def movies_index(request):
  movies = Movie.objects.filter(user=request.user)
  return render(request, 'movies/index.html', {'movies':movies})

@login_required
def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  services_movie_doesnt_stream = Service.objects.exclude(id__in = movie.services.all().values_list('id'))
  viewing_form = ViewingForm()
  return render(request, 'movies/detail.html', {
    'movie': movie, 
    'viewing_form': viewing_form, 
    'services': services_movie_doesnt_stream
  })

@login_required
def add_viewing(request, movie_id):
  form = ViewingForm(request.POST)
  if form.is_valid():
    new_viewing = form.save(commit=False)
    new_viewing.movie_id = movie_id
    new_viewing.save()
  return redirect('detail', movie_id=movie_id)

@login_required
def assoc_service(request, movie_id, service_id):
  Movie.objects.get(id=movie_id).services.add(service_id)
  return redirect('detail', movie_id=movie_id)

@login_required
def unassoc_service(request, movie_id, service_id):
  Movie.objects.get(id=movie_id).services.remove(service_id)
  return redirect('detail', movie_id=movie_id)

class ServiceList(LoginRequiredMixin, ListView):
  model = Service

class ServiceDetail(LoginRequiredMixin, DetailView):
  model = Service

class ServiceCreate(LoginRequiredMixin, CreateView):
  model = Service
  fields = '__all__'

class ServiceUpdate(LoginRequiredMixin, UpdateView):
  model = Service
  fields = '__all__'

class ServiceDelete(LoginRequiredMixin, DeleteView):
  model = Service
  success_url = '/services/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)