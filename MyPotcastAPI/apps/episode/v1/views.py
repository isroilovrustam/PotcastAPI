from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    RetrieveDestroyAPIView
from .serializers import EpisodeGETSerializer, EpisodeCommentSerializer, PlaylistGETSerializer, \
    EpisodeLikeSerializer, EpisodePOSTSerializer, PlaylistRUDSerializer
from ..models import Episode, CommentEpisode, Playlist, EpisodeLike
from rest_framework import permissions, response, views


class EpisodeGETListAPIView(ListAPIView):
    queryset = Episode.objects.order_by('-id')
    serializer_class = EpisodeGETSerializer


class EpisodePOSTListAPIView(CreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodePOSTSerializer
    permission_classes = (permissions.IsAdminUser,)


class EpisodeRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    # serializer_class = EpisodePOSTSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EpisodeGETSerializer
        return EpisodePOSTSerializer


class CommentEpisodeListCreatedAPIView(ListCreateAPIView):
    queryset = CommentEpisode.objects.order_by('-id')
    serializer_class = EpisodeCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        episode_id = self.kwargs.get("episode_id")

        if episode_id:
            qs = qs.filter(episode_id=episode_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['episode_id'] = self.kwargs.get('episode_id')
        return ctx


class PlaylistGETAPIView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistGETSerializer


class PlaylistRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    # serializer_class = PlaylistRUDSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlaylistGETSerializer
        return PlaylistRUDSerializer


class AddEpisodeToPlaylistAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        play = Playlist.objects.filter(id=self.kwargs.get('pk')).first()
        for i in self.request.data['episodes']:
            episode = Episode.objects.filter(id=i).first()
            play.episodes.add(episode)
        serializer = PlaylistGETSerializer(play)
        return response.Response(serializer.data)


class EpisodeLikeListCreateAPIView(ListCreateAPIView):
    queryset = EpisodeLike.objects.order_by('-id')
    serializer_class = EpisodeLikeSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        episode_id = self.kwargs.get("episode_id")

        if episode_id:
            qs = qs.filter(episode_id=episode_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['episode_id'] = self.kwargs.get('episode_id')
        return ctx
