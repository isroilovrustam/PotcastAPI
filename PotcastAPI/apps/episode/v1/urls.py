from django.urls import path
from . import views

urlpatterns = [
    path('episode-list/', views.EpisodeListAPIView.as_view()),
    path('episode-create/', views.EpisodeCreateAPIView.as_view()),
    path('episode-retrieve/<int:pk>/', views.EpisodeRetrieveAPIView.as_view()),
    path('episode-comment/<int:episode_id>/', views.EpisodeCommentCreateAPIView.as_view()),
    path('playlist/', views.PlaylistListCreateAPIView.as_view()),
    path('playlist-rd/<int:pk>/', views.PlaylistRUDAPIView.as_view()),
    path('playmusic/<int:play_list_id>/', views.PlaymusicCreateAPIView.as_view()),
    path('playmusic/<int:play_list_id>/<int:pk>/', views.PlaymusicDestroyAPIView.as_view()),
    path('likes/', views.LikeListAPIView.as_view()),
    path('likes-create/<int:episode_id>/', views.LikePOSTAPIView.as_view()),
]
