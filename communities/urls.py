from django.urls import path
from . import views

app_name = "communities"

urlpatterns = [
    path("", views.index, name="index"),
    path("index_jab/", views.index_jab, name="index_jab"),
    path("index_question/", views.index_question, name="index_question"),
    path("index_boast/", views.index_boast, name="index_boast"),
    path("index_consult/", views.index_consult, name="index_consult"),
    path("index_hello/", views.index_hello, name="index_hello"),
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
    path("<int:article_pk>/like/", views.like, name="like"),
    path("notion_create/", views.notion_create, name="notion_create"),
    path("<int:article_pk>/notion_update/", views.notion_update, name="notion_update"),
    path("search/", views.search, name="search"),
]
