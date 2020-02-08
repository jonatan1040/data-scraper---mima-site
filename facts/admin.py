from django.contrib import admin
from facts import models


class ArtistAdmin(admin.ModelAdmin):
    # date_hierarchy = 'date'
    search_fields = (
        'id',
        'artist',
    )
    list_display = (
        'id',
        'artist',
    )


class SongsAdmin(admin.ModelAdmin):
    # date_hierarchy = 'date'
    search_fields = (
        'id',
        'artist_id',
        'song',
    )
    list_display = (
        'id',
        'artist_id',
        'song',
    )


class FactsAdmin(admin.ModelAdmin):
    # date_hierarchy = 'date'
    search_fields = (
        'id',
        'facts',
        'song_id',
        'author',
    )
    list_display = (
        'id',
        'facts',
        'song_id',
        'author',
    )


admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.Song, SongsAdmin)
admin.site.register(models.Facts, FactsAdmin)

