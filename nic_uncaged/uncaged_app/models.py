from django.db import models

class Filmography(models.Model):
    title = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    role = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    # page_link = models.URLField()
    # rating = models.CharField(max_length=8)
    # runtime = 
    # synopsis = 
