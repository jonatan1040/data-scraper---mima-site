from django.db import models


class Artist(models.Model):
    artist = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.artist


class Song(models.Model):
    id = models.AutoField(primary_key=True, null=False, verbose_name="ID")
    song = models.CharField(max_length=100, null=False)
    artist = models.ForeignKey(Artist, null=False, on_delete=models.PROTECT,
                               related_name="songs")   # models.PROTECT does not give you the option to delete a
    # father (artist in our case) before you remove its childrens from him because if you could delete the father
    # then its children will be deleted too
    # related_name="songs" means that if i would make it then i can use the name to call it, for example i could say
    # artist.song and get all the song of that artist

    def __str__(self):
        return f"{self.song} - {self.artist}"


class Facts(models.Model):
    facts = models.TextField()
    song = models.ForeignKey(Song, null=False, on_delete=models.PROTECT,
                             related_name="facts")
    author = models.CharField(max_length=100, null=False, default='none')

    def __str__(self):
        return (f"{self.facts}\n"
                f"נכתב עי: {self.author}")
