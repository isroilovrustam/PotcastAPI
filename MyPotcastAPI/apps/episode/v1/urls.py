from django.urls import path
from .views import EpisodeGETListAPIView, EpisodePOSTListAPIView, EpisodeRUDAPIView, CommentEpisodeListCreatedAPIView, \
             PlaylistGETAPIView, EpisodeLikeListCreateAPIView, AddEpisodeToPlaylistAPI, PlaylistRUDAPIView

urlpatterns = [
    path('episode-list/', EpisodeGETListAPIView.as_view()),
    path('episode-create/', EpisodePOSTListAPIView.as_view()),
    path('episode-rud/<int:pk>/', EpisodeRUDAPIView.as_view()),
    path('comment-episode/<int:episode_id>/', CommentEpisodeListCreatedAPIView.as_view()),
    path('episode-like/', EpisodeLikeListCreateAPIView.as_view()),
    path('play-list/', PlaylistGETAPIView.as_view()),
    path('play-list-rud/<int:pk>/', PlaylistRUDAPIView.as_view()),
    path('add-episode/<int:pk>/', AddEpisodeToPlaylistAPI.as_view()),
]
