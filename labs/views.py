from django.shortcuts import render
from dotenv import load_dotenv
import os
from products.models import Products

# Create your views here.
def main(request):
    products = Products.objects.all()
    context = {
        'products': products,
        'products_10': products[0:10],
    }
    return render(request, "labs/main.html", context)

def rating(request):
    return render(request, "labs/rating.html")

def intro(request):
    load_dotenv()
    MAPKEY = os.getenv("MAPKEY")
    context = {
        'MAPKEY': MAPKEY,
    }
    return render(request, "labs/intro.html", context)