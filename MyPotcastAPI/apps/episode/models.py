from django.db import models

from apps.profile.models import Profile
from apps.main.models import Category, Tag


# Create your models here.

class Episode(models.Model):
    title = models.CharField(max_length=202)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_episode')
    image = models.ImageField(upload_to='episode/', null=True, blank=True)
    music = models.FileField(upload_to='music/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tag_episode')
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentEpisode(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='comment_episode', null=True,
                                blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username


class Playlist(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=202)
    episodes = models.ManyToManyField(Episode, related_name='play_list')

    def __str__(self):
        return self.title


class Playmusic(models.Model):
    play_list = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    def __str__(self):
        return self.play_list.title


class EpisodeLike(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.OneToOneField(Episode, on_delete=models.CASCADE)

    def __str__(self):
        return self.episode.title
