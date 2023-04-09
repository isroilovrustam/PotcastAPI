from rest_framework import generics, permissions
from rest_framework.response import Response

from . import serializers
from ..models import Episode, EpisodeComment, Playlist, Playmusic, EpisodeLike


class EpisodeListAPIView(generics.ListAPIView):
    queryset = Episode.objects.order_by('-id')
    serializer_class = serializers.EpisodeGETSerializer


class EpisodeCreateAPIView(generics.CreateAPIView):
    queryset = Episode.objects.order_by('-id')
    serializer_class = serializers.EpisodePOSTSerializer


class EpisodeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Episode.objects.order_by('-id')
    serializer_class = serializers.EpisodeGETSerializer


class EpisodeCommentCreateAPIView(generics.CreateAPIView):
    queryset = EpisodeComment.objects.order_by('-id')
    serializer_class = serializers.EpisodeCommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        episode_id = self.kwargs.get('episode_id')
        if episode_id:
            qs = qs.filter(episode_id=episode_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['episode_id'] = self.kwargs.get('episode_id')
        return ctx


class PlaylistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Playlist.objects.order_by('-id')
    serializer_class = serializers.PlaylistSerializer


class PlaylistRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = serializers.PlaylistGETSerializer


class PlaymusicDestroyAPIView(generics.DestroyAPIView):
    queryset = Playmusic.objects.order_by('-id')
    serializer_class = serializers.PlaylistDesSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['play_list_id'] = self.kwargs.get('play_list_id')
        return ctx


class PlaymusicCreateAPIView(generics.CreateAPIView):
    queryset = Playmusic.objects.order_by('-id')
    serializer_class = serializers.PlaymusicSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['play_list_id'] = self.kwargs.get('play_list_id')
        return ctx

    def create(self, request, *args, **kwargs):
        play_list_id = self.kwargs.get('play_list_id')
        play = Playmusic.objects.values_list('play_list_id')
        if play_list_id in play:
            Playmusic.objects.get(play_list_id=play_list_id).delete()
            return Response("Delete-like")
        instance = Playmusic.objects.create(play_list_id=play_list_id)
        serializer = serializers.PlaymusicSerializer(instance)
        return Response(serializer.data)


class LikeListAPIView(generics.ListAPIView):
    queryset = EpisodeLike.objects.all()
    serializer_class = serializers.LikeGETSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        author = self.request.user.profile_user
        if author:
            qs = qs.filter(author=author)
            return qs
        return qs


class LikePOSTAPIView(generics.CreateAPIView):
    queryset = EpisodeLike.objects.all()
    serializer_class = serializers.LikePOSTSerilazer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['episode_id'] = self.kwargs.get('episode_id')
        return ctx

    def create(self, request, *args, **kwargs):
        episode_id = self.kwargs.get('episode_id')
        author_id = request.user.profile_user.id
        likes = EpisodeLike.objects.values_list('episode_id', 'author_id')
        if (episode_id, author_id) in likes:
            EpisodeLike.objects.get(episode_id=episode_id, author_id=author_id).delete()
            return Response("Delete-like")
        instance = EpisodeLike.objects.create(author_id=author_id, episode_id=episode_id)
        serializer = serializers.LikePOSTSerilazer(instance)
        return Response(serializer.data)
