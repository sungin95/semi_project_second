from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from dotenv import load_dotenv
import os
from .models import Products
from django.http import JsonResponse

# Create your views here.
def index(request):
    products = Products.objects.all()
    category = request.GET.get("category")
    if category:
        products_category = Products.objects.filter(제조회사__contains=category)
    else:
        products_category = products
    context = {
        'products': products,
        'category': category,
        'products_category': products_category,
    }
    return render(request, "products/index.html", context)

def detail(request, pk):
    load_dotenv()
    KAKAO_KEY = os.getenv("KAKAOKEY")
    product = get_object_or_404(Products, pk=pk)
    model_name = product.모델명
    special_price = product.가격
    price = int(round((product.가격) * 1.1, -4))
    thumbnail = product.썸네일
    image1 = product.이미지1
    image3 = product.이미지3
    image2 = product.이미지2
    context = {
        "KAKAO_KEY": KAKAO_KEY,
        "price": price,
        "special_price": special_price,
        "modelName": model_name,
        "product": product,
        "thumbnail": thumbnail,
        "image1": image1,
        "image2": image2,
        "image3": image3,
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
