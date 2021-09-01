from django.db import models

class Filmography(models.Model):
    imdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    role = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    # page_link = models.URLField()
    # imdb_rating = models.CharField(max_length=8)
    # uncaged_rating = models.CharField(max_length=8)
    runtime = models.CharField(max_length=20)
    plot = models.TextField()
