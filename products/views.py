from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Review
from dotenv import load_dotenv
import os
from .models import Products
from .forms import ReviewForm, PurchaseForm
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_safe,
    require_http_methods,
    require_POST,
)

# Create your views here.
def index(request):
    products = Products.objects.all()
    # 카테고리 분류
    category = request.GET.get("category", "")
    if category:
        products_category = Products.objects.filter(Q(제조회사__contains=category))
    else:
        products_category = products
    brand = request.GET.get("brand", "")
    if brand:
        products_brand = Products.objects.filter(Q(제조회사__contains=brand))
    else:
        products_brand = products
    # 가격 분류  1,2,3,4,5
    price = request.GET.get("price", "")
    if price:
        products_price = Products.objects.filter(Q(가격등급__contains=price))
    else:
        products_price = products
    # 무게 분류  1,2,3,4
    weight = request.GET.get("weight", "")
    if weight:
        products_weight = Products.objects.filter(Q(무게등급__contains=weight))
    else:
        products_weight = products
    # 프로세스 분류 AMD, INTEL, 애플
    processor = request.GET.get("processor", "")
    if processor:
        products_processor = Products.objects.filter(Q(CPU제조사분류__contains=processor))
    else:
        products_processor = products
    # 프로세스 분류 4000, 5000, 6000, i3, i5, i7, i9, 기타, m1, m2
    processor_number = request.GET.get("processor_number", "")
    if processor_number:
        products_processor_number = Products.objects.filter(
            Q(CPU넘버분류__contains=processor_number)
        )
    else:
        products_processor_number = products
    # 저장용량등급 분류  1,2,3,4
    storage = request.GET.get("storage", "")
    if storage:
        products_storage = Products.objects.filter(Q(저장용량등급__contains=storage))
    else:
        products_storage = products
    # GPU종류등급 분류  1,2
    graphic = request.GET.get("graphic", "")
    if graphic:
        products_graphic = Products.objects.filter(Q(GPU종류등급__contains=graphic))
    else:
        products_graphic = products
    # 해상도등급 분류  "FHD","QHD","UHD"
    resolution = request.GET.get("resolution", "")
    if resolution:
        products_resolution = Products.objects.filter(Q(해상도등급__contains=resolution))
    else:
        products_resolution = products
    # 화면크기등급 분류  1,2,3
    size = request.GET.get("size", "")
    if size:
        products_size = Products.objects.filter(Q(화면크기등급__contains=size))
    else:
        products_size = products

    print(request.GET.keys())
    print(list(request.GET.values()))
    result = (
        products_category
        & products_price
        & products_weight
        & products_processor
        & products_processor_number
        & products_storage
        & products_graphic
        & products_resolution
        & products_size
        & products_brand
    )
    print(len(result))
    products_category = result

    page = request.GET.get("page", "1")
    paginator = Paginator(products_category, 6)
    page_obj = paginator.get_page(page)
    context = {
        "products": products,
        "brand": brand,
        "price": price,
        "weight": weight,
        "processor": processor,
        "processor_number": processor_number,
        "storage": storage,
        "graphic": graphic,
        "resolution": resolution,
        "size": size,
        "result": result,
        "category": category,
        "filter": len(result),
        "products_category": products_category,
        "page_obj": page_obj,
    }
    return render(request, "products/index.html", context)


def detail(request, pk):
    load_dotenv()
    KAKAO_KEY = os.getenv("KAKAOKEY")
    product = get_object_or_404(Products, pk=pk)
    reviews = product.review_set.all()
    review_form = ReviewForm()
    product_grade = 0
    lenReviews = len(reviews)
    for review in reviews:
        product_grade += review.grade
    if lenReviews != 0:
        product_grade = round((product_grade / lenReviews), 1)
    model_name = product.모델명
    special_price = product.가격
    price = int(round((product.가격) * 1.1, -4))
    thumbnail = product.썸네일
    image1 = product.이미지1
    image2 = product.이미지2
    image3 = product.이미지3

    context = {
        "review_form": review_form,
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
    return render(request, "products/detail.html", context)


@login_required
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


@login_required
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


@login_required
def review_create(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            user = request.user
            user.point += 100
            user.save()
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


@login_required
def update(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("products:detail", product_pk)
    else:
        reviewContent = review.content
    context = {
        "reviewContent": reviewContent,
    }
    return JsonResponse(context)



def delete(request, product_pk, review_pk):
    get_object_or_404(Review, pk=review_pk).delete()
    context = {}
    return JsonResponse(context)


# 필터링 계산
@login_required
def calculate_weight(request):
    products = Products.objects.all()
    # 무게 등급 나누기
    for product in products:
        product.무게 = int(product.무게)
        if product.무게 < 1000:
            product.무게등급 = "1kg미만"
        elif product.무게 >= 1000 and product.무게 < 1500:
            product.무게등급 = "1kg~1.5kg미만"
        elif product.무게 >= 1500 and product.무게 < 2000:
            product.무게등급 = "1.5kg~2.0kg미만"
        elif product.무게 >= 2000:
            product.무게등급 = "2kg이상"
        product.save()
    return redirect("products:index")

@login_required
def calculate_price(request):
    products = Products.objects.all()
    # 가격 등급 나누기.
    for product in products:
        if product.가격 <= 500000:
            product.가격등급 = "50만원이하"
        elif product.가격 > 500000 and product.가격 <= 1000000:
            product.가격등급 = "50만원이상~100만원미만"
        elif product.가격 > 1000000 and product.가격 <= 1500000:
            product.가격등급 = "100만원이상~150만원미만"
        elif product.가격 > 1500000 and product.가격 <= 2000000:
            product.가격등급 = "150만원이상~200만원미만"
        elif product.가격 > 2000000:
            product.가격등급 = "200만원이상"
        product.save()
    return redirect("products:index")

@login_required
def calculate_storage(request):
    products = Products.objects.all()
    # 저장 용량 등급 나누기.
    for product in products:
        if product.저장용량 <= 256:
            product.저장용량등급 = "250GB~256GB이하"
        elif product.저장용량 >= 500 and product.저장용량 <= 516:
            product.저장용량등급 = "500GB~512GB이하"
        elif product.저장용량 >= 1024 and product.저장용량 < 2048:
            product.저장용량등급 = "1TB이상~2TB미만"
        elif product.저장용량 >= 2048:
            product.저장용량등급 = "2TB이상"
        product.save()
    return redirect("products:index")

@login_required
def calculate_processor(request):
    products = Products.objects.all()
    # CPU제조사 분류
    for product in products:
        if product.CPU제조사 == "AMD":
            product.CPU제조사분류 = "AMD"
            if product.CPU넘버[0] == "4":
                product.CPU넘버분류 = "AMD4000번대"
            elif product.CPU넘버[0] == "5":
                product.CPU넘버분류 = "AMD5000번대"
            elif product.CPU넘버[0] == "6":
                product.CPU넘버분류 = "AMD6000번대"
        elif product.CPU제조사 == "인텔":
            product.CPU제조사분류 = "INTEL"
            if product.CPU넘버[0:2] == "i3":
                product.CPU넘버분류 = "i3"
            elif product.CPU넘버[0:2] == "i5":
                product.CPU넘버분류 = "i5"
            elif product.CPU넘버[0:2] == "i7":
                product.CPU넘버분류 = "i7"
            elif product.CPU넘버[0:2] == "i9":
                product.CPU넘버분류 = "i9"
            else:
                product.CPU넘버분류 = "기타"
        elif product.CPU제조사 == "애플(ARM)":
            product.CPU제조사분류 = "애플"
            if product.CPU종류 == "실리콘 M1 PRO" or product.CPU종류 == "실리콘 M1 MAX":
                product.CPU넘버분류 = "M1"
            elif product.CPU종류 == "실리콘 M2":
                product.CPU넘버분류 = "M2"
        product.save()
    return redirect("products:index")

@login_required
def calculate_graphic(request):
    products = Products.objects.all()
    # 그래픽카드 분류
    for product in products:
        if product.GPU종류 == "내장그래픽":
            product.GPU종류등급 = "내장그래픽"
        elif product.GPU종류 == "외장그래픽":
            product.GPU종류등급 = "외장그래픽"
            if product.GPU제조사 == "AMD":
                product.GPU종류등급 = "AMD외장그래픽"
            elif product.GPU제조사 == "인텔":
                product.GPU종류등급 = "인텔외장그래픽"
            elif product.GPU제조사 == "엔비디아":
                product.GPU종류등급 = "엔비디아외장그래픽"
        product.save()
    return redirect("products:index")

@login_required
def calculate_resolution(request):
    products = Products.objects.all()
    # 해상도 분류
    for product in products:
        if int(product.해상도[5:9]) <= 1200:
            product.해상도등급 = "FHD"
        elif int(product.해상도[5:9]) <= 1600:
            product.해상도등급 = "QHD"
        elif int(product.해상도[5:9]) <= 2400:
            product.해상도등급 = "UHD"
        product.save()
    return redirect("products:index")

@login_required
def calculate_size(request):
    products = Products.objects.all()
    # 노트북 크기 분류
    for product in products:
        if (
            product.화면크기 == "35.5cm(14인치)"
            or product.화면크기 == "33.782cm(13.3인치)"
            or product.화면크기 == "34.5cm(13.6인치)"
            or product.화면크기 == "27.4cm(10.9인치)"
            or product.화면크기 == "33.7cm(13인치)"
            or product.화면크기 == "33.7cm(13.3인치)"
            or product.화면크기 == "34.03cm(13.4인치)"
            or product.화면크기 == "33.78cm(13.3인치)"
            or product.화면크기 == "35.6cm(14인치)"
            or product.화면크기 == "35.56cm(14인치)"
            or product.화면크기 == "35.97cm(14.2인치)"
        ):
            product.화면크기등급 = "14인치이하"
        elif (
            product.화면크기 == "39.6cm(15.6인치)"
            or product.화면크기 == "36.8cm(14.5인치)"
            or product.화면크기 == "39.62cm(15.6인치)"
            or product.화면크기 == "40.8cm(16인치)"
            or product.화면크기 == "40.64cm(16인치)"
            or product.화면크기 == "35.97cm(14.2인치)"
            or product.화면크기 == "41.05cm(16.2인치)"
            or product.화면크기 == "40.9cm(16.1인치)"
            or product.화면크기 == "40.89cm(16.1인치)"
            or product.화면크기 == "38.1cm(15인치)"
            or product.화면크기 == "40.6cm(16인치)"
        ):
            product.화면크기등급 = "15인치~16.2인치"
        elif (
            product.화면크기 == "43.9cm(17.3인치)"
            or product.화면크기 == "43.1cm(17인치)"
            or product.화면크기 == "43.94cm(17.3인치)"
            or product.화면크기 == "43.18cm(17인치)"
        ):
            product.화면크기등급 = "17인치~17.3인치"
        product.save()
    return redirect("products:index")


@login_required
def calculate_ten(request):
    products = Products.objects.all()
    for product in products:
        product.ten_price = int(round((product.가격) * 1.1))
        product.save()
    return redirect("products:index")
