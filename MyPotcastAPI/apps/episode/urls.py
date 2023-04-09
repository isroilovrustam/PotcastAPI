from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.episode.v1.urls'))
]