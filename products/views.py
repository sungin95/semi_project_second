from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Review
from dotenv import load_dotenv
import os
from .models import Products
from .forms import ReviewForm
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
        "products": products,
        "category": category,
        "products_category": products_category,
    }
    return render(request, "products/index.html", context)


def detail(request, pk):
    load_dotenv()
    KAKAO_KEY = os.getenv("KAKAOKEY")
    product = get_object_or_404(Products, pk=pk)
    reviews = product.review_set.all()
    product_grade = 0
    lenReviews = len(reviews)
    for review in reviews:
        product_grade += review.grade
    product_grade = round((product_grade / lenReviews), 1)
    model_name = product.모델명
    special_price = product.가격
    price = int(round((product.가격) * 1.1, -4))
    thumbnail = product.썸네일
    image1 = product.이미지1
    image3 = product.이미지3
    image2 = product.이미지2
    context = {
        "reviews": reviews,
        "product_grade": product_grade,
        "lenReviews": lenReviews,
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


def like_reviews(request, product_pk, review_pk):
    product = get_object_or_404(Products, pk=product_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if review.like.filter(pk=request.user.pk).exists():
        review.like.remove(request.user)
        is_like = False
    else:
        review.like.add(request.user)
        is_like = True
    context = {
        "isLiked": is_like,
        "likeReviewCount": review.like.count(),
    }
    return JsonResponse(context)


def review_create(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.products = product
            review.save()
        return redirect("products:detail", product.pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
        "product": product,
    }
    return render(request, "products/create.html", context)


def update(request):

    return redirect("products:detail")  # product.pk


def delete(request, product_pk, review_pk):
    get_object_or_404(Review, pk=review_pk).delete()
    return redirect("products:detail", product_pk)
