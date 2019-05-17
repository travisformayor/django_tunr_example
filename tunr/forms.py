from django import forms
from .models import Artist, Song

class ArtistForm(forms.ModelForm):
  class Meta: # Meta class contains info that isn't specific to one instance, but instead all versions of that form
    model = Artist
    fields = ('name', 'photo_url', 'nationality')

class SongForm(forms.ModelForm):
  class Meta: # Meta class contains info that isn't specific to one instance, but instead all versions of that form
    model = Song
    fields = ('title', 'artist','preview_url', 'album')