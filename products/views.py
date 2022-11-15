from django.shortcuts import render, redirect, get_object_or_404
from .models import Products

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

def detail(request):
    return render(request, "products/product_detail.html")
