from django.db import models


class Facts(models.Model):
    song_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    facts = models.TextField(max_length=1000)

# class Song(models.Model);
#     "my name is"