# in tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
  path('', views.artist_list, name='artist_list'),
  path('artist/<int:pk>', views.artist_detail, name='artist_detail'),
  path('artist/new', views.artist_create, name='artist_create'),
  path('artist/<int:pk>/edit', views.artist_edit, name='artist_edit'),
  path('artist/<int:pk>/delete', views.artist_delete, name='artist_delete'),
  path('songs', views.song_list, name='song_list'),
  path('songs/new', views.song_create, name='song_create'),
  path('songs/<int:pk>/edit', views.song_edit, name='song_edit'),
  path('songs/<int:pk>/delete', views.song_delete, name='song_delete'),
  path('songs/<int:pk>', views.song_detail, name='song_detail'),
]