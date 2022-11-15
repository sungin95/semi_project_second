from django.shortcuts import render, redirect, get_object_or_404
from dotenv import load_dotenv
import os
from .models import Products
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "products/index.html")


def detail(request, pk):
    load_dotenv()
    KAKAO_KEY = os.getenv("KAKAOKEY")
    product = get_object_or_404(Products, pk=pk)
    model_name = product.모델명
    special_price = product.가격
    price = int(round((product.가격) * 1.1, -4))
    thumbnail = product.썸네일

    context = {
        "KAKAO_KEY": KAKAO_KEY,
        "price": price,
        "special_price": special_price,
        "modelName": model_name,
        "product": product,
        "thumbnail": thumbnail,
    }
    return render(request, "products/product_detail.html", context)


def like_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if product.like_product.filter(pk=request.user.pk).exists():
        product.like_product.remove(request.user)
        is_like = False
    else:
        product.like_product.add(request.user)
        is_like = True
    context = {
        "isLiked": is_like,
        "likeCount": product.like_product.count(),
    }
    return JsonResponse(context)
