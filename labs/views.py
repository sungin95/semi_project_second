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
        search = request.GET.get("category", "")

        if len(search) >= 1:
            if Search.objects.filter(keyword=search).exists():
                search_keyword = Search.objects.get(keyword=search)
                search_keyword.count += 1
                search_keyword.save()
            else:
                Search.objects.create(keyword=search, count=1)

        a = list(Products.objects.values()[0].keys())
        remove_set = {'id', '썸네일', '이미지1', '이미지2', '이미지3', '안전확인인증', '적합성평가인증'}
        a = [i for i in a if i not in remove_set]

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
            context = {
                "search_lists": search_lists,
                "s": s,
                "search": search,
                "a": a,
            }
            return render(request, "products/index.html", context)