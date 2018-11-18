from django.db import models
from django.urls import reverse


# Create your models here.
class Album(models.Model):
    owner=models.ForeignKey('accounts.CustomUser',related_name='albums',on_delete=models.CASCADE)
    album_title=models.CharField(max_length=250)
    artist=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)
    album_logo=models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '-' +self.artist


class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE) 
    #CASCADE: When the referenced object is deleted, also delete the objects that have references to it (When you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
    audio_file=models.FileField()
    song_title=models.CharField(max_length=250)
    is_favourite=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:songs')
    
    def __str__(self):
        return self.song_title




    