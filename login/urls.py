from django.urls import path, include


urlpatterns = [
    path("login/", include("allauth.urls")),
]
