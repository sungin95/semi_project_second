from django.urls import path
from . import views

app_name = "communities"

urlpatterns = [
    path("", views.index, name="index"),
    path("article_create/", views.article_create, name="article_create"),
    path("<int:article_pk>/", views.detail, name="detail"),
    path("<int:article_pk>/delete/", views.article_delete, name="article_delete"),
    path("<int:article_pk>/update/", views.update, name="update"),
    path("<int:article_pk>/comments/", views.comment_create, name="comment_create"),
    path(
        "<int:article_pk>/<int:comment_pk>/comment_delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path(
        "<int:article_pk>/<int:comment_pk>/sub_comment_create/",
        views.sub_comment_create,
        name="sub_comment_create",
    ),
]
