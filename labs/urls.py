from django.urls import path
from . import views

app_name = "labs"

urlpatterns = [
    path("", views.main, name="main"),
    path("rating/", views.rating, name="rating"),
    path("intro/", views.intro, name="intro"),
    path("search/", views.search, name="search"),
]
