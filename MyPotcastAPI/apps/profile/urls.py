from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.profile.v1.urls'))
]