from typing import DefaultDict
from django.db import models

class Filmography(models.Model):
    imdb_id = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=100, null=True)
    year = models.SmallIntegerField(null=True)
    role = models.CharField(max_length=100, null=True)
    likes = models.IntegerField(default=0, null=True)
    page_link = models.URLField(null=True)
    imdb_rating = models.CharField(max_length=8, null=True)
    uncaged_rating = models.JSONField(null=True)
    runtime = models.CharField(max_length=20, null=True)
    plot = models.TextField(null=True)
    cover_url = models.URLField(null=True)
