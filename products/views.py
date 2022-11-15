from django.shortcuts import render
from dotenv import load_dotenv
import os

# Create your views here.
def index(request):
    return render(request, "products/index.html")


def detail(request):
    load_dotenv()
    KAKAO_KEY = os.getenv("KAKAOKEY")
    context = {
        "KAKAO_KEY": KAKAO_KEY,
    }
    return render(request, "products/product_detail.html", context)
