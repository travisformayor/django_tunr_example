from django.db import models

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=100)
  nationality = models.CharField(max_length=100)
  photo_url = models.TextField()

  def __str__(self):
      return self.name

class Song(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
  title = models.CharField(max_length=100)
  preview_url = models.TextField(null=True)
  album = models.TextField(null=True)

  def __str__(self):
    return f'{self.title} - {self.artist.name}'