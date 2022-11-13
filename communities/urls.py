from django.urls import path
from . import views

app_name = "communities"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail", views.detail, name="detail"),  # pk 나중에 추가 해야 합니다.
]
