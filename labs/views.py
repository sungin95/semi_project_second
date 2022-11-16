from django.shortcuts import render
from dotenv import load_dotenv
import os
from products.models import Products
from django.db.models import Q
from .models import Search

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

def search(request):
    s = Search.objects.filter().order_by("count")[1:12]
    if request.method == "GET":
        products = Products.objects.all()
        search = request.GET.get("search", "")

        if len(search) >= 0:
            if Search.objects.filter(keyword=search).exists():
                search_keyword = Search.objects.get(keyword=search)
                search_keyword.count += 1
                search_keyword.save()
            else:
                Search.objects.create(keyword=search, count=1)

        if search:
            
            search_lists = products.filter(
                Q(화면밝기__icontains=search)
                | Q(메모리대역폭__icontains=search)
            )
            context = {
                "search_lists": search_lists,
                "s": s,
                "search": search,
            }
            return render(request, "products/index.html", context)