from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.detail, name="detail"),
    path("user_point/<int:value>", views.user_point, name="user_point"),
    path("add/<int:product_id>/", views.add_cart, name="add_cart"),
    path("remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("full_remove/", views.full_remove, name="full_remove"),
]
