from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

LOCATIONS =  (
    ('H', 'home'),
    ('F', "friend's house"),
    ('T', 'movie theater')
)

class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services_detail', kwargs={'pk': self.id})


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    services = models.ManyToManyField(Service)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

    def seen_before(self):
        return self.viewing_set.count() >= 1


class Viewing(models.Model):
    date = models.DateField('viewing date')
    location = models.CharField(
        max_length=1,
        choices=LOCATIONS,
        default=LOCATIONS[0][0]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_location_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  def __str__(self):
    return f"photo for movie_id: {self.movie_id} @{self.url}"