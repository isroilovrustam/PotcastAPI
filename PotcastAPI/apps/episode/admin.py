from django.contrib import admin
from .models import Episode, EpisodeComment, Playlist, Playmusic


# Register your models here.


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title']


@admin.register(EpisodeComment)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'episode']


@admin.register(Playlist)
class PlayAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title']


@admin.register(Playmusic)
class PlaymusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'play_list']
