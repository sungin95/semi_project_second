from django.urls import path
from . import views

app_name = "communities"

urlpatterns = [
    path("", views.index, name="index"),
]
