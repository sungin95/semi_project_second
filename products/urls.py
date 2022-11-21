from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("detail/<int:pk>/review", views.review_create, name="review_create"),
    path("like/<int:pk>", views.like_product, name="like_product"),
    path(
        "like_reviews/<int:product_pk>/<int:review_pk>",
        views.like_reviews,
        name="like_reviews",
    ),
    path(
        "detail/<int:product_pk>/<int:review_pk>/update",
        views.update,
        name="update",
    ),
    path(
        "detail/<int:product_pk>/<int:review_pk>/delete",
        views.delete,
        name="delete",
    ),
    path("calculate_weight/", views.calculate_weight, name="calculate_weight"),
    path("calculate_price/", views.calculate_price, name="calculate_price"),
    path("calculate_storage/", views.calculate_storage, name="calculate_storage"),
    path("calculate_processor/", views.calculate_processor, name="calculate_processor"),
    path("calculate_graphic/", views.calculate_graphic, name="calculate_graphic"),
    path(
        "calculate_resolution/", views.calculate_resolution, name="calculate_resolution"
    ),
    path("calculate_size/", views.calculate_size, name="calculate_size"),
    path("calculate_ten/", views.calculate_ten, name="calculate_ten"),
]
