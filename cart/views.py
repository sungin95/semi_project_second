from django.shortcuts import render, redirect
from .models import Cart, CartItem
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
    product = Product.objects.get(id=product_id)
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


def detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id="c1")
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += 1290000 * cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(
        request,
        "cart/cart.html",
        dict(cart_items=cart_items, total=total, counter=counter),
    )
