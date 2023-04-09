from django.contrib import admin
from .models import Episode, CommentEpisode, Playlist, Playmusic, EpisodeLike


# Register your models here.
@admin.register(Playlist)
class Admni(admin.ModelAdmin):
    filter_horizontal = ['episodes']


admin.site.register(Episode)
admin.site.register(CommentEpisode)
admin.site.register(Playmusic)
admin.site.register(EpisodeLike)
