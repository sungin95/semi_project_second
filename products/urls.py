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
    path("detail/calculate_weight/", views.calculate_weight, name="calculate_weight"),
    path("detail/calculate_price/", views.calculate_price, name="calculate_price"),
    path("detail/calculate_storage/", views.calculate_storage, name="calculate_storage"),
    path("detail/calculate_processor/", views.calculate_processor, name="calculate_processor"),
    path("detail/calculate_graphic/", views.calculate_graphic, name="calculate_graphic"),
    path("detail/calculate_resolution/", views.calculate_resolution, name="calculate_resolution"),
    path("detail/calculate_size/", views.calculate_size, name="calculate_size"),
    path("purchase/<int:product_pk>", views.purchase, name="purchase"),
]
