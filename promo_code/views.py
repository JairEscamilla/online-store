from django.shortcuts import render
from django.http import JsonResponse
from .models import PromoCode

# Create your views here.
def validate(request):
    code = request.GET.get("code")

    promo_code = PromoCode.objects.filter(code=code).first()

    if promo_code is None:
        return JsonResponse({
            "status": False
        }, status=404)
    


    return JsonResponse({
        "status": True,
        "code": promo_code.code,
        "discount": promo_code.discount
    })
