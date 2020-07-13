from django.shortcuts import render
from .models import Order
from carts.utils import get_or_create_cart
from .utils import get_or_create_order, breadcrumb
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    shipping_address = order.shipping_address

    return render(request, 'orders/order.html', {'cart': cart, 'order': order, 'breadcrumb': breadcrumb})

@login_required(login_url="login")
def address(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    return render(request, "orders/address.html", {'cart': cart, 'order': order, 'breadcrumb': breadcrumb(address=True)})