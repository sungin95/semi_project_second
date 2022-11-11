from django.urls import path, include

app_name = "login"

urlpatterns = [
    path("login/", include("allauth.urls")),
]
