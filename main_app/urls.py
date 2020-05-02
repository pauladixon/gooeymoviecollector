from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('movies/', views.movies_index, name='index'),
  path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
  path('movies/create', views.MovieCreate.as_view(), name='movies_create'),
  path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
  path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
  path('movies/<int:movie_id>/add_viewing/', views.add_viewing, name='add_viewing'),
  path('movies/<int:movie_id>/assoc_service/<int:service_id>/', views.assoc_service, name='assoc_service'),
  path('movies/<int:movie_id>/unassoc_service/<int:service_id>/', views.unassoc_service, name='unassoc_service'),
  path('services/', views.ServiceList.as_view(), name='services_index'),
  path('services/<int:pk>/', views.ServiceDetail.as_view(), name='services_detail'),
  path('services/create/', views.ServiceCreate.as_view(), name='services_create'),
  path('services/<int:pk>/update/', views.ServiceUpdate.as_view(), name='services_update'),
  path('services/<int:pk>/delete/', views.ServiceDelete.as_view(), name='services_delete'),
  path('accounts/signup', views.signup, name='signup'),
]