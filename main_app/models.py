from django.db import models
from django.urls import reverse
from datetime import date

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies_detail', kwargs={'pk': self.id})

    def seen_before(self):
        return self.viewing_set.filter(date=date.today()).count() >= 1

class Viewing(models.Model):
    date = models.DateField('viewing date')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_view_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
