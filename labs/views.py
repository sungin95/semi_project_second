from django.shortcuts import render, redirect
from dotenv import load_dotenv
import os
from products.models import Products
from django.db.models import Q
from .models import Search
from django.core.paginator import Paginator
from django.views.decorators.http import require_safe, require_http_methods, require_POST

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

        if len(search) >= 1:
            if Search.objects.filter(keyword=search).exists():
                search_keyword = Search.objects.get(keyword=search)
                search_keyword.count += 1
                search_keyword.save()
            else:
                Search.objects.create(keyword=search, count=1)

        if search:
            search_lists = products.filter(
                Q(모델명__icontains=search) |Q(가격__icontains=search) |
                Q(제조회사=search) |Q(등록년월__icontains=search) |
                Q(운영체제__icontains=search) |Q(게임용__icontains=search) |
                Q(사무_인강용__icontains=search) |Q(그래픽작업용__icontains=search) |
                Q(화면크기__icontains=search) |Q(화면비율__icontains=search) |
                Q(해상도__icontains=search) |Q(화면크기대__icontains=search) |
                Q(DCI_P3__icontains=search) |Q(NTSC__icontains=search) |
                Q(화면밝기__icontains=search) |Q(주사율__icontains=search) |
                Q(패널종류__icontains=search) |Q(패널표면처리__icontains=search) |
                Q(CPU제조사__icontains=search) |Q(CPU종류__icontains=search) |
                Q(CPU코드명__icontains=search) |Q(CPU넘버__icontains=search) |
                Q(코어수__icontains=search) |Q(스레드수__icontains=search) |
                Q(메모리타입__icontains=search) |Q(메모리용량__icontains=search) |
                Q(메모리슬롯__icontains=search) |Q(메모리최대용량__icontains=search) |
                Q(메모리대역폭__icontains=search) |Q(메모리교체__icontains=search) |
                Q(메모리구성__icontains=search) |Q(저장장치종류__icontains=search) |
                Q(저장용량__icontains=search) |Q(저장슬롯__icontains=search) |
                Q(GPU종류__icontains=search) |Q(GPU제조사__icontains=search) |
                Q(GPU칩셋__icontains=search) |Q(TGP__icontains=search) |
                Q(GPU메모리__icontains=search) |Q(썬더볼트3__icontains=search) |
                Q(썬더볼트4__icontains=search) |Q(배터리__icontains=search) |
                Q(어댑터__icontains=search) |Q(충전단자__icontains=search) |
                Q(게임관련기능__icontains=search) |Q(PANTONE__icontains=search) |
                Q(무게__icontains=search) |Q(고속충전__icontains=search) |
                Q(셀룰러__icontains=search) |Q(지문인식__icontains=search) |
                Q(쿨링팬__icontains=search) |Q(터치스크린__icontains=search) |
                Q(트루톤__icontains=search) |Q(화면회전각__icontains=search) 
            )
            print(len(search_lists))
            products = Products.objects.all()
            # 카테고리 분류
            category = request.GET.get("category","")
            if category:
                products_category = Products.objects.filter(Q(제조회사__contains=category))
            else:
                products_category = products
            brand = request.GET.get("brand","")
            if brand:
                products_brand = Products.objects.filter(Q(제조회사__contains=brand))
            else:
                products_brand = products
            # 가격 분류  1,2,3,4,5
            price = request.GET.get("price","")
            if price:
                products_price = Products.objects.filter(Q(가격등급__contains=price))
            else:
                products_price = products
            # 무게 분류  1,2,3,4
            weight = request.GET.get("weight","")
            if weight:
                products_weight = Products.objects.filter(Q(무게등급__contains=weight))
            else:
                products_weight = products
            # 프로세스 분류 AMD, INTEL, 애플
            processor = request.GET.get("processor","")
            if processor:
                products_processor = Products.objects.filter(Q(CPU제조사분류__contains=processor))
            else:
                products_processor = products
            # 프로세스 분류 4000, 5000, 6000, i3, i5, i7, i9, 기타, m1, m2
            processor_number = request.GET.get("processor_number","")
            if processor_number:
                products_processor_number = Products.objects.filter(
                    Q(CPU넘버분류__contains=processor_number)
                )
            else:
                products_processor_number = products
            # 저장용량등급 분류  1,2,3,4
            storage = request.GET.get("storage","")
            if storage:
                products_storage = Products.objects.filter(Q(저장용량등급__contains=storage))
            else:
                products_storage = products
            # GPU종류등급 분류  1,2
            graphic = request.GET.get("graphic","")
            if graphic:
                products_graphic = Products.objects.filter(Q(GPU종류등급__contains=graphic))
            else:
                products_graphic = products
            # 해상도등급 분류  "FHD","QHD","UHD"
            resolution = request.GET.get("resolution","")
            if resolution:
                products_resolution = Products.objects.filter(Q(해상도등급__contains=resolution))
            else:
                products_resolution = products
            # 화면크기등급 분류  1,2,3
            size = request.GET.get("size","")
            if size:
                products_size = Products.objects.filter(Q(화면크기등급__contains=size))
            else:
                products_size = products
            result = search_lists&products_category&products_price&products_weight&products_processor&products_processor_number&products_storage&products_graphic&products_resolution&products_size&products_brand
            print(len(result))
            page = request.GET.get("page", "1")
            paginator = Paginator(result, 6)
            page_obj = paginator.get_page(page)
            context = {
                "brand": brand,
                "price": price,
                "weight": weight,
                "processor": processor,
                "processor_number": processor_number,
                "storage": storage,
                "graphic": graphic,
                "resolution": resolution,
                "size": size,
                "search_lists": search_lists,
                "s": s,
                "search": search,
                "search_count": len(result),
                "page_obj": page_obj,
            }
            return render(request, "products/index.html", context)
        
        else:
            return redirect('products:index')