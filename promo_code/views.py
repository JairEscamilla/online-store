from django.shortcuts import render
from django.http import JsonResponse
from .models import PromoCode
from carts.utils import get_or_create_cart
from orders.utils import get_or_create_order


# Create your views here.
def validate(request):
    code = request.GET.get("code")
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    promo_code = PromoCode.objects.filter(code=code).first()

    if promo_code is None:
        return JsonResponse({
            "status": False
        }, status=404)
    

    order.apply_promo_code(promo_code)

    return JsonResponse({
        "status": True,
        "code": promo_code.code,
        "discount": promo_code.discount,
        'total': order.total
    })
