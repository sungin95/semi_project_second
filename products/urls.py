from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("product_index/", views.product_index, name="product_index"),
    path("index/", views.index, name="index"),
]
