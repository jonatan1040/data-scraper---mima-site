from django.urls import path
from . import views

app_name = "mima"
urlpatterns = [
    path('artist/<int:artist_number>/', views.get_artist, name="artist"),
    path('song/<int:song_number>/', views.get_song, name="song"),
    path('fact/<int:facts_number>/', views.get_facts, name="facts"),
]
