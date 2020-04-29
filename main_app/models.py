from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title