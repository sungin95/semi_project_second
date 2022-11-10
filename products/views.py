from django.shortcuts import render

# Create your views here.
def product_index(request):
    return render(request, "products/product_index.html")
