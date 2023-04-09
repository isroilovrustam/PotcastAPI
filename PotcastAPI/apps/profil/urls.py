from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.profil.v1.urls'))
]