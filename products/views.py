from django.shortcuts import render
from dotenv import load_dotenv
import os
from .models import Products
import math

# Create your views here.
def index(request):
    return render(request, "products/index.html")


def detail(request, pk):
    load_dotenv()
    KAKAO_KEY = os.getenv("KAKAOKEY")
    product = Products.objects.get(pk=pk)
    model_name = product.모델명
    print(type(model_name))
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
