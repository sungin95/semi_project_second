from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Products
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# 장바구니 생성 함수
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# 장바구니에 추가하는 함수
def add_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect("cart:detail")


def detail(request, total=0, counter=0, total_plus=0, total_dc=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += cart_item.product.가격 * cart_item.quantity
            total_plus += int(
                round(((cart_item.product.가격) * 1.1) * cart_item.quantity, -4)
            )
            counter += cart_item.quantity
            cart_item.product.ten_price = int(round((cart_item.product.가격) * 1.1))
            cart_item.product.save()
        total_dc = total_plus - total

    except ObjectDoesNotExist:
        pass
    return render(
        request,
        "cart/cart.html",
        dict(
            cart_items=cart_items,
            total=total,
            counter=counter,
            total_plus=total_plus,
            total_dc=total_dc,
        ),
    )


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("cart:detail")
