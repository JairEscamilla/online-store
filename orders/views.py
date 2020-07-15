from django.shortcuts import render
from .models import Order
from carts.utils import get_or_create_cart
from .utils import get_or_create_order, breadcrumb
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from shipping_addresses.models import ShippingAddress
from django.contrib import messages
from .utils import destroy_order
from carts.utils import destroy_cart
from .mails import Mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet
from .decorators import validate_cart_and_order
import threading
# Create your views here.

class OrderListView(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "orders/orders.html"
    
    def get_queryset(self):
        return self.request.user.orders_completed()


@login_required(login_url='login')
@validate_cart_and_order
def order(request, cart, order):
    shipping_address = order.shipping_address

    return render(request, 'orders/order.html', {'cart': cart, 'order': order, 'breadcrumb': breadcrumb})

@login_required(login_url="login")
@validate_cart_and_order
def address(request, cart, order):
    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.shippingaddress_set.count()

    return render(request, "orders/address.html", {'cart': cart, 'order': order, 'breadcrumb': breadcrumb(address=True), 'shipping_address': shipping_address, 'can_choose_address': can_choose_address})

@login_required(login_url="login")
def select_address(request):
    
    sp = request.user.shippingaddress_set.all()

    return render(request, "orders/select_address.html", {
        'breadcrumb': breadcrumb(address=True),
        'sp': sp
    })

@login_required(login_url="login")
@validate_cart_and_order
def check_address(request, cart, order, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect("carts:cart")
    
    order.update_shipping_address(shipping_address)
    return redirect('orders:address')

@login_required(login_url="login")
@validate_cart_and_order
def confirm(request, cart, order):

    shipping_address = order.shipping_address

    if shipping_address is None:
        return redirect("orders:address")

    return render(request, "orders/confirm.html", {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'breadcrumb': breadcrumb(address=True, confirmation=True)
    })

@login_required(login_url="login")
@validate_cart_and_order
def cancel(request, cart, order):

    if request.user.id != order.user.id:
        return redirect("carts:cart")
    
    order.cancel()
    destroy_cart(request)
    destroy_order(request)

    messages.error(request, "Orden cancelada")

    return redirect("index")

@login_required(login_url="login")
@validate_cart_and_order
def complete(request, cart, order):
    if request.user.id != order.user_id:
        return redirect("carts:cart")
    
    order.complete()

    thread = threading.Thread(target=Mail.send_complete_order, args = (
        order, request.user
    ))

    thread.start()

    destroy_cart(request)
    destroy_order(request)

    messages.success(request, "Compra completada exitosamente")

    return redirect("index")