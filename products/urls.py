from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("product_detail/<int:pk>", views.detail, name="detail"),
    path("product_detail/<int:pk>/review", views.review_create, name="review_create"),
    path("like/<int:pk>", views.like_product, name="like_product"),
    path(
        "like_reviews/<int:product_pk>/<int:review_pk>",
        views.like_reviews,
        name="like_reviews",
    ),
    path(
        "product_detail/<int:product_pk>/<int:review_pk>/update",
        views.update,
        name="update",
    ),
    path(
        "product_detail/<int:product_pk>/<int:review_pk>/delete",
        views.delete,
        name="delete",
    ),
]
