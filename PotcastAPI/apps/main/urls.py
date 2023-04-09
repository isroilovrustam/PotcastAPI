from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.main.v1.urls'))
]